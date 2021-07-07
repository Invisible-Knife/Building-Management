import cv2
 
# Load the Cascade Classifier
body_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_fullbody.xml")
 
#start  web cam
cap = cv2.VideoCapture('videos/cctv_demo.mp4')
 
while cap.isOpened():
     
    #read image from webcam
    respose, color_img = cap.read()
     
    if respose == False:
        break
         
    # Convert to grayscale
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
     
    # Detect the body
    bodies = body_cascade.detectMultiScale(gray_img, 1.1, 3 )
     
    #display rectrangle
    for (x, y, w, h) in bodies:
        cv2.rectangle(color_img, (x, y), (x+w, y+h), (0, 0, 255), 2)
         
        # display image
        cv2.imshow('body detection', color_img)
         
    #press key Q to quit 
    if cv2.waitKey(100) & 0xFF == ord('q'):
            break
   
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
