# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:41:02 2020

@author: Swathi
"""

import pygame
 
def run_game():
    # screen and game parameters
    screen_width, screen_height = 800, 600
 
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode( (screen_width, screen_height), 0, 32)
 
run_game()