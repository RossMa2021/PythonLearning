import sys
from pygame.locals import *
import pygame
from pygame.locals import*

white = (255,255,255)
black = (0,0,0)

class TextPanel(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()

    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
        pygame.display.update()
