import cv2 as cv

cap = cv.VideoCapture('Taiwan.mp4')

roi = None
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True:
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if roi ==None:
        roi = cv.selectROI(frame)
    
    startPoint = (roi[0], roi[1])
    endPoint = (roi[0]+roi[2], roi[1]+roi[3])
    print("roi: ", roi)
    cv.rectangle(frame,startPoint,endPoint,(0,255,0), 2)
    
    # Display the resulting frame 
    cv.imshow('Frame', frame)
    

    

   
    # Press Q on keyboard to  exit 
    if cv.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break