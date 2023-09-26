import cv2 as cv
img = cv.imread("./images/Family.JPEG")

cv.imshow("Display Window", img)
k = cv.waitKey(0)