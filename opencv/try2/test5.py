import cv2 as cv
import numpy as np

image = cv.imread("../1.png")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("res", gray)
cv.waitKey(0)
cv.destroyAllWindows()
ret, thresh1 = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
h, w = gray.shape

# 横向直线列表
horizontal_lines = []
for i in range(h - 1):
    # 找到两条记录的分隔线段，以相邻两行的平均像素差大于120为标准
    if np.mean(gray[i, :]) - np.mean(gray[i + 1, :]) > 100:
        print(np.mean(gray[i, :]))
        print(np.mean(gray[i + 1, :]))
        print("-----------------")