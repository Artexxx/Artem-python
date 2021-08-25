import glob
import os.path as path
import shutil
from PIL import Image
from colorama import Fore, init; init(autoreset=True)


def image_path_generator(image_dir):
    for e in ('png', 'jpg', 'gif'):
        yield from glob.glob(image_dir + '\*.' + e)


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
        images = image_path_generator(img_dir)
    else:
        raise Exception('img_dir - должен быть каталогом с фото')
    if not path.isdir(out_dir):
        raise Exception('out_dir - должен быть созданным каталогом')

    for file in images:
        is_porn = check_porn(file)
        if is_porn:
            print(f'{Fore.GREEN}{file} is porn')
            shutil.move(file, out_dir)
        else:
            print(f'{Fore.RED}{file} is not porn')
