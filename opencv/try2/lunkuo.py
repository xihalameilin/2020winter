import cv2

rect_width = 10
rect_height = 5


def get_vertical_lines_2(image, line_count):
    row = image.shape[0]
    col = image.shape[1]
    vertical_lines = []
    for i in range(col):
        count = 0
        for j in range(row):
            px = image[j, i]
            if px == 255:
                count += 1
        if count > row - int(rect_height * line_count * 1.6):
            vertical_lines.append(i)
    print("一共找到如下竖线" + str(vertical_lines))
    return vertical_lines


def get_continuous_lines(vertical_list):
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
        if len(temp) > 5:
            res_list.append(temp)
    print("一共找到{}条连续线".format(str(len(res_list))))
    print(res_list)
    return res_list


img = cv2.imread('../test3.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (rect_width, rect_height))
dst = cv2.dilate(binary, kernel)

contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# epsilon = cv2.arcLength(contours[1], True)
# approx = cv2.approxPolyDP(contours[1], epsilon, True)
cv2.drawContours(img, contours, -1, (0, 0, 0), 2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
vertical_liens = get_vertical_lines_2(binary, 4)
res_list = get_continuous_lines(vertical_liens)
for i in res_list:
    num = int((i[0] + i[-1])/2)
    cv2.line(img, (num, 0), (num, img.shape[1]), (0, 0, 0), 1)
cv2.imshow("img", img)
cv2.waitKey(0)