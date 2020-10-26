import cv2
import numpy as np


img = cv2.imread("test.png", 0)
kernel = np.zeros((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("img", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()