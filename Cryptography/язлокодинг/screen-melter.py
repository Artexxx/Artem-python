"""
Создает эффект плавления экрана пользователя.
"""

import pyautogui, cv2, numpy, random
import win32api
import win32con


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))


def main():
    cv2.waitKey(2000)

    image_screenshot = pyautogui.screenshot()
    _array_image = numpy.array(image_screenshot)
    image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)

    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_TOPMOST, cv2.WND_PROP_TOPMOST)

    cv2.setMouseCallback("window", mouse_event)

    cv2.imshow("window", image)

    _width = _array_image.shape[1]  # width
    _height = _array_image.shape[0]  # height
    _columns = 40
    _step = _width // _columns
    _move_down_by = 5

    while True:
        _col = random.randint(0, _columns) * _step
        for i in range(_move_down_by):
            _array_image[i + 1:_height, _col:_col + _step, :3] = _array_image[i:_height - 1, _col:_col + _step, :3]
            image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)
            cv2.imshow("window", image)
        if cv2.waitKey(10) == 27:  # press `Esc`
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
