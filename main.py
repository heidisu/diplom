import generated
import pdf
import os
import argparse

IMG_WIDTH = 1020
IMG_HEIGHT = 680

class ImageInfo:
    def __init__(self, path, width, height):
        self.path = path
        self.width = width
        self.height = height


def get_out_path(text, out_folder, ending):
    filename = text.replace(' ', '_')
    return os.path.join(out_folder, f"{filename}.{ending}")

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', required=True)
    parser.add_argument('-title', default="Kursbevis")
    parser.add_argument('-subtitle', default="tildeles")
    parser.add_argument('-text', required=True)
    parser.add_argument('-out_folder', default="out")
    return parser

def main(name, title, subtitle, text, out_folder):
    image_info = ImageInfo(get_out_path(name, out_folder, "png"), IMG_WIDTH, IMG_HEIGHT)
    generated.generate_from_text(image_info, name)
    pdf.create_certificate(name, title, subtitle, text, image_info, get_out_path(name, out_folder, "pdf"))

if __name__ == "__main__":
    args = arg_parser().parse_args()
    main(args.name, args.title, args.subtitle, args.text.replace('\\n', '\n'), args.out_folder)
