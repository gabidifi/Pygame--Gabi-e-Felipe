import pygame

pygame.init()
tempo = pygame.time.Clock()

# Configuração da tela
tela_largura = 900
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Pong")

# Configuração dos objetos
jogador = pygame.Rect(tela_largura - 20, tela_altura / 2 - 70, 10, 140)
oponente = pygame.Rect(10, tela_altura / 2 - 70, 10, 140)
bola = pygame.Rect(tela_largura / 2 - 15, tela_altura / 2 - 15, 30, 30)

# Configuração da velocidade da bola
velo_bola_em_y = 10
velo_bola_em_x = 10

# Configuração das cores
cor_para_tras = pygame.Color('grey12')
cor_cinza = (200, 200, 200)

# Desenho dos objetos na tela
tela.fill(cor_para_tras)
pygame.draw.rect(tela, cor_cinza, jogador)
pygame.draw.rect(tela, cor_cinza, bola)
pygame.draw.rect(tela, cor_cinza, oponente)
pygame.draw.aaline(tela, cor_cinza, (tela_largura / 2, 0), (tela_largura / 2, tela_altura))

# Configuração da posição inicial da bola
x = tela_largura / 2 - 15
y = tela_altura / 2 - 15
descendo = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    bola = pygame.Rect(x, y, 30, 30)
    pygame.draw.rect(tela, cor_cinza, bola)

    if descendo:
        x += 1
        y += 1
    else:
        x -= 1
        y -= 1

    if x > 900 or y > 600:
        descendo = False
    if x < 0 or y < 0:
        descendo = True

    pygame.display.update()
