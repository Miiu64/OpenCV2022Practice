#imports cv2 but named as cv
import cv2 as cv


#Reading images


#Reads an image in a path and returns it as a matrix of pixels
img = cv.imread('Photos\City_Skyline.jpg')

#Shows the image in a new window named after the paramter
cv.imshow('City Skyline', img)


#Reading videos


#Captures 0 for webcam, 1 for first camera, etc.
#Also captures video in file path
capture = cv.VideoCapture('Videos\Infinite_Loop.mp4')

while True:
    #reads video frame by frame, always returns true when the frame was successfully read
    isTrue, frame = capture.read()
    #Shows video frame by frame
    cv.imshow('Video', frame)
    
    #Breaks the loop when 20 miliseconds and the letter d is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#Releases capture device
capture.release()
#Destroys all Windows
cv.destroyAllWindows()

#Waits an infinite amount of time for a key pressed
#cv.waitKey(0)



