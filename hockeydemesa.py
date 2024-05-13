import pygame
import random
import time
from menu import *
from gameover import *

pygame.init()
tempo = pygame.time.Clock()

#musicas
menu = pygame.mixer.Sound('menu.mp3')


# Configuração da tela
tela_largura = 1000
tela_altura = 480
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("obstaculo")

# obstaculo
obs_altura = 70
obs_larguea = 70
obstaculo = pygame.image.load('obstaculo.png').convert_alpha()
obstaculo = pygame.transform.scale(obstaculo, (obs_larguea, obs_altura))
obstaculo_pos = pygame.Rect(tela_largura + 100, tela_altura / 2, obs_larguea, obs_altura) 

# Carregar a imagem de fundo
fundo = pygame.image.load('cam.png').convert()
fundo = pygame.transform.scale(fundo, (tela_largura, tela_altura))

# Configuração dos objetos
jogador = pygame.Rect(tela_largura - 20, tela_altura / 2 - 70, 10, 140)
oponente = pygame.Rect(10, tela_altura / 2 - 70, 10, 140)
bola = pygame.Rect(tela_largura / 2 - 15, tela_altura / 2 - 15, 30, 30)

# imagens menu 

imng1 = pygame.image.load('azul.png').convert_alpha()
imng1 = pygame.transform.scale(imng1, [1000,480])
img2 = pygame.image.load('branco.png').convert_alpha()
img2 = pygame.transform.scale(img2, [1000,480])

 #Configuração da velocidade da bola/ jogadores
velo_bola_em_y = 6
velo_bola_em_x = 6
velo_jogadorx = 0
velo_oponentex = 0
velo_jogadory = 0
velo_oponentey = 0
velo_obstaculo= 1

# Configuração das cores
cor_para_tras = pygame.Color('grey12')
preto = (0, 0, 0)


jogador_score = 0
oponente_score = 0
fonte = pygame.font.Font("freesansbold.ttf",28)

# tempo de score 
tempo_score = None 

#Inicializa o jogo com menu 

pygame.mixer.music.set_volume(0)
menu.play()
inicia(tela,imng1,img2)
pause = False
while True:
    for evento in pygame.event.get():

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

    # ----- Gera saídas

    # Bola
    bola.x += velo_bola_em_x
    bola.y += velo_bola_em_y

    if bola.top <= 0 or bola.bottom >= tela_altura:
        velo_bola_em_y *=-1

    if bola.left <= 0: 
        jogador_score += 1
        bola.center = (tela_largura/2,tela_altura/2)
        velo_bola_em_y *= random.choice((1,-1))
        velo_bola_em_x *= random.choice((1,-1))
       

    if bola.right >= tela_largura:
        oponente_score += 1
        bola.center = (tela_largura/2,tela_altura/2)
        velo_bola_em_y *= random.choice((1,-1))
        velo_bola_em_x *= random.choice((1,-1))

    if bola.colliderect (jogador) or bola.colliderect(oponente) or bola.colliderect(obstaculo_pos):
        velo_bola_em_x *= -1

    # obstaculo
    if jogador_score >= 1 or oponente_score >= 1:
        obstaculo_pos.y += velo_obstaculo
        if obstaculo_pos.top <= 0 or obstaculo_pos.bottom >= tela_altura:
            velo_obstaculo *= -1
            bola.center = (tela_largura/2,tela_altura/2)
            velo_obstaculo *= random.choice((1,-1))
            
    # 5 Pontos
    if jogador_score == 6 or oponente_score == 6:
        pygame.mixer.music.set_volume(0)
        menu.play()
        gameover(tela, imng1,img2)

    # Jogador
    jogador.y += velo_jogadory
    jogador.x += velo_jogadorx
    if jogador.top <= 0:
        jogador.top = 0
    if jogador.bottom >= tela_altura:
        jogador.bottom = tela_altura
    if jogador.left <= 0:
        jogador.left = 0
    if jogador.right >= tela_largura:
        jogador.right = tela_largura

    # Oponente
    oponente.y += velo_oponentey
    oponente.x += velo_oponentex
    if oponente.top <= 0:
        oponente.top = 0
    if oponente.bottom >= tela_altura:
        oponente.bottom = tela_altura
    if oponente.left <= 0:
        oponente.left = 0
    if oponente.right >= tela_largura:
        oponente.right = tela_largura

    if jogador_score == 1 or oponente_score == 1:
        obstaculo_pos.center = (tela_largura / 2, tela_altura / 2)

    # Frame
    tela.fill(cor_para_tras)
    tela.blit(fundo, (0, 0))  
    tela.blit(obstaculo, obstaculo_pos) 
    pygame.draw.rect(tela,preto,jogador)
    pygame.draw.rect(tela,preto,oponente)
    pygame.draw.ellipse(tela,preto,bola)
    

    # Placar
    jogador_texto = fonte.render(f"{jogador_score}",False,preto)
    tela.blit(jogador_texto,(530,150))
    
    oponente_texto = fonte.render(f"{oponente_score}",False,preto)
    tela.blit(oponente_texto,(450,150))

    pygame.display.flip()
    tempo.tick(60)

