import cv2 as cv
import numpy as np

def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (6, 2))
    dst = cv.dilate(binary, kernel)
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (2, 6))
    dst = cv.dilate(dst, kernel2)
    cv.imshow("dilate", dst)
    return dst


def close(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (6, 2))
    dst = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    kernel2 = np.ones((2, 4), np.uint8)
    dst = cv.dilate(dst, kernel2, iterations=1)
    cv.imshow("dilate", dst)
    return dst

img = cv.imread("../7.png")
dilate_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()