import pygame
import random
from config_geral import bola, tela_altura, tela_largura, batida, oponente, menu_som,\
    img3, img4, tela, velo_jogadorx, velo_oponente, fonte , obstaculo_pos, preto ,vermelho,\
    azul , cor_para_tras , fundo , obstaculo, tempo , velo_oponentex, velo_bola_em_x, velo_bola_em_y,\
    velo_jogadory , velo_obstaculo , velo_oponentey, jogador_score, oponente_score
    
from menu import *
from gameover import gameover


def game(escolha,jogador): 
    global velo_bola_em_y , velo_bola_em_x , velo_jogadorx ,velo_jogadory , velo_obstaculo , velo_oponentey, jogador_score , oponente_score
    #NECESSARIO COLOCAR COMO GLOBAL POIS É ALTERADO AO DECORRER DO CODIGO

    if escolha == 1: #PRIMEIRA ESCOLHA SENDO CONTRA O ROBO 
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        velo_jogadory += 6
                    if evento.key == pygame.K_UP:
                        velo_jogadory -= 6
                    

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_DOWN:
                        velo_jogadory -= 6
                    if evento.key == pygame.K_UP:
                        velo_jogadory += 6
                #ESTES A CIMA SERVEM PARA MOVIMENTAR O JOGADOR

            # ----- Gera saídas

            # Bola
            global velo_bola_em_x, velo_bola_em_y
            #GLOBAL POIS ESTAMOS ALTERANDO AO DECORRER DO JOGO
            bola.x += velo_bola_em_x
            bola.y += velo_bola_em_y

            if bola.top <= 0 or bola.bottom >= tela_altura:
                velo_bola_em_y *=-1

            if bola.left <= 0: 
                jogador_score += 1 #MAIS UM NA PONTUACAO POIS SIGNIFICA QUE PASSOU O GOL DO JOGADOR
                bola.center = (tela_largura/2,tela_altura/2) #REDIRECIONA ONDE A BOLA DEVE ESTAR APOS O GOL
                velo_bola_em_y *= random.choice((1,-1)) #A BOLA DEVE COMECAR A SE MOVIMENTAR LOGO APOS O GOL
                velo_bola_em_x *= random.choice((1,-1)) #A BOLA DEVE COMECAR A SE MOVIMENTAR LOGO APOS O GOL
            

            if bola.right >= tela_largura:
                oponente_score += 1 #MAIS UM NA PONTUACAO POIS SIGNIFICA QUE PASSOU O GOL DO ADVERSARIO
                bola.center = (tela_largura/2,tela_altura/2) #REDIRECIONA ONDE A BOLA DEVE ESTAR APOS O GOL
                velo_bola_em_y *= random.choice((1,-1)) #A BOLA DEVE COMECAR A SE MOVIMENTAR LOGO APOS O GOL
                velo_bola_em_x *= random.choice((1,-1)) #A BOLA DEVE COMECAR A SE MOVIMENTAR LOGO APOS O GOL

            if bola.colliderect (jogador) and velo_bola_em_x > 0:
                if abs(bola.right - jogador.left) < 10:
                    velo_bola_em_x *= -1 #SE HOUVER UMA COLISAO A BOLA TEM QUE PARA A OUTRA DIRECAO
                    batida.play() #O AUDIO DA BATIDA DEVE SER ATIVADO PARA TER A SENSACAO DE UMA BATIDA
                elif abs(bola.bottom - jogador.top) < 10 and velo_bola_em_y > 0:
                    velo_bola_em_y *= -1 #SE HOUVER UMA COLISAO A BOLA TEM QUE PARA A OUTRA DIRECAO
                    batida.play() #O AUDIO DA BATIDA DEVE SER ATIVADO PARA TER A SENSACAO DE UMA BATIDA
                elif abs(bola.top - jogador.bottom) < 10 and velo_bola_em_y < 0:
                    velo_bola_em_y *= -1 #SE HOUVER UMA COLISAO A BOLA TEM QUE PARA A OUTRA DIRECAO
                    batida.play() #O AUDIO DA BATIDA DEVE SER ATIVADO PARA TER A SENSACAO DE UMA BATIDA

            if bola.colliderect(oponente) and  velo_bola_em_x <  0:
                if abs(bola.left - oponente.right) < 10:
                    velo_bola_em_x *= -1 #A BATIDA O MESMO QUE O JOGADOR
                    batida.play() # MESMA RAZAO PARA TER SENSACAO DE BATIDA
                elif abs(bola.bottom - oponente.top) < 10 and velo_bola_em_y > 0:
                    velo_bola_em_y *= -1
                    batida.play()
                elif abs(bola.top - oponente.bottom) < 10 and velo_bola_em_y < 0:
                    velo_bola_em_y *= -1
                    batida.play()

                    
            # 5 Pontos
            if jogador_score == 5 or oponente_score == 5: #PONTUACAO LIMITE PARA A PARTIDA ACABAR
                pygame.mixer.music.set_volume(0)
                menu_som.play()
                gameover(tela, img3,img4) #ATIVA O MODO GAMEOVER PARA SABER SE O USUARIO GOSTARIA DE CONTINUAR OU ENCERRAR O JOGO
                jogador_score = 0 #REINICIA O PLACAR DO JOGADOR
                oponente_score = 0 #REINICIA O PLACAR DO ADVERSARIO

            # Jogador
            jogador.y += velo_jogadory
            jogador.x += velo_jogadorx
            if jogador.top <= 0:
                jogador.top = 0
            if jogador.bottom >= tela_altura: #LIMITA ATE ONDE O JOGADOR PODE SE LOCOMOVER PARA NAO ESCAPAR DA TELA
                jogador.bottom = tela_altura
            if jogador.left <= 0: #LIMITA ATE ONDE O JOGADOR PODE SE LOCOMOVER PARA NAO ESCAPAR DA TELA
                jogador.left = 0
            if jogador.right >= tela_largura: #LIMITA ATE ONDE O JOGADOR PODE SE LOCOMOVER PARA NAO ESCAPAR DA TELA
                jogador.right = tela_largura

            # Oponente
            if oponente.top < bola.y: #ONDE O ROBO DEVE SE LOCOMOVER (SEGUINDO A BOLA)
                oponente.top += velo_oponente
            if oponente.bottom > bola.y:
                oponente.bottom -= velo_oponente
            if oponente.top <= 0:
                oponente.top = 0
            if oponente.bottom >= tela_altura:
                oponente.bottom = tela_altura

            if jogador_score == 1 or oponente_score == 1:
                obstaculo_pos.center = (tela_largura / 2, tela_altura / 2) #POSICIONA O BONECO DE DECORACAO

            # Frame
            tela.fill(cor_para_tras)
            tela.blit(fundo, (0, 0))  
            tela.blit(obstaculo, obstaculo_pos) 
            pygame.draw.rect(tela,azul,jogador)
            pygame.draw.rect(tela,vermelho,oponente)
            pygame.draw.ellipse(tela,preto,bola)
            

            # Placar
            jogador_texto = fonte.render(f"{jogador_score}",False,preto)
            tela.blit(jogador_texto,(530,150)) #DESENHA O NUMERO DO PLACAR PRO JOGADOR VISUALIZAR
            
            oponente_texto = fonte.render(f"{oponente_score}",False,preto)
            tela.blit(oponente_texto,(450,150)) #DESENHA O NUMERO DO PLACAR PRO JOGADOR VISUALIZAR
             
            pygame.display.flip()
            tempo.tick(60)

    #OS TEXTOS DA ESCOLHA 2 SAO O MESMO DA 1, O QUE MUDA É A ADICAO DE UM NOVO JOGADOR AO INVES DO ROBO
    #ALGUMA NO CODIGO CONSULTAR OS TEXTOS DA ESCOLHA 1 
    elif escolha == 2: #SELECIONA A OPCAO DO MULTIPLAYER(2 JOGADORES)
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()

                if evento.type == pygame.KEYDOWN: 
                    if evento.key == pygame.K_DOWN:
                        velo_jogadory += 6
                    if evento.key == pygame.K_UP:
                        velo_jogadory -= 6
                    if evento.key == pygame.K_s:
                        velo_oponentey += 6
                    if evento.key == pygame.K_w:
                        velo_oponentey -= 6

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_DOWN:
                        velo_jogadory -= 6
                    if evento.key == pygame.K_UP:
                        velo_jogadory += 6
                    if evento.key == pygame.K_s:
                        velo_oponentey -= 6
                    if evento.key == pygame.K_w:
                        velo_oponentey += 6

            # ----- Gera saídas

            # Bola
            bola.x += velo_bola_em_x
            bola.y += velo_bola_em_y

            if bola.top <= 0 or bola.bottom >= tela_altura:
                velo_bola_em_y *=-1 #A BOLA REBATE QUANDO BATE EM CIMA OU EMBAIXO

            if bola.left <= 0: #MESMO TEXTO DO ESCOLHA == 1
                jogador_score += 1
                bola.center = (tela_largura/2,tela_altura/2)
                velo_bola_em_y *= random.choice((1,-1))
                velo_bola_em_x *= random.choice((1,-1))
            

            if bola.right >= tela_largura + 5:
                oponente_score += 1
                bola.center = (tela_largura/2,tela_altura/2)
                velo_bola_em_y *= random.choice((1,-1))
                velo_bola_em_x *= random.choice((1,-1))

            #MESMO TEXTO DA ESCOLHA == 1
            if bola.colliderect (jogador) and velo_bola_em_x > 0:
                if abs(bola.right - jogador.left) < 10:
                    velo_bola_em_x *= -1
                    batida.play()
                elif abs(bola.bottom - jogador.top) < 10 and velo_bola_em_y > 0:
                    velo_bola_em_y *= -1
                    batida.play()
                elif abs(bola.top - jogador.bottom) < 10 and velo_bola_em_y < 0:
                    velo_bola_em_y *= -1
                    batida.play()
            
            if bola.colliderect(oponente) and  velo_bola_em_x <  0:
                if abs(bola.left - oponente.right) < 10:
                    velo_bola_em_x *= -1
                    batida.play()
                elif abs(bola.bottom - oponente.top) < 10 and velo_bola_em_y > 0:
                    velo_bola_em_y *= -1
                    batida.play()
                elif abs(bola.top - oponente.bottom) < 10 and velo_bola_em_y < 0:
                    velo_bola_em_y *= -1
                    batida.play()

            # 5 Pontos para o vencendor 
            if jogador_score == 5 or oponente_score == 5:
                pygame.mixer.music.set_volume(0)
                menu_som.play()
                gameover(tela, img3,img4)
                jogador_score = 0
                oponente_score = 0


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
            #COMO AGORA TEMOS MAIS UM JOGADOR TEMOS QUE COLOCAR O METODO DE ANDAR AO INVES DE SEGUIR A BOLA
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
            pygame.draw.rect(tela,azul,jogador)
            pygame.draw.rect(tela,vermelho,oponente)
            pygame.draw.ellipse(tela,preto,bola)
            

            # Placar
            jogador_texto = fonte.render(f"{jogador_score}",False,preto)
            tela.blit(jogador_texto,(530,150))
            
            oponente_texto = fonte.render(f"{oponente_score}",False,preto)
            tela.blit(oponente_texto,(450,150))

            pygame.display.flip()
            tempo.tick(60)
