import cv2 as cv


# 图片膨胀
def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (12, 4))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate", dst)
    return dst


# 获取竖线 调用两次
def get_vertical_lines(image, ratio=0.94):
    row = image.shape[0]
    col = image.shape[1]
    vertical_lines = []
    for i in range(col):
        count = 0
        for j in range(row):
            px = image[j, i]
            if px == 0:
                count += 1
        if count > int(row * ratio):
            vertical_lines.append(i)
    print("一共找到如下竖线" + str(vertical_lines))
    return vertical_lines


# 获取横线 调用一次
def get_level_lines(image, ratio=0.9):
    row = image.shape[0]
    col = image.shape[1]
    level_lines = []
    for i in range(row):
        count = 0
        for j in range(col):
            px = image[i, j]
            if px == 0:
                count += 1
        if count > int(col * ratio):
            level_lines.append(i)
    print("一共找到如下横线" + str(level_lines))
    return level_lines


def get_vertical_list(vertical_list):
    res_list = []
    i = 0
    while i < len(vertical_list):
        temp = []
        for j in range(vertical_list[i], vertical_list[-1]):
            if j in vertical_list:
                temp.append(j)
                i += 1
            else:
                i -= 1
                break
        i += 1
        res_list.append(temp)
    print("一共找到{}条竖线".format(str(len(res_list))))
    print(res_list)
    return res_list


def draw(image, res_list , stop_list , level_lines):
    # cv.line(image, (res_list[0][-1], level_lines[0]), (res_list[0][-1], level_lines[-1]), (0, 0, 0), 1)
    # cv.line(image, (res_list[-1][0], level_lines[0]), (res_list[-1][0], level_lines[-1]), (0, 0, 0), 1)
    if len(res_list) < 2:
        return
    res_list.remove(res_list[0])
    res_list.remove(res_list[-1])
    for i in res_list:
        if len(i) > 5:
            num = int((i[0] + i[1]) / 2)
            if judge(num, stop_list):
                cv.line(image, (num, level_lines[0]), (num, level_lines[-1]), (0, 0, 0), 1)


def judge(num, stop_list):
    for i in stop_list:
        if abs(i - num) <= 20:
            return False
    return True


def getxbegin(img, lines):
    col = img.shape[1]
    for i in range(col):
        if img[lines[0], i] == 0:
            xBegin = i
            break
    return xBegin


def getxend(img, lines):
    col = img.shape[1]
    for i in range(col - 1, 0, -1):
        if img[lines[0], i] == 0:
            xEnd = i
            break
    return xEnd
src = cv.imread("../7.png", 0)
ret, binary = cv.threshold(src, 200, 255, cv.THRESH_BINARY)

stop_list = get_vertical_lines(binary, ratio=0.9)
level_lines = get_level_lines(binary)
x_begin = getxbegin(binary, level_lines)
x_end = getxend(binary, level_lines)

src = cv.imread("../7.png")
gray = dilate_demo(src)
vertical_lines = get_vertical_lines(gray, ratio=0.9)
res_list = get_vertical_list(vertical_lines)
draw(src, res_list=res_list, stop_list=stop_list, level_lines=level_lines)

if len(res_list) >= 2:
    cv.line(src, (x_begin, level_lines[0]), (x_begin, level_lines[-1]), (0, 0, 0), 1)
    cv.line(src, (x_end, level_lines[0]), (x_end, level_lines[-1]), (0, 0, 0), 1)

cv.imshow("res", src)
cv.waitKey(0)
cv.destroyAllWindows()
