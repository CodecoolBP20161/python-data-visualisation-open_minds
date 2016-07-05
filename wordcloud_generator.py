
from PIL import Image, ImageDraw, ImageFont
import math
import os
import random
import uuid


class Wordcloud():
    FONT = '/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf'
    FONT_SIZE = [15, 18, 20, 22, 24, 27, 30, 35, 40, 45]
    FONT_COLOR = ''  # from database, based on main_color
    WORDLIST = []

    def __init__(self, width=640, height=640):
        self.width = width
        self.height = height
        self.words_to_draw = {}  # 'text': text, 'fontsize': fontsize,
        # 'x': x, 'y': y, 'w': width, 'h': height, 'color': self.FONT_COLOR
        self.image = Image.new('RGBA', [width, height], "#fff")

    def get_color(self):
        # from database
        pass

    def set_size(self):
        # based on the order, of WORDLIST
        pass

    def set_coordinates(self):
        # inside out, from largest to smallest, based on length and size
        pass

    def check_overlap(self):
        # check whether a word overlaps with another
        pass

    def check_isinside(self):
        # checks whether a word is partly outside of the image
        pass

    def save(cls):
        img.save('sample-out.png')
