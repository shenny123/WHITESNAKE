import random
import pygame

class Apple:
    def __init__(self, image, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randrange(30, screen_width - 30,30)
        self.y = random.randrange(30, screen_height - 30,30)
        self.image = image
        self.pos = image.get_rect().move(self.x, self.y)
    def respawn(self):
        self.pos.topleft = (random.randrange(30, self.screen_width - 30,30), random.randrange(30, self.screen_height - 30,30))
        print(self.pos)

class Head:
    def __init__(self, image, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = image
        self.pos = image.get_rect().move(300,210)
        self.dx = 0
        self.dy = 0
    def move(self):
        self.pos = self.pos.move(self.dx, self.dy)
    def up(self):
        self.dy = -30
        self.dx = 0
    def down(self):
        self.dy = 30
        self.dx = 0
    def left(self):
        self.dy = 0
        self.dx = -30
    def right(self):
        self.dy = 0
        self.dx = 30
class Body:
    def __init__(self, image, x, y):
        self.image = image
        self.pos = image.get_rect().move(x, y)
        self.dx = 0
        self.dy = 0
        self.nextdx = 0
        self.nextdy = 0
    def move(self):
        self.pos = self.pos.move(self.dx, self.dy)