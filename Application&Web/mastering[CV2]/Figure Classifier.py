""" figure_сlassifier.py - обнаруживает формы фигур по количеству угловых точек"""
import cv2


def get_object_type(count_points, width, height):
    if count_points == 3:
        return "triangle."
    elif count_points == 4:
        asp_ratio = width / float(height)
        if asp_ratio > 0.95 and asp_ratio < 1.05:
            return "square"
        else:
            return "rectangle"
    elif count_points > 4:
        return "circle"
    return "don't know"


def get_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 3400:
            # Обводит найденную фигуру красным
            cv2.drawContours(imageContour, contour, -1, (0, 0, 255), thickness=7)
            # Нахождим угловые точки
            perimeter = cv2.arcLength(contour, closed=True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, closed=True)
            count_points = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # Помещаем найденную фигуру в квадрат и подписываем её название
            cv2.rectangle(imageContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(imageContour, get_object_type(count_points, w, h),
                        (x + (w // 2) - 50, y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)


image = cv2.imread('figureImg.jpg')
imageContour = image.copy()
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (7, 7), 1)
imageCanny = cv2.Canny(imageBlur, 50, 50)
get_contours(imageCanny)
cv2.imshow("classifier", imageContour)
cv2.waitKey(0)
