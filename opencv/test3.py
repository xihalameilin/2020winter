import cv2
import numpy as np
from matplotlib import pyplot as plt


# 此文件试图给图片补上竖着的线

# 0 黑色  255 白色
img = cv2.imread('test.png', 0)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

shape = img.shape
print(shape)
row = shape[0]
col = shape[1]
count = 0

# 获取图片的横线
lines = []
for i in range(row):
    count = 0
    for j in range(col):
        px = img[i, j]
        if px == 0:
            count += 1
    if count > int(3 * row / 2):
        lines.append(i)
print("一共找到如下横线" + str(lines))
linesNum = len(lines)

xBegin = 0
for i in range(col):
    if img[lines[0], i] == 0:
        xBegin = i
        break

xEnd = 0
for i in range(col - 1, 0, -1):
    if img[lines[0], i] == 0:
        xEnd = i
        break
print("x" + str(xBegin) + " x" + str(xEnd))

myList = []
last = -1
for i in range(col):
    count = 0
    for j in range(row):
        px = img[j, i]
        if px == 0:
            count += 1
    if count <= linesNum:
        myList.append(i)
print(myList)

newList = []
i = 0
while i < len(myList):
    temp = []
    for j in range(myList[i], myList[-1]):
        if j in myList:
            temp.append(j)
            i += 1
        else:
            i -= 1
            break
    i += 1
    newList.append(temp)

# 最左边的边处理 最右边的边处理
newList.remove(newList[0])
newList.remove(newList[-1])
cv2.line(img, (xBegin, lines[0]), (xBegin, lines[-1]), (0, 0, 0), 1)
cv2.line(img, (xEnd, lines[0]), (xEnd, lines[-1]), (0, 0, 0), 1)

for i in newList:
    print(len(i))
    if len(i) > 15:
        num = int((i[0] + i[-1]) / 2)
        cv2.line(img, (num, lines[0]), (num, lines[-1]), (0, 0, 0), 1)



cv2.imshow('image', img)
#cv2.imwrite("hhhh.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
