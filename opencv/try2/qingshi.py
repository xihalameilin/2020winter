import cv2 as cv
import numpy as np
img = cv.imread('test.png', 0)
print(img.shape)
ret, img = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
kernel = np.zeros((10, 5), np.uint8)
dilation = cv.dilate(img, kernel, iterations=1)
cv.imshow("img1", img)
cv.imshow("img2", dilation)
cv.waitKey(0)
cv.destroyAllWindows()