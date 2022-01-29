import cv2 as cv        #imports cv2 but named as cv

img = cv.imread('')     #Reads an image in a path and returns it as a matrix of pixels

cv.imshow()             #Shows the image in a new window named after the paramter

cv.waitKey(0)           #Waits an infinite amount of time for a key to pressed on a keyboard