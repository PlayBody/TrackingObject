import cv2
import numpy as np
import math

class TrackEngine:
    def __init__(self) -> None:
        pass
    
    def run(self, path):

        trackArray = []
        # Read video
        cap = cv2.VideoCapture(path) 

        # Initialize object detector
        object_detector = cv2.createBackgroundSubtractorMOG2(1500, 300, False)


        prevBoxes = []
        # Iterate through frames
        while True:
            # Read frame
            ret, frame = cap.read()

            if ret is False:
                break

            # Detect objects
            mask = object_detector.apply(frame)
            
            # Find contours
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # contoured = frame.copy()
            # cv2.drawContours(contoured, contours, -1, (255, 255, 255), 3)
            
            boxes = []
            # Draw bounding boxes
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w < 10 or h < 10:
                    continue
                if w > 200 or h > 200:
                    continue
                roi = frame[y:y+h, x:x+w]
                nx = x + w/2
                ny = y + h/2

                score = 1e9
                if len(prevBoxes) > 0:
                    for prev in prevBoxes:
                        nscore = math.hypot(prev[0] - nx, prev[1] - ny)
                        if nscore < score:
                            score = nscore
                
                boxes.append([nx, ny, score])
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)
            
            if len(boxes) > 0:
                prevBoxes = boxes
            trackArray.append(boxes)
            # Display output  
            cv2.imshow('Frame', frame)
            # cv2.imshow('Contour', contoured)
            
            # Break if 'q' pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        # Release resources
        cap.release()
        cv2.destroyAllWindows()
        
        return trackArray