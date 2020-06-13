from PIL import Image, ImageDraw
import random

BACKGROUND_COLOR = (R, G, B) = (7, 236, 235)
ALPHABET = 'abcdefghijklmnopqrstuvwxyzæøå'

def generate_random(width, height):
    img = Image.new('RGB', (width, height), color='#0000FF')
    draw_img = ImageDraw.Draw(img)

    rows = int(2 ** random.randint(2, 4))
    row_height = int(height / (rows + 4))
    startX = int(-row_height * 0.75)
    startY = int(height/2 - rows/2 * row_height)
    endX = int(width + row_height)
    endY = int(height/2 + rows/2 * row_height)

    for x in range(startX, endX, row_height):
        for y in range(startY, endY, row_height):
            thickness = int(2 ** random.randint(1, 3))
            uth1 = int(row_height / thickness)
            uth2 = int(row_height + uth1)
            if random.randint(0, 1) > 0.5:
                draw_img.polygon([(x, y), (x + row_height, y + row_height), (x + uth2, y + row_height), (x + uth1, y)], fill='#000000')
            else:
                draw_img.polygon([(x, y + row_height), (x + row_height, y), (x + uth2, y), (x + uth1, y + row_height)], fill='#FFFFFF')
    return img


class TextIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.numbers = []
        for c in self.text:
            self.numbers.append(ord(c))

    def next(self):
        number = self.numbers[self.index]
        self.index += 1
        if self.index >= len(self.numbers):
            self.index = 0
        return number

def int_avg(x, y=0):
    return int((x + y)/2)

def interpolate(c1, c2, percent):
    return int(c1 + percent * (c2 - c1))

def get_background_color(char):
    percent = ALPHABET.find(char.lower())/(len(ALPHABET) - 1)
    (r1, g1, b1) = 	(7,239,235)
    (r2, g2, b2) = 	(102,68,175)
    return (
        interpolate(r1, r2, percent), 
        interpolate(g1, g2, percent), 
        interpolate(b1, b2, percent))

def generate_from_text(image_info, text):
    color_iter = TextIterator(text)
    size_iter = TextIterator(text)
    img = Image.new(
        'RGB', 
        (image_info.width, image_info.height), 
        color=get_background_color(text[0]))
    draw_img = ImageDraw.Draw(img)
    size = size_iter.next() % 3 + 2
    rows = int(2 ** size)
    row_height = int(image_info.height / (rows + 4))
    startX = int(-row_height * 0.75)
    startY = int(image_info.height/2 - rows/2 * row_height)
    endX = int(image_info.width + row_height)
    endY = int(image_info.height/2 + rows/2 * row_height)

    for x in range(startX, endX, row_height):
        for y in range(startY, endY, row_height):
            size = size_iter.next() % 3 + 1
            thickness = int(2 ** size)
            uth1 = int(row_height / thickness)
            uth2 = int(row_height + uth1)
            if color_iter.next() % 2 == 1:
                draw_img.polygon([
                    (x, y), 
                    (x + row_height, y + row_height), 
                    (x + uth2, y + row_height), 
                    (x + uth1, y)], 
                    fill=(int_avg(color_iter.next()), int_avg(color_iter.next()), int_avg(color_iter.next())))
            else:
                draw_img.polygon([
                    (x, y + row_height), 
                    (x + row_height, y), 
                    (x + uth2, y), 
                    (x + uth1, y + row_height)], 
                    fill=(int_avg(color_iter.next(), 255), int_avg(color_iter.next(), 255), int_avg(color_iter.next(), 255)))
    img.save(image_info.path, "PNG")
    


