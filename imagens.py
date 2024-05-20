import pygame
import os

pygame.init()

#IMAGENS UTILIZADAS NO JOGO
obstaculos = pygame.image.load(os.path.join("obstaculo.png")).convert_alpha()
disco1 = pygame.image.load(os.path.join("1.png")).convert_alpha()
disco2 = pygame.image.load(os.path.join("2.png")).convert_alpha()
campo = pygame.image.load(os.path.join("cam.png")).convert_alpha()
