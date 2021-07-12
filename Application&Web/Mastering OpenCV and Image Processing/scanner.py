import cv2
import numpy as np


def pre_processing(image):
    """ Нужно для определения границ (делает контур объектов толще)"""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (5, 5), 1)
    canny_image = cv2.Canny(blur_image, 200, 200)
    kernel = np.ones((5, 5))
    dial_image = cv2.dilate(canny_image, kernel, iterations=2)
    thres_image = cv2.erode(dial_image, kernel, iterations=1)
    return thres_image


def get_contours(image):
    """ Находит самый большой контур, похожий на прямоугольник """
    global raw_image
    biggest = np.array([])
    max_area = 0
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(raw_image, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    cv2.drawContours(raw_image, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder(points):
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), np.int32)
    add = points.sum(1)
    new_points[0] = points[np.argmin(add)]
    new_points[3] = points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]
    return new_points


def get_warp(image, biggest):
    """ Получение фотки документа """
    width, height = image.shape[:2]
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    perspective_image = cv2.warpPerspective(image, matrix, (width, height))

    cropped_image = perspective_image[20:perspective_image.shape[0] - 20, 20:perspective_image.shape[1] - 20]
    cropped_image = cv2.resize(cropped_image, (width, height))
    return cropped_image


cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    raw_image = image.copy()
    biggest = get_contours(pre_processing(image))
    if biggest.size != 0:
        warped_image = get_warp(image, biggest)
        cv2.imshow("Document", warped_image)
    cv2.imshow("WorkFlow", raw_image)
    if cv2.waitKey(10) == 27: break  # press `ESC`
cap.release()
cv2.destroyAllWindows()
