import cv2 as cv

#img = cv.imread('Photos\City_Skyline.jpg')

#cv.imshow('City Skyline', img)

#A function to rescale a frame
def rescaleFrame(frame, scale=0.75):
    #shape[1] is the width of the frame, which is then multipled by the scale and casted as a int
    width = int(frame.shape[1] * scale)
    #shape[0] is the height of the frame, which is then multipled by the scale and casted as a int
    height = int(frame.shape[0] * scale)
    
    #Creates a table with the scaled width and height
    dimensions = (width, height)
    
    #Returns the frame resized into a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos\Infinite_Loop.mp4')

while True:
    
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()