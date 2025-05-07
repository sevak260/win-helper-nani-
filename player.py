import pygame

class player:
    def __init__(self,x,y,speed,display):
        self.scr=display
        self.f = pygame.font.Font(None, 25)
        self.text = self.f.render('lll', True, (80, 80, 80))
        self.right = pygame.image.load('res\\right.png')
        self.right = pygame.transform.scale(self.right, (90, 90))
        self.left = pygame.transform.flip(self.right,True,False)
        self.left = pygame.transform.scale(self.left, (90, 90))
        self.position=(200,200)
        self.fon=self.left
        self.speed=speed
    def change_text(self,text):
        self.text = self.f.render(text, True, (80, 80, 80))
    def change_pos(self,x,y):
        self.position=(x,y)
    def change_fon(self,turn):
        if turn=='right':
            self.fon=self.right
        elif turn=='left':
            self.fon=self.left
        else:
            print(end='')
    def draw(self,message):
        self.scr.fill((1, 2, 3))
        self.scr.blit(self.fon,self.position)
        try:
            data=message.get(timeout=0.0)
            data = str(data).replace("\n\n","\n")
            self.change_text(data)
            return data
        except:
            pass
        self.scr.blit(self.text,(90,0))