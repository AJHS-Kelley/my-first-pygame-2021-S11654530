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

# draw lines on the screen.
pygame.draw.line(windowsurface, red (60,60), (120,60), 4)

# Draw lines on the screen 
pygame.draw.line(windowsurface, RED, (60,60), (120,60), 4)
pygame.draw.line(windowsurface, WHITE (75,60), (60,75), 2)
pygame.draw.line(windowsurface, BLUE (0,150),(150,0), 1)

# Draw the circle.
pygame.Draw.circle(windowsurface, Black, (300,50),20,0)

# Draw an ellipise
pygame.draw.rect(windowsurface, RED, (textRect.left - 20,))

# Draw the text rectangle.
pygame




# Draw the text onto the surface.
windowsurface.blit(text, textRect)

#update pygame display
pygame.display.update()

# Run game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()