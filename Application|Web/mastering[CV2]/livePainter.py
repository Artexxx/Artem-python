import cv2
import numpy as np

myColors = {
    'pink': [133, 56, 0, 159, 156, 255],
    'green': [57, 76, 0, 100, 255, 255],
}
myColorValues = [[180, 105, 255],
                 [0, 255, 0], ]

# [x , y , colorId ]
myPoints = []

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for count, colorName in enumerate(myColors):
        lower = np.array(myColors[colorName][0:3])
        upper = np.array(myColors[colorName][3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContoursCoordinats(mask)
        cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        cv2.imshow(colorName, mask)
    return newPoints


def getContoursCoordinats(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(10) == 27: break  # press `ESC`
cap.release()
cv2.destroyAllWindows()
