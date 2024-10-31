import pygame as pg
import random
import math
import globals as gb
from boid import Boid

class Universe:
    def __init__(self):
        self.boids = [Boid() for _ in range(gb.NUMBER_OF_POINTS)]

    def update(self):
        for boid in self.boids:
            boid.update_position(self.boids)

    def draw(self, screen):
        for boid in self.boids:
            boid.draw(screen)