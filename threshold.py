import cv2
import numpy as np


def threshold_image(img):
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 27, 10)
    # dilate = cv2.dilate(thresh, (7, 7), iterations=2)
    erode = cv2.erode(thresh, (7, 7), iterations=2)
    return erode


img = cv2.imread("./img/light-left.jpg", 0)
thresh_img = threshold_image(img)
# cv2.imwrite("./img/thresh-left.jpg", thresh_img)
cv2.imshow("Threshold", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("./img/light-right.jpg", 0)
thresh_img = threshold_image(img)
# cv2.imwrite("./img/thresh-right.jpg", thresh_img)
cv2.imshow("Threshold", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
