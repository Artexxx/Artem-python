""" combining_photos.py - полкартинку, состаящию из склеенных фоток, одинакового размера """
import cv2
import numpy as np
from typing import List, TypeVar

Img = TypeVar('Image')


def normalize_images(matrix_images: List[List[Img]], start_img: Img, scale=0.5):
    """
    Приводит все фотографии в матрице `matrix_images` к размеру `start_img`.
    """
    for x, row in enumerate(matrix_images):
        for y, img in enumerate(row):
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            if img.shape[:2] == start_img.shape[:2]:
                matrix_images[x][y] = cv2.resize(img, (0, 0), fx=scale, fy=scale)
            else:
                matrix_images[x][y] = cv2.resize(img, (start_img.shape[1], start_img.shape[0]), fx=scale, fy=scale)
    return matrix_images


def stack_images(matrix_images: List[List[Img]], scale=0.5):
    """
    matrix_images: прямоугольная матрица картинок.
    scale: во сколько раз уменьшится каждая картинка.
    start_img: картинка к которой будут приведены остальные картинки в `matrix_images`
    :return: склееные картинки из `matrix_images`
    """
    start_img = matrix_images[0][0]
    matrix_images = normalize_images(matrix_images, start_img, scale)

    rows = len(matrix_images)
    blank_image = np.zeros(start_img.shape, np.uint8)
    result_img = [blank_image] * rows
    for x in range(0, rows):
        result_img[x] = np.hstack(matrix_images[x])
    return np.vstack(result_img)


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

result = stack_images([[img1, img2, img3], [img21, img22, img23], [img31, img32, img33]], scale=0.2)

cv2.imshow("Title", result)
cv2.waitKey(0)
