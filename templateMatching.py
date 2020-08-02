import cv2 as cv

cap = cv.VideoCapture('Taiwan.mp4')

r = None
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True:
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if r ==None:
        r = cv.selectROI(frame)
    
    # Display the resulting frame 
    cv.imshow('Frame', frame)

   
    # Press Q on keyboard to  exit 
    if cv.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break