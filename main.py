import pygame
import buttons
import sys
import os
from get_words import liten
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

def ai_func(data, stop_event):
    while not stop_event.is_set():
        text = liten()
        if text:
            data.put(text)
stop_event = threading.Event()
message_queue = queue.Queue()
nn_thread = threading.Thread(target=ai_func, args=(message_queue, stop_event),daemon=True)
nn_thread.start()

pygame.init()

scr=pygame.display.set_mode(pyautogui.size(),flags=pygame.NOFRAME)

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                       hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(1, 2, 3), 0, win32con.LWA_COLORKEY)

pygame.font.init()
f2 = pygame.font.Font(None, 32)
time=pygame.time.Clock()
scene=1
move=False
run=True


button_quit=buttons.Button(2,101,32,'выйти')
button_move=buttons.Button(2,5,32,'догонялки')
button_help=buttons.Button(2,37,32,'помощь')
button_back=buttons.Button(2,69,32,'назад')
pl=player.player(300,300,2,scr)

try:
    while run:
        time.tick(60)

        for i in pygame.event.get():
            if i.type==pygame.MOUSEBUTTONDOWN:
                if i.button==1:
                    if scene==1:
                        scene=-1
                        pygame.display.set_mode((130,130),flags=pygame.NOFRAME)
                    else:
                        scr.fill((0,0,0))
                        if button_quit.rect.collidepoint(pygame.mouse.get_pos()):
                            run=False
                        if button_move.rect.collidepoint(pygame.mouse.get_pos()):
                            move=not move
                            scene=1
                            pygame.display.set_mode(pyautogui.size(),flags=pygame.NOFRAME)
                        if button_help.rect.collidepoint(pygame.mouse.get_pos()):
                            os.startfile('help.html')
                        if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                            scene=1
                            pygame.display.set_mode(pyautogui.size(),flags=pygame.NOFRAME)

        if scene==1:

            keys=pygame.key.get_pressed()
            if not move:
                if keys[pygame.K_RIGHT]:
                    pl.change_pos(pl.position[0]+pl.speed,pl.position[1])
                    pl.change_fon('right')
                if keys[pygame.K_LEFT]:
                    pl.change_pos(pl.position[0]-pl.speed,pl.position[1])
                    pl.change_fon('left')
                if keys[pygame.K_DOWN]:
                    pl.change_pos(pl.position[0],pl.position[1]+pl.speed)
                if keys[pygame.K_UP]:
                    pl.change_pos(pl.position[0],pl.position[1]-pl.speed)

            answer=pl.draw(message_queue)
            if answer:
                print(answer)

            if move:
                #x
                if pl.position[0]>mouse.get_position()[0]-pl.fon.size[0]/2+5:
                    pl.change_pos(pl.position[0]-pl.speed,pl.position[1])
                    pl.change_fon('left')
                elif pl.position[0]<mouse.get_position()[0]-pl.fon.size[0]/2-5:
                    pl.change_pos(pl.position[0]+pl.speed,pl.position[1])
                    pl.change_fon('right')

                #y
                if pl.position[1]>mouse.get_position()[1]-pl.fon.size[1]/2+5:
                    pl.change_pos(pl.position[0],pl.position[1]-pl.speed)
                elif pl.position[1]<mouse.get_position()[1]-pl.fon.size[1]/2-5:
                    pl.change_pos(pl.position[0],pl.position[1]+pl.speed)

        else:
            button_back.render(scr)
            button_quit.render(scr)
            button_help.render(scr)
            button_move.render(scr)

        pygame.display.update()

finally:
    stop_event.set()
    nn_thread.join(timeout=0.1)
    pygame.quit()