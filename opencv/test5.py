import cv2


# 0 黑色  255 白色
img = cv2.imread('7.png', 0)
ret, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

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
    print(count)
    if count > int(2 * col / 3):
        lines.append(i)
print("一共找到如下横线" + str(lines))
linesNum = len(lines)



# 获取图片的竖线
lines = []
for i in range(col):
    count = 0
    for j in range(row):
        px = img[j, i]
        if px == 0:
            count += 1
    if count > int(2 * row / 3):
        lines.append(i)
print("一共找到如下竖线" + str(lines))
linesNum = len(lines)

cv2.imshow('image', img)
#cv2.imwrite("hhhh.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
