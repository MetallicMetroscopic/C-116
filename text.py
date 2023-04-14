import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img, 'Sun', (100,80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,0,255), 2)
cv2.putText(img, 'Mercury', (115,190), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Venus', (190,270), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Earth', (290,270), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Mars', (385,270), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Jupiter', (485,80), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Saturn', (780,110), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Uranus', (970,140), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
cv2.putText(img, 'Neptune', (1110,140), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)


cv2.imshow('Solar system', img)
cv2.waitKey(0)