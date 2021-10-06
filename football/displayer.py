#!/usr/bin/python

from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

class DisplayText:

    def __init__(self):
        self.inky_display = auto()
        self.inky_display.set_border(self.inky_display.WHITE)
        self.img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype(FredokaOne, 16)

    def create_drawing(self, message):
        h = 12

        for line in message:
            w = self.font.getsize(line)[0]
            #x = (self.inky_display.WIDTH / 2) - (w / 2)
            x = 10
            y = h
            h += 31
            self.draw.text((x,y), line, self.inky_display.BLACK, self.font)

        logo = "PiBall"
        self.draw.text((160 ,43), logo, self.inky_display.RED, self.font)

    def display(self, message):
        self.create_drawing(message)
        self.inky_display.set_image(self.img)
        self.inky_display.show()

#new = DisplayText()

#new.display(["Manchester United: 2", "45 mins", "Tottenham Hotspur: 1"])
