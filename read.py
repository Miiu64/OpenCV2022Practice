#imports cv2 but named as cv
import cv2 as cv


#Reading images


#Reads an image in a path and returns it as a matrix of pixels
#img = cv.imread('Photos\City_Skyline.jpg')

#Shows the image in a new window named after the paramter
#cv.imshow('City Skyline', img)


#Reading videos


#Captures 0 for webcam, 1 for first camera, etc.
#Also captures video in file path
capture = cv.VideoCapture('Videos\Astronaut.gif')

