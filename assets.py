import pygame
import os
import configu 
 
BOLA = 'bola'


def load_assets():
    assets = {}
    assets[BOLA] = pygame.image.load(os.path.join(IMG_DIR, 'bola.png')).convert_alpha()
    
    
    