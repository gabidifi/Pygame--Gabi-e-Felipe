import pygame


WIDTH = 1200 #altura
HEIGHT = 600 #largura


def inicia(janela,primeira,segunda): 
    img1 = True
    fim = False
    escolha = 0
    while not fim:
        pygame.display.update()
        pygame.time.wait(600)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                #fecha janela
                fim = True
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    escolha = 1
                if evento.key == pygame.K_2:
                    escolha = 2
                fim = True

        if img1 == False:
            img1 = True
            janela.blit(primeira, (0,0))

        else:
            img1 = False
            janela.blit(segunda, (0,0))
        
    return escolha

