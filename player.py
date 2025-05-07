import pygame
from pygame._sdl2 import Window

class player:
    def __init__(self,x,y,speed,display):
        self.scr=display
        self.f1 = pygame.font.Font(None, 25)
        self.text1 = self.f1.render('lll', True, (180, 180, 180))
        self.right = pygame.image.load('res\\right.png')
        self.right = pygame.transform.scale(self.right, (90, 90))
        self.left = pygame.transform.flip(self.right,True,False)
        self.left = pygame.transform.scale(self.left, (90, 90))
        self.fon=self.left
        self.win = Window.from_display_module()
        self.speed=speed
    def change_text(self,text):
        self.text1 = self.f1.render(text, True, (180, 180, 180))
    def change_pos(self,x,y):
        self.win.position=x,y
    def change_fon(self,turn):
        if turn=='right':
            self.fon=self.right
        elif turn=='left':
            self.fon=self.left
        else:
            print('rerrror')
    def draw(self,message):
        self.scr.fill((1, 0, 0))
        self.scr.blit(self.fon,(0,0))
        try:
            data=message.get(timeout=0.01)
            data = str(data).replace("\n\n","\n")
            self.change_text(data)
            return data
        except:
            pass
        self.scr.blit(self.text1,(90,0))