from PIL import Image
import argparse
import pyprind
import glob
import os


def make_pdf(path, pdf_filename):
    extensions = ["*.jpg", "*.png"]
    image_list = []
    for extension in extensions:
        for file in glob.glob(path + extension):
            image_list.append(file)
    image_list.sort()

    try:
        title_img = Image.open(image_list[0])
        print('Find images:', *image_list[:3], '...', *image_list[-2:])
        pbar = pyprind.ProgBar(len(image_list), bar_char="♡", stream=1)
    except:
        print("\n\n\033[1;31;48m"  # Red
              "[#] An error occurred in opening the image, check the path:"
              "\n\033[1;37;0m"  # End
              "Your path: ", path)
        return 0
    im_list = []
    for image in image_list[1:]:
        im = Image.open(image)
        im_list.append(im)
        pbar.update()
    title_img.save(pdf_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)
    print("\n\nOK", pdf_filename, )


def main():
    parser = argparse.ArgumentParser(
        description="Easily convert your hentais from folders of images to one pdf file"
    )
    parser.add_argument(
        "-m",
        "--make",
        nargs=2,
        metavar=('path', 'name'),
        required=False,
        help="provide abosule or relative path to a folder with your hentai and a name you want to give for the generated pdf file"
    )
    parser.add_argument(
        "-mc",
        "--makecurrent",
        nargs=1,
        metavar='name',
        required=False,
        help="open terminal in the folder with your hentai and provide a name you want to give for the generated pdf file"
    )
    args = parser.parse_args()

    if args.makecurrent or args.make:
        if args.makecurrent:
            path = os.getcwd()
            name = args.makecurrent[0]
        elif args.make[0].startswith("/"):
            path = args.make[0]
            name = args.make[1]
        elif args.make[0].startswith("/") == False:
            path = os.getcwd() + "/" + args.make[0]
            name = args.make[1]
    else:
        parser.print_help()
        path = input('>>> Your img dir: ')
        name = input('>>> Your PDF name: ')

    if "\\" in path:
        path = path.replace("\\", "/")
    if not path.endswith("/"):
        path += "/"
    if not name.endswith(".pdf"):
        name += ".pdf"
    make_pdf(path, name)


if __name__ == "__main__":
    main()
    # make_pdf("AnimeGirl/", "output/AnimeGirl.pdf")
