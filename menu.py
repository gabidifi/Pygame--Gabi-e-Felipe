import pygame

WIDTH = 1200 #altura
HEIGHT = 600 #largura


def inicia(janela,primeira,segunda): 
    img1 = True
    m = True
    state = False
    while m != state:
        pygame.display.update()
        pygame.time.wait(600)

        if m == True:
            

            if img1 == False:
                img1 = True
                janela.blit(primeira, (0,0))

            else:
                img1 = False
                janela.blit(segunda, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #fecha janela
                pygame.quit()
                break
            elif event.type == pygame.KEYDOWN:   #Se apertar uma tecla vai patra um while e se for outra vai para o outro
                    m = not m
        
