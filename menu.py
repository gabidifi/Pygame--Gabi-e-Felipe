import pygame


WIDTH = 1200 #altura
HEIGHT = 600 #largura


def inicia(janela,primeira,segunda): #FUNCAO PARA INICIALIZAR O JOGO COM A TELA DE INICIO
    img1 = True
    fim = False
    escolha = 0
    while not fim:
        pygame.display.update()
        pygame.time.wait(600)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                #fecha janela quando o X é pressionado
                fim = True
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    escolha = 1 # ESCOLHA DO MODO CONTRA O ROBO
                if evento.key == pygame.K_2:
                    escolha = 2 # ESCOLHA DO MODO CONTRA OUTRO PLAYER
                fim = True

        if img1 == False:
            img1 = True
            janela.blit(primeira, (0,0))

        else:
            img1 = False
            janela.blit(segunda, (0,0))
        # ESTE IF E ELSE SERVEM PARA FICAR PISCANDO PARA DAR UMA SENSACAO DE MOVIMENTO
    return escolha #RETORNA A ESCOLHA QUE O USUARIO FEZ

