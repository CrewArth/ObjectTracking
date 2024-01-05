import cv2

cap = cv2.VideoCapture(1)

tracker = cv2.TrackerCSRT_create()
ret, frame = cap.read()
boundingBox = cv2.selectROI('Object Detection', frame, False)

tracker.init(frame, boundingBox)

def drawBox(frame, boundingBox):
    x, y, w, h = int(boundingBox[0]), int(boundingBox[1]), int(boundingBox[2]), int(boundingBox[3])
    cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (255,0,0), 3)

while True:
    ret, frame = cap.read()

    ret, boundingBox = tracker.update(frame)

    if ret:
        drawBox(frame, boundingBox)
        cv2.putText(frame, "Tracking Object", (40,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    else:
        cv2.putText(frame, "Lost Object", (40,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)    
    timer = cv2.getTickCount()
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, str(int(fps)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    cv2.imshow('Object Detection', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()