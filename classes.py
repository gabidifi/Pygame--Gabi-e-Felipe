import pygame
from pygame.sprite import _Group
import os

#IMAGENS
jogador_img =  pygame.image.load(os.path.join("obstaculo.png"))

class Player(pygame.sprite.Sprite):
    x = 900
    y = 200
    def __init__(self,imgs):
        self.jogador_img1 = jogador_img
        self.rect = pygame.Rect(self.x , self.y , 50, 50)
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self,evento):
        velo_jogadorx = 0
        velo_oponentex = 0
        velo_jogadory = 0
        velo_oponentey = 0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                velo_jogadory += 6
            if evento.key == pygame.K_UP:
                velo_jogadory -= 6
            if evento.key == pygame.K_RIGHT:
                velo_jogadorx += 6
            if evento.key == pygame.K_LEFT:
                velo_jogadorx -= 6
            if evento.key == pygame.K_s:
                velo_oponentey += 6
            if evento.key == pygame.K_w:
                velo_oponentey -= 6
            if evento.key == pygame.K_d:
                velo_oponentex += 6
            if evento.key == pygame.K_a:
                velo_oponentex -= 6

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_DOWN:
                velo_jogadory -= 6
            if evento.key == pygame.K_UP:
                velo_jogadory += 6
            if evento.key == pygame.K_RIGHT:
                velo_jogadorx -= 6
            if evento.key == pygame.K_LEFT:
                velo_jogadorx += 6
            if evento.key == pygame.K_s:
                velo_oponentey -= 6
            if evento.key == pygame.K_w:
                velo_oponentey += 6
            if evento.key == pygame.K_d:
                velo_oponentex -= 6
            if evento.key == pygame.K_a:
                velo_oponentex += 6

class Oponente(pygame.sprite.Sprite):
    x = 200
    y = 200
    def __init__(self,imgs):