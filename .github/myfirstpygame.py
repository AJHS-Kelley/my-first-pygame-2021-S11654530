# my first pygame< Ronald Durham, 11/29/21 1:58pm, v0.1

import pygame, sys 
from pygame locals import *

# star pygame 
pygame.init()

#setup our window . 1
windowsurface = pygame.display.set_mode((500, 400),0,32)
pygame.disply.set_caption('hello, world!')

# Setup colors 
Black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
Blue = (0,0,255)