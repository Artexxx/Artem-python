import os
import os.path as path
import shutil
from PIL import Image


def check_porn(file):
    img = Image.open(file).convert('YCbCr')
    w, h = img.size
    data = img.getdata()
    cnt = 0
    for i, ycbcr in enumerate(data):
        y, cb, cr = ycbcr
        if 86 <= cb <= 117 and 140 <= cr <= 168:
            cnt += 1
    return cnt > w * h * 0.1


if __name__ == '__main__':
    img_dir = input('Каталог c фото:')
    out_dir = input('Каталог перемещения:')
    if path.isdir(img_dir):
        file_list = [path.join(img_dir, file) for file in os.listdir(img_dir)]
    else:
        raise Exception('img_dir - должен быть каталогом с фото')
    if not path.isdir(out_dir):
        raise Exception('out_dir - должен быть каталогом перемещения')

    for file in file_list:
        if path.isfile(file):
            is_porn = check_porn(file)
            if is_porn:
                print(file, 'is porn')
                shutil.move(file, out_dir)
            else:
                print(file, 'is not porn')
