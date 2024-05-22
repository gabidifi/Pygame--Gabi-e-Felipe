import pygame
from menu import inicia
from funcao_jogo import game
from config_geral import tela, img1, img2, menu_som , jogador

pygame.init()

# tempo de score 
tempo_score = None 

#Inicializa o jogo com menu 

pygame.mixer.music.set_volume(0)
menu_som.play() #PLAY NA MUSICA DE INICIO
escolha = inicia(tela,img1,img2)
pause = False

game(escolha,jogador) #COMECA O JOGO COM AS FUNCOES CRIADAS ANTERIORMENTE