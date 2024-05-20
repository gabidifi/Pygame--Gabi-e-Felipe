import pygame
from menu import *
from config_geral import *

def gameover(janela, over1,over2):
    primeiro_over = True 
    game_over = True
    while game_over != False:
        pygame.display.update()
        pygame.time.wait(600)
       
        if game_over == True:
                
            if primeiro_over == True:
                primeiro_over = False
                janela.blit(over2, (0,0))
            else:
                primeiro_over = True
                janela.blit(over1, (0,0))
            #ESTE IF E ELSE SERVEM PARA FICAR PISCANDO NA TELA, DANDO UMA SENSACAO DE MOVIMENTO

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
              
                pygame.quit()
                break
                #SE USUARIO QUISER SAIR APENAS APERTAR NO X NORMAL
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.quit() # COMO PODEMOS SAIR APERTANDO O X TAMBEM PODE COM A TECLA S
                    break
                if event.key == pygame.K_c: # SE O USUARIO PRESSIONAR "C" O JOGO REINICIA PARA A TELA INICIAL
                    pygame.mixer.music.set_volume(0)
                    menu_som.play()
                    escolha = inicia(tela,img1,img2) #NOVAMENTE O USUARIO NA TELA INICIAL PARA ESCOLHER QUAL MODO JOGAR
                    pause = False
                    return
 
                    
                    