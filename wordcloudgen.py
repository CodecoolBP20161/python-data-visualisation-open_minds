from PIL import Image, ImageDraw, ImageFont
import math
from main import *


class WordCloud(object):

    FONT = '/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf'
    FONT_COLOR = ['#F2B701', '#E57D04', '#DC0030', '#B10058', '#7C378A',
                  '#3465AA', '#09A275', '#85BC5F', '#39d', '#aab5f0'
                  ]
    FONT_SIZE = [25, 28, 30, 32, 34, 37, 40, 45, 50, 55]

    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.wordlist = None
        self.image = Image.new('RGBA', [width, height], "#123")
        self.image_draw = ImageDraw.Draw(self.image)

    def draw(self, words):
        self.words = words
        num = random.randint(0, 7)
        image_file_path = 'cloud_image' + '.jpg'
        self.image_file_path = image_file_path

        index = 0
        length = len(self.words)
        for word in self.words:
            if index == length - 1:
                weight = 0
            else:
                weight = self.rescale_weight(word['weight'], self.words[0]['weight'],
                                             self.words[-1]['weight'])
            self.find_coordinates(index, word['text'], int(weight))
            index += 1

        return self.save()

    def rescale_weight(self, n, maxinum, minimum):
        scale_min = 1
        scale_max = 10

        if maxinum == minimum:
            return 9

        weight = round((1 * (scale_max - scale_min) * (n - minimum)) / (maxinum-minimum))

        return weight

    def find_coordinates(self, index, text, weight):
        angle_step = 0.57
        radius_step = 8
        radius = 25
        angle = random.uniform(0.2, 6.28)

        fontsize = self.FONT_SIZE[weight]
        width, height = self.image_draw.textsize(text, font=ImageFont.truetype(self.FONT, fontsize))

        x = self.width/2 - width/2.0
        y = self.height/2 - height/2.0

        count = 1
        while self._check_overlap(x, y, height, width):
            if count % 8 == 0:
                radius += radius_step
            count += 1

            if index % 2 == 0:
                angle += angle_step
            else:
                angle += -angle_step

            x = self.width/2 - (width / 2.0) + (radius*math.cos(angle))
            y = self.height/2 + radius*math.sin(angle) - (height / 2.0)

        self.wordlist.append({'text': text, 'fontsize': fontsize,
                              'x': x, 'y': y, 'w': width, 'h': height,
                              'color': self.FONT_COLOR[weight]
                              })

    def _check_overlap(self, x, y, h, w):
        if not self.wordlist:
            self.wordlist = []
            return False

        for word in self.wordlist:
            if not ((x+w < word['x']) or (word['x'] + word['w'] < x) or
                    (y + h < word['y']) or (word['y'] + word['h'] < y)):
                return True

        return False

    def save(self):
        for word in self.wordlist:
            if self._lies_inside(word):
                self.image_draw.text((word['x'], word['y']), word['text'],
                                     font=ImageFont.truetype(self.FONT,
                                     word['fontsize']), fill=word['color']
                                     )

        self.image.save(self.image_file_path, "JPEG", quality=90)
        return self.image_file_path

    def _lies_inside(self, word):

        if word['x'] >= 0 and word['x'] + word['w'] <= self.width and\
         word['y'] >= 0 and word['y'] + word['h'] <= self.height:
            return True

        return False


if __name__ == '__main__':
    t = WordCloud()
    words = []
    temp = {}

    for element in first_list:
        temp["text"] = element[0]
        temp["weight"] = element[1]
        words.append(dict(temp))

    print(t.draw(words))
