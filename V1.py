# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from time import sleep
pygame.init()

# ----- Gera tela principal
tela_largura = 900
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Pong")

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
ball = pygame.image.load('bola.png')  

# Configuração dos objetos
jogador = pygame.Rect(tela_largura - 20, tela_altura / 2 - 70, 10, 140)
oponente = pygame.Rect(10, tela_altura / 2 - 70, 10, 140)

# Configuração da velocidade da bola
velo_bola_em_y = 10
velo_bola_em_x = 10

# Configuração das cores
cor_para_tras = pygame.Color('grey12')
cor_cinza = (200, 200, 200)

# Configuração da posição inicial da bola
x = tela_largura / 2 - 15
y = tela_altura / 2 - 15
descendo = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    tela.fill(cor_para_tras)
    tela.blit(ball, (x, y))
    pygame.draw.rect(tela, cor_cinza, jogador)
    pygame.draw.rect(tela, cor_cinza, oponente)
    pygame.draw.aaline(tela, cor_cinza, (tela_largura / 2, 0), (tela_largura / 2, tela_altura))
    sleep(0.005)
    if descendo:
        x = x + 1 
        y = y + 1 
    else: 
        x = x - 1
        y = y - 1

    if x > tela_largura or y > tela_altura:
        descendo = False
    if x < 0 or y < 0:
        descendo = True

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

