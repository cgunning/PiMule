#!/usr/bin/python3

import sys
import pygame
from pygame.locals import *
import subprocess
import os
from scroll_menu import Menu
import pygame.mixer
from conf import Config
from player import Player

if not pygame.font.get_init():
    pygame.font.init()
        
def exit(menu):
    menu.destroy()
    pygame.display.quit()
    sys.exit()
    
if __name__ == "__main__":
    conf = Config()
    player = Player()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #0,6671875 and 0,(6) of HD resoultion
    
    menu = Menu(conf, player)
    menu.set_dir(conf.get_conf_for_label('root')['dir'])
    menu.render(screen, full_update = True)
    
    
    pygame.key.set_repeat(199,69)#(delay,interval)
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # What action should we do?
                if event.key == K_UP:
                    menu.move_selection(-1)
                    menu.render(screen)
                if event.key == K_DOWN:
                    menu.move_selection(1)
                    menu.render(screen)
                if event.key == K_RETURN:
                    #menu = 
                    selected_menu_item = menu.menu_items[menu.selected_menu_item]
                    if selected_menu_item.action.action_type == 'navigate':
                        menu.set_dir(menu.menu_items[menu.selected_menu_item].action.action)
                        menu.render(screen, full_update = True)
                    elif selected_menu_item.action.action_type == 'execute':
                        player.pause()
                        pygame.display.quit()
                        proc = subprocess.Popen(selected_menu_item.action.action)
                        proc.wait()
                        player.resume()
                        pygame.display.init()
                        pygame.mouse.set_visible(False)
                        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #0,6671875 and 0,(6) of HD resoultion
                        menu.render(screen, full_update = True)
                if event.key == K_ESCAPE:
                    exit(menu)
            elif event.type == QUIT:
                exit(menu)
        pygame.time.wait(8)
       
