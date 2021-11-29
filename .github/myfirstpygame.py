# my first pygame< Ronald Durham, 11/29/21 1:58pm, v0.3

import pygame, sys 
from pygame locals import *

# start pygame 
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

# setup font .
basicfont = pygame.font.sysfont(none, 48)

# Setup text.
text = basicfont.render('hello, world!', true, White =, Blue)
textrect = text.get_rect()
textRect.centerx= windowsurface.get_rect().centerx
textRect.centerx= windowsurface.get_rect().centery

# fill background color.
windowsurface.fill(white)

# Draw a polygon onto the screen
pygame.draw.polygon(windowsurface, Green, ((146,0) , (291,106), (236,277), (56,277),