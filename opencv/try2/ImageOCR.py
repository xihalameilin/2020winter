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

        self.horizontal_line_list = []
        self.vertical_line_list = []

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
        self.horizontal_line_list = horizontal_line_list
        self.vertical_line_list = vertical_line_list
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
        vertical_lines = self.vertical_line_list
        horizontal_lines = self.horizontal_line_list
        print(horizontal_lines)
        print(vertical_lines)
        self.show_image(self.blank_image)
        # 区域列表
        rects = []
        # for i in range(1, len(vertical_lines) - 1):
        #     for j in range(1, len(horizontal_lines) - 1):
        #         rects.append((horizontal_lines[j], horizontal_lines[j + 1],
        #                       vertical_lines[i], vertical_lines[i + 1]))
        #         row_label_image = self.blank_image[horizontal_lines[j]: horizontal_lines[j + 1],
        #                       vertical_lines[0]: vertical_lines[1]]
        #         col_label_image = self.blank_image[horizontal_lines[0]: horizontal_lines[1],
        #                       vertical_lines[i]: vertical_lines[i + 1]]
        #         content_image = self.blank_image[horizontal_lines[j]:horizontal_lines[j + 1],
        #                       vertical_lines[i]: vertical_lines[i + 1]]
        #         self.show_image(row_label_image)
        #         self.show_image(col_label_image)
        #         self.show_image(content_image)

        res = []
        for i in range(0, len(horizontal_lines) - 1):
            temp = []
            for j in range(0, len(vertical_lines) - 1):
                item = self.blank_image[horizontal_lines[i]:horizontal_lines[i+1],
                       vertical_lines[j]:vertical_lines[j+1]]
                # 增加识别代码
                self.show_image(item)
                content = self.ocr(item)
                print(content)
                temp.append(content)
            res.append(temp)
        print(res)

        # 打印三元组
        for i in range(1, len(horizontal_lines) - 1):
            for j in range(1, len(vertical_lines) - 1):
                content = res[i][j]
                row_label = res[i][0]
                col_label = res[0][j]
                print("三元组结果:content:{}row:{}col:{}".format(content, row_label, col_label))
        return rects

    # 识别单元格中的文字
    def ocr(self, image):
        # 特殊字符列表
        special_char_list = ':|\'\"?![]()~#$%^&*_+-={};<>/¥\n'
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        text = pytesseract.image_to_string(image)
        print(text)
        return ''.join([x for x in text if x not in special_char_list])

    # 显示图像
    def show_image(self, image):
        cv2.imshow('cell_res', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__' :
    ocr = ImageTableOCR("../1.png")
    ocr.draw()
    ocr.cell_detect()