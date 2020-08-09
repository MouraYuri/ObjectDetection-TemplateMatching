import cv2 as cv
import numpy as np

def searchTemplate(template,img):
    flattenTemplate = np.array(template).flatten()
    for i in range(len(img)-len(template)):
        for j in range(len(img[0])-len(template[0])):
            return

cap = cv.VideoCapture('Taiwan.mp4')

roi = None
template = None
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True:
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if roi ==None:
        roi = cv.selectROI(frame)
        #template = frame[roi[0]:roi[0]+roi[2],roi[1]:roi[1]+roi[3]]
        template = frame[roi[1]:roi[1]+roi[3],roi[0]:roi[0]+roi[2]]

    newFrame = searchTemplate(template, frame)

    startPoint = (roi[0], roi[1])
    endPoint = (roi[0]+roi[2], roi[1]+roi[3])
    #cv.rectangle(frame,startPoint,endPoint,(0,255,0), 2)
    method = 'cv.TM_CCOEFF'
    res = cv.matchTemplate(frame,template, method=4)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    w, h = template.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(frame,top_left, bottom_right, 255, 2)


    # Display the resulting frame 
    cv.imshow('frame', frame)
    

    

   
    # Press Q on keyboard to  exit 
    if cv.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break