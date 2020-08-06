"""
для использования надо скачать нужный xml файл
https://github.com/opencv/opencv/tree/master/data/haarcascades
"""
import cv2

faceCascade = cv2.CascadeClassifier("nameDownloadFile.xml")
img = cv2.imread('baba.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)

cv2.imshow("Result", img)
cv2.waitKey(0)
