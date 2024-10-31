import globals  as gb
import pygame   as pg

class Canvas():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((gb.WIDTH, gb.HEIGHT))
        pg.display.set_caption("Polygon Animation - Vinícius Hallmann")
        self.clock = pg.time.Clock()

    def clear(self):
        self.screen.fill(gb.BACKGROUND_COLOR)

    def update(self):
        pg.display.flip()
        self.clock.tick(gb.FPS)
