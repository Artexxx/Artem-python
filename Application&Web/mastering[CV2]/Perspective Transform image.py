"""
perspective_transform.py -- осуществляет перспективную трансформацию с live камерой
    Пусть * - края объекта, который мы хотим перспективно трансформировать
    Тогда перспективная трансформировация выглядит примерно так:
    |  *   *  | -> |*     *|
    |*       *|    |*     *|
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    height, width = img.shape[:2]

    cv2.circle(img, (width * 2 // 6, 0), 7, (0, 0, 255), -1)
    cv2.circle(img, (width * 4 // 6, 0), 7, (0, 0, 255), -1)
    cv2.circle(img, (0, height), 7, (0, 0, 255), -1)
    cv2.circle(img, (width, height), 7, (0, 0, 255), -1)

    pts1 = np.float32([[width * 2 // 6, 0], [width * 4 // 6, 0], [0, height], [width, height]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (width, height))

    cv2.imshow("camera", result)
    if cv2.waitKey(10) == 27:  # press `Esc`
        break

cap.release()
cv2.destroyAllWindows()
