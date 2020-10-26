import cv2 as cv
import numpy as np


def erode_demo(image):
   # print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))#定义结构元素的形状和大小
    dst = cv.erode(binary, kernel)#腐蚀操作
    cv.imshow("erode_demo", dst)


def dilate_demo(image):
    #print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))#定义结构元素的形状和大小
    dst = cv.dilate(binary, kernel)#膨胀操作
    cv.imshow("dilate_demo", dst)



src = cv.imread("../test.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
erode_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()
