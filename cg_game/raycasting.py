import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game):
        self.game = game

    def ray_cast(self):
        size = TILE_WIDTH
        x,y = self.game.player.pos
        angle = self.game.player.angle
        startAng = angle - HALF_FOV
        while startAng<angle + HALF_FOV:
            pg.draw.line(self.game.screen,'red',(x*size,y*size),(x*size + WIDTH * math.cos(startAng),y*size + WIDTH * math.sin(startAng)))
            startAng += DELTA_ANGLE


    def update(self):
        self.ray_cast()