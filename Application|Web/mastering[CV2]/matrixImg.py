""" matrixImg.py -- выводит фотку состаящию из склеенных фоток, одинакового размера """
import cv2
import numpy as np


def normalizeImages(imgArray, startImg, scale):
    for x, imgs in enumerate(imgArray):
        for y, img in enumerate(imgs):
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            if img.shape[:2] == startImg.shape[:2]:
                imgArray[x][y] = cv2.resize(img, (0, 0), fx=scale, fy=scale)
            else:
                imgArray[x][y] = cv2.resize(img, (startImg.shape[1], startImg.shape[0]), fx=scale, fy=scale)
    return imgArray


def stackImages(imgArray, *, scale=0.5):
    """
    imgArray: прямоугольная матрица картинок
    scale: во сколько раз уменьшится каждая картинка
    startImg: картинка к которой будут приведены остальные картинки в `imgArray`
    :return: склееные картинки из `imgArray`
    """
    startImg_ = imgArray[0][0]
    imgArray = normalizeImages(imgArray, startImg_, scale)

    rows = len(imgArray)
    imageBlank = np.zeros(startImg_.shape, np.uint8)
    hor = [imageBlank] * rows
    for x in range(0, rows):
        hor[x] = np.hstack(imgArray[x])
    ver = np.vstack(hor)
    return ver


img = cv2.imread('picture.png')

img3 = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
img2 = cv2.cvtColor(img, cv2.COLOR_LRGB2LAB)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

img23 = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
img22 = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
img21 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img33 = cv2.cvtColor(img, cv2.COLOR_HLS2BGR)
img32 = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
img31 = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

imgStack = stackImages([[img1, img2, img3], [img21, img22, img23], [img31, img32, img33]], scale=0.2)

cv2.imshow("title", imgStack)
cv2.waitKey(0)
