import pygame

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
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
              
                pygame.quit()
                break
       
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_over = not game_over
                if event.key == pygame.K_s:
                    pygame.quit()
                    break