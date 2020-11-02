import cv2
import numpy as np
import pytesseract


class ImageTableOCR(object):
    # 初始化
    def __init__(self, ImagePath):
        # 读取图片
        self.image = cv2.imread(ImagePath)
        self.copy_image = cv2.imread(ImagePath)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.horizontal_lines = self.horizontal_line_detect()
        self.vertical_lines = self.vertical_line_detect()
        self.blank_image = self.clear_lines()

    # 横向直线检测
    def horizontal_line_detect(self):
        h, w = self.gray.shape
        # 横向直线列表
        horizontal_lines = []
        for i in range(h - 1):
            # 找到两条记录的分隔线段，以相邻两行的平均像素差大于120为标准
            if np.mean(self.gray[i, :]) - np.mean(self.gray[i + 1, :]) > 120:
                horizontal_lines.append([0, i, w, i])
        print("一共找到如下原图中的横线" + str(horizontal_lines))
        return horizontal_lines

    #  纵向直线检测
    def vertical_line_detect(self):
        h, w = self.gray.shape
        # 纵向直线列表
        vertical_lines = []
        for i in range(w - 1):
            if np.mean(self.gray[:, i]) - np.mean(self.gray[:, i]) > 120:
                vertical_lines.append((i, 0, i, h))
        print("一共找到如下原图中的竖线" + str(vertical_lines))
        return vertical_lines

    # 将原图的线去掉
    def clear_lines(self):
        image = self.copy_image
        h, w = image.shape[:2]
        for i in self.horizontal_lines:
            index = i[1]
            low = 0 if index - 1 < 0 else index - 1
            high = w if index + 2 > w else index + 2
            for j in range(low, high):
                image[j, 0:w] = [255, 255, 255]
        for i in self.vertical_lines:
            index = i[0]
            low = 0 if index - 1 < 0 else index - 1
            high = h if index + 2 > h else index + 2
            for j in range(low, high):
                image[0:h, j] = [255, 255, 255]
        return image

    # 得到竖直的空白区域
    def get_vertical_areas(self):
        row_, col_ = self.gray.shape
        # 步长 col_step
        col_step = int(col_ / 40)
        gray = self.gray
        vertical_lines = []
        for col in range(0, col_, col_step):
            roi = gray[0:row_, col:col + col_step]
            dev = np.std(roi)
            mean = np.mean(roi)
            if dev < 30 and mean > 245:
                vertical_lines.append(col)
        return vertical_lines, col_step

    def get_horizontal_areas(self):
        row_, col_ = self.gray.shape
        # 步长 row_step
        row_step = int(row_ / 40)
        gray = self.gray
        level_lines = []
        for row in range(0, row_, row_step):
            roi = gray[row:row + row_step, 0: col_]
            dev = np.std(roi)
            mean = np.mean(roi)
            if dev < 30 and mean > 245:
                level_lines.append(row)
        return level_lines, row_step

    # 得到连续的区域
    def get_lines_to_be_draw(self):
        vertical_lines, col_step = self.get_vertical_areas()
        vertical_line_list = []
        i = 0
        while i < len(vertical_lines):
            standard = vertical_lines[i]
            temp = [standard]
            while i + 1 < len(vertical_lines) and vertical_lines[i] + col_step == vertical_lines[i + 1]:
                temp.append(vertical_lines[i+1])
                i += 1
            if len(temp) > 1:
                vertical_line_list.append(int((temp[0] + temp[-1])/2))
            elif len(temp) == 1:
                vertical_line_list.append(temp[0])
            i += 1

        horizontal_lines, row_step = self.get_horizontal_areas()
        horizontal_line_list = []
        i = 0
        while i < len(horizontal_lines):
            standard = horizontal_lines[i]
            temp = [standard]
            while i + 1 < len(horizontal_lines) and horizontal_lines[i] + row_step == horizontal_lines[i + 1]:
                temp.append(horizontal_lines[i+1])
                i += 1
            if len(temp) > 1:
                horizontal_line_list.append(int((temp[0] + temp[-1]) / 2))
            elif len(temp) == 1:
                horizontal_line_list.append(temp[0])
            i += 1
        return horizontal_line_list, vertical_line_list


    def draw(self):
        level_lines_to_be_draw, vertical_lines_to_be_draw = self.get_lines_to_be_draw()
        image = self.blank_image
        for i in vertical_lines_to_be_draw:
            cv2.line(image, (i, level_lines_to_be_draw[0]), (i, level_lines_to_be_draw[-1]), (0, 0, 0), 1)
        for i in level_lines_to_be_draw:
            cv2.line(image, (vertical_lines_to_be_draw[0], i), (vertical_lines_to_be_draw[-1], i), (0, 0, 0), 1)

        return image

    # 顶点检测
    def VertexDetect(self):
        vertical_lines = self.vertical_lines
        horizontal_lines = self.horizontal_lines

        # 顶点列表
        vertex = []
        for v_line in vertical_lines:
            for h_line in horizontal_lines:
                vertex.append((v_line[0], h_line[1]))

        # print(vertex)

        # 绘制顶点
        for point in vertex:
            cv2.circle(self.image, point, 1, (255, 0, 0), 2)

        return vertex

    # 寻找单元格区域
    def cell_detect(self):
        vertical_lines = self.vertical_lines
        horizontal_lines = self.horizontal_lines

        # 顶点列表
        rects = []
        for i in range(0, len(vertical_lines) - 1):
            for j in range(len(horizontal_lines) - 1):
                rects.append((vertical_lines[i][0], horizontal_lines[j][1],
                              vertical_lines[i + 1][0], horizontal_lines[j + 1][1]))

        print(len(rects))
        print(str(rects))
        return rects

    # 识别单元格中的文字
    def ocr(self):
        rects = self.cell_detect()
        image = self.blank_image
        # 特殊字符列表
        special_char_list = '.:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥\n'
        print(self.vertical_lines)
        steps = (len(self.vertical_lines) - 1) * (len(self.horizontal_lines) - 1)
        for i in range(steps):
            rect1 = rects[i]
            DetectImage1 = image[rect1[1]:rect1[3], rect1[0]:rect1[2]]

            # Tesseract所在的路径
            pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
            # 识别数字（每行第一列）
            text = pytesseract.image_to_string(DetectImage1, config="--psm 10")
            print(''.join([x for x in text if x not in special_char_list]))

    # 显示图像
    def show_image(self):
        cv2.imshow('AI', self.draw())
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__' :
    ocr = ImageTableOCR("../1.png")
    ocr.show_image()
    ocr.ocr()