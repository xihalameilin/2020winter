import cv2 as cv
import numpy as np
import copy
import pytesseract


# def big_image_binary(image):
#     print(image.shape)
#     #整个图像的宽高
#     h, w = image.shape[:2]
#     # 分成小块，每一块的宽高
#     cw = w
#     ch = 5
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     #步长 ch cw
#     for row in range(0, h, ch):
#         for col in range(0, w, cw):
#             #获取分块（感兴趣区域）
#             roi = gray[row:row+ch, col:cw+col]
#             print(np.std(roi), np.mean(roi))
#             dev = np.std(roi)
#             if dev < 15:
#                 gray[row:row + ch, col:cw + col] = 0   #dev < 15的让它变白
#             else:
#                 ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#                 gray[row:row + ch, col:cw + col] = dst
#     cv.imshow("img", gray)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def clear_original_lines(image):
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, image = cv.threshold(image, 180, 255, cv.THRESH_BINARY)
    row = image.shape[0]
    col = image.shape[1]
    level_original_lines = []
    for i in range(row):
        black_count = 0
        for j in range(col):
            px = image[i, j]
            if px == 0:
                black_count += 1
        if black_count > int(8 * col / 10):
            level_original_lines.append(i)
            image[i, 0:col] = 255
    print("一共找到如下原图中的横线" + str(level_original_lines))

    vertical_original_lines = []
    for i in range(col):
        black_count = 0
        for j in range(row):
            px = image[j, i]
            if px == 0:
                black_count += 1
        if black_count > int(8 * row / 10):
            vertical_original_lines.append(i)
            image[0:row, i] = 255
    print("一共找到如下原图中的竖线" + str(vertical_original_lines))
    return image, level_original_lines, vertical_original_lines


def clear(image, level_original_lines, vertical_original_lines):
    print(image.shape)
    row = image.shape[0]
    col = image.shape[1]
    print(image[0, 1])
    for i in level_original_lines:
        low = 0 if i-1 < 0 else i-1
        high = col if i+2 > col else i+2
        for j in range(low, high):
            image[j, 0:col] = [255, 255, 255]
    for i in vertical_original_lines:
        low = 0 if i - 1 < 0 else i - 1
        high = row if i + 2 > row else i + 2
        for j in range(low, high):
            image[0:row, j] = [255, 255, 255]
    return image


# 找竖直的空白区域
def big_image_binary(image):
    row_, col_ = image.shape[:2]
    # 步长 col_step
    col_step = int(col_/40)
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = image
    vertical_lines = []
    for col in range(0, col_, col_step):
        roi = gray[0:row_, col:col + col_step]
        dev = np.std(roi)
        mean = np.mean(roi)
        if dev < 30 and mean > 250:
            gray[0:row_, col:col + col_step] = 0   # 区域变黑
            vertical_lines.append(col)
        # else:
        #     ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        #     gray[0:row_, col:col + col_step] = dst
    return gray, vertical_lines, col_step


# 找水平的空白区域
def big_image_binary_2(image):
    row_, col_ = image.shape[:2]
    # 步长 col_step
    row_step = int(row_/40)
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = image
    level_lines = []
    for row in range(0, row_, row_step):
        roi = gray[row:row + row_step, 0: col_]
        dev = np.std(roi)
        mean = np.mean(roi)
        if dev < 30 and mean > 250:
            level_lines.append(row)
            gray[row:row + row_step, 0: col_] = 0   # 区域变黑
        # else:
        #     ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        #     gray[row:row + row_step, 0: col_] = dst
    return gray, level_lines, row_step


def get_continuous_list(lines, step):
    res_list = []
    i = 0
    while i < len(lines):
        temp = []
        for j in range(lines[i], lines[-1] + 1, step):
            if j in lines:
                temp.append(j)
                i += 1
            else:
                i -= 1
                break
        i += 1
        if len(temp) > 1:
            res_list.append(int((temp[0]+temp[1])/2))
        elif len(temp) == 1:
            res_list.append(temp[0])
    print("一共找到{}条连续要画的线,如下:".format(str(len(res_list))))
    print(res_list)
    return res_list


def draw_lines(image, vertical_lines_to_be_draw, level_lines_to_be_draw):
    for i in vertical_lines_to_be_draw:
        cv.line(image, (i, level_lines_to_be_draw[0]), (i, level_lines_to_be_draw[-1]), (0, 0, 0), 1)
    for i in level_lines_to_be_draw:
        cv.line(image, (vertical_lines_to_be_draw[0], i), (vertical_lines_to_be_draw[-1], i), (0, 0, 0), 1)
    return image


img = cv.imread("../1.png")
img2 = img.copy()
no_lines_image, level_original_lines, vertical_original_lines = clear_original_lines(img)

to_be_draw = clear(img2, level_original_lines, vertical_original_lines)

# cv.imshow("temp", to_be_draw)
# cv.waitKey(0)
# cv.destroyAllWindows()
no_lines_image_copy1 = copy.deepcopy(no_lines_image)
no_lines_image_copy2 = copy.deepcopy(no_lines_image)

image1, vertical_lines, col_step = big_image_binary(no_lines_image)
image2, level_lines, row_step = big_image_binary_2(no_lines_image_copy1)

vertical_lines_to_be_draw = get_continuous_list(vertical_lines, col_step)
level_lines_to_be_draw = get_continuous_list(level_lines, row_step)

res = draw_lines(to_be_draw, vertical_lines_to_be_draw, level_lines_to_be_draw)
cv.imshow("res", to_be_draw[35:55, 3:200])
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(to_be_draw[35:55, 3:200])
print(text)
exclude_char_list = '.:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥\n'
text = ''.join([x for x in text if x not in exclude_char_list])
print(text)
cv.imwrite("post_7.png", res)
cv.waitKey(0)
cv.destroyAllWindows()





