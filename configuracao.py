import pygame

pygame.init()
tempo = pygame.time.Clock()

tela_largura = 900
tela_altura = 600
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption("Pong")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    tempo.tick(60)

