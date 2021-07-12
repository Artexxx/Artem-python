import cv2
import numpy as np

COLORS = {
    'pink': [133, 56, 0, 159, 156, 255],
    'green': [57, 76, 0, 100, 255, 255],
}
ColorValues = [[180, 105, 255],
               [0, 255, 0], ]

# [x , y , colorId ]
points = []


def find_color(image, COLORS, ColorValues):
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_points = []
    for count, colorName in enumerate(COLORS):
        lower = np.array(COLORS[colorName][0:3])
        upper = np.array(COLORS[colorName][3:6])
        mask = cv2.inRange(imageHSV, lower, upper)
        x, y = get_contours_coordinats(mask)
        cv2.circle(imageResult, (x, y), 15, ColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, count])
        cv2.imshow(colorName, mask)
    return new_points


def get_contours_coordinats(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imageResult, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def draw_on_canvas(points, ColorValues):
    for point in points:
        cv2.circle(imageResult, (point[0], point[1]), 10, ColorValues[point[2]], cv2.FILLED)


cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    imageResult = image.copy()
    new_points = find_color(image, COLORS, ColorValues)
    if len(new_points) != 0:
        for point in new_points:
            points.append(point)
    if len(points) != 0:
        draw_on_canvas(points, ColorValues)

    cv2.imshow("Result", imageResult)
    if cv2.waitKey(10) == 27: break  # press `ESC`
cap.release()
cv2.destroyAllWindows()
