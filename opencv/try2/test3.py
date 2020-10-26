import cv2 as cv


def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (12, 4))
    dst = cv.dilate(binary, kernel)
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (5, 10))
    dst = cv.dilate(dst, kernel2)
    cv.imshow("dilate", dst)
    return dst


img = cv.imread("../1.png")
dilate_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()