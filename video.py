
import numpy as np
import cv2

frameCounter = 0

cap = cv2.VideoCapture('movie_002.mp4')

while True:
  _, frame = cap.read()
  if frame is None:
    break
  cv2.imshow('app', frame)
  frameCounter += 1
  print(frameCounter)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()