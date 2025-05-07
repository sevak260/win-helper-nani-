import pygame
from pygame._sdl2 import Window

class Button:
    def __init__(self,x,y,size,text,color=(200,200,200)):
        self.font = pygame.font.Font(None, size)
        self.text=self.font.render(text,True,color)
        self.rect=self.text.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vin=Window
    def render(self,screen):
        screen.blit(self.text,self.rect)