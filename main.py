import pygame
import buttons
import sys
import os
from ai import liten
import time
import threading
import mouse
import queue
import win32api
import win32con
import win32gui
from pygame._sdl2 import Window
import pyautogui
import player

print(pyautogui.size())

def ai_func(data):
    while True:
        text=liten()
        if text:
            data.put(text)
message_queue = queue.Queue()
nn_thread = threading.Thread(target=ai_func, args=(message_queue,))
nn_thread.daemon = True  # Завершаем поток при закрытии основного потока
nn_thread.start()

pygame.init()

scr=pygame.display.set_mode((90,100),flags=pygame.NOFRAME)

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                       hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(1, 0, 0), 0, win32con.LWA_COLORKEY)

pygame.font.init()
f2 = pygame.font.Font(None, 32)
time=pygame.time.Clock()
scene=1
move=False
run=True


button_quit=buttons.Button(0,96,32,'выйти')
button_move=buttons.Button(0,0,32,'догонялки')
button_help=buttons.Button(0,32,32,'помощь')
button_back=buttons.Button(0,64,32,'назад')
pl=player.player(300,300,1,scr)

while run:

    for i in pygame.event.get():
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                if scene==1:
                    scene=-1
                    pygame.display.set_mode((150,120),flags=pygame.NOFRAME)
                else:
                    scr.fill((0,0,0))
                    if button_quit.rect.collidepoint(pygame.mouse.get_pos()):
                        run=False
                    if button_move.rect.collidepoint(pygame.mouse.get_pos()):
                        if move:
                            move=False
                            scene=1
                            pygame.display.set_mode((90,100),flags=pygame.NOFRAME)
                        else:
                            move=True
                            scene=1
                            pygame.display.set_mode((90,100),flags=pygame.NOFRAME)
                    if button_help.rect.collidepoint(pygame.mouse.get_pos()):
                        os.startfile('help.html')
                    if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                        scene=1
                        pygame.display.set_mode((90,100),flags=pygame.NOFRAME)

    if scene==1:

        keys=pygame.key.get_pressed()
        if not move:
            if keys[pygame.K_RIGHT]:
                pl.change_pos(pl.win.position[0]+1,pl.win.position[1])
                pl.change_fon('right')
            if keys[pygame.K_LEFT]:
                pl.change_pos(pl.win.position[0]-1,pl.win.position[1])
                pl.change_fon('left')
            if keys[pygame.K_DOWN]:
                pl.change_pos(pl.win.position[0],pl.win.position[1]+1)
            if keys[pygame.K_UP]:
                pl.change_pos(pl.win.position[0],pl.win.position[1]-1)

        pl.draw(message_queue)

        if move:
            #x
            if pl.win.position[0]>mouse.get_position()[0]-pl.fon.size[0]/2+5:
                pl.change_pos(pl.win.position[0]-pl.speed,pl.win.position[1])
                pl.change_fon('left')
            elif pl.win.position[0]<mouse.get_position()[0]-pl.fon.size[0]/2-5:
                pl.change_pos(pl.win.position[0]+1,pl.win.position[1])
                pl.change_fon('right')

            #y
            if pl.win.position[1]>mouse.get_position()[1]-pl.fon.size[1]/2+5:
                pl.change_pos(pl.win.position[0],pl.win.position[1]-pl.speed)
            elif pl.win.position[1]<mouse.get_position()[1]-pl.fon.size[1]/2-5:
                pl.change_pos(pl.win.position[0],pl.win.position[1]+pl.speed)
    
    else:
        button_back.render(scr)
        button_quit.render(scr)
        button_help.render(scr)
        button_move.render(scr)

    pygame.display.update()

pygame.quit()