import pygame

pygame.init()
tempo = pygame.time.Clock()

tela_largura = 900
tela_altura = 600
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption("Pong")

bola = pygame.Rect(tela_largura/2-15,tela_altura/2-15,15,15)
jogador = pygame.Rect(tela_largura - 20,tela_altura/2-70,10,140)
oponente = pygame.Rect(10,tela_altura/2-70,10,140)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    tempo.tick(60)

