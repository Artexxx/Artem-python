"""
Для использования надо скачать нужный xml файл
https://github.com/opencv/opencv/tree/master/data/haarcascades
"""
import cv2

faceCascade = cv2.CascadeClassifier("nameDownloadFile.xml")
image = cv2.imread('man.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imageGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 5)

cv2.imshow("Result", image)
cv2.waitKey(0)
