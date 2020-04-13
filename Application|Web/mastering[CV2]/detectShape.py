""" detectShape.py -- обнаруживает формы фигур по количеству угловых точек"""
import cv2


def getObjectType(numPoints, width, height):
    if numPoints == 3:
        return "триуг."
    elif numPoints == 4:
        aspRatio = width / float(height)
        if aspRatio > 0.95 and aspRatio < 1.05:
            return "квадрат"
        else:
            return "прямоуг."
    elif numPoints > 4:
        return "круг"
    return "не знаю"


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 3400:
            # обвести найденную фигуру красным
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 255), thickness=7)
            # нахождение угловых точек
            peri = cv2.arcLength(cnt, closed=True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, closed=True)
            numPoints = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # поместить найденную фигуру в квадрат и подписать её тип
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(imgContour, getObjectType(numPoints, w, h),
                        (x + (w // 2) - 50, y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 0, 0), 2)


img = cv2.imread('figureImg.jpg')
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)
cv2.imshow("classifier", imgContour)

cv2.waitKey(0)
