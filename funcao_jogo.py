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
    if escolha == 1: 
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

            # ----- Gera saídas

            # Bola
            global velo_bola_em_x, velo_bola_em_y
            bola.x += velo_bola_em_x
            bola.y += velo_bola_em_y

            if bola.top <= 0 or bola.bottom >= tela_altura:
                velo_bola_em_y *=-1
                # print('bola.top: ', bola.top)
                # print('bola.bottom: ', bola.bottom)
                # print('velo_bola_em_x: ', velo_bola_em_x)
                # print('velo_bola_em_y: ', velo_bola_em_y)

            if bola.left <= 0: 
                jogador_score += 1
                bola.center = (tela_largura/2,tela_altura/2)
                velo_bola_em_y *= random.choice((1,-1))
                velo_bola_em_x *= random.choice((1,-1))
            

            if bola.right >= tela_largura:
                oponente_score += 1
                bola.center = (tela_largura/2,tela_altura/2)
                velo_bola_em_y *= random.choice((1,-1))
                velo_bola_em_x *= random.choice((1,-1))

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

                    
            # 5 Pontos
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
            if oponente.top < bola.y:
                oponente.top += velo_oponente
            if oponente.bottom > bola.y:
                oponente.bottom -= velo_oponente
            if oponente.top <= 0:
                oponente.top = 0
            if oponente.bottom >= tela_altura:
                oponente.bottom = tela_altura

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


    elif escolha == 2: 
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
                velo_bola_em_y *=-1

            if bola.left <= 0: 
                jogador_score += 1
                bola.center = (tela_largura/2,tela_altura/2)
                velo_bola_em_y *= random.choice((1,-1))
                velo_bola_em_x *= random.choice((1,-1))
            

            if bola.right >= tela_largura + 5:
                oponente_score += 1
                bola.center = (tela_largura/2,tela_altura/2)
                velo_bola_em_y *= random.choice((1,-1))
                velo_bola_em_x *= random.choice((1,-1))

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
