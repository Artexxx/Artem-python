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
    imgdir = input('Каталог c фото:')
    dstdir = input('Каталог перемещения:')
    if path.isdir(imgdir):
        filelist = [path.join(imgdir, file) for file in os.listdir(imgdir)]
    else:
        raise Exception('imgdir - должен быть каталогом с фото')
    if not path.isdir(dstdir):
        raise Exception('dstdir - должен быть каталогом перемещения')

    for file in filelist:
        if path.isfile(file):
            is_porn = check_porn(file)
            if is_porn:
                print(file, 'is porn')
                shutil.move(file, dstdir)
            else:
                print(file, 'is not porn')
