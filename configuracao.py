import pygame

pygame.init()
tempo = pygame.time.Clock()

#TELA COM BOM TAMANHO TALVEZ AUMENTAR
tela_largura = 900
tela_altura = 600
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption("Pong")


#OBJETOS FORMADOS POREM AJUSTAR TAMANHO
jogador = pygame.Rect(tela_largura - 20,tela_altura/2-70,10,140)
oponente = pygame.Rect(10,tela_altura/2-70,10,140)

bola = pygame.Rect(tela_largura/2- 15,tela_altura/2- 15,30,30)
#MAIS AJUSTE SOBRE A BOLA
velo_bola_em_y = 10
velo_bola_em_x = 10

#CORES
cor_para_tras = pygame.Color('grey12')
#a cor cinza
cor_cinza = (200,200,200)

tela.fill(cor_para_tras)
pygame.draw.rect(tela,cor_cinza, jogador)
pygame.draw.rect(tela,cor_cinza, bola)
pygame.draw.rect(tela,cor_cinza, oponente)
pygame.draw.aaline(tela,cor_cinza,(tela_largura/2,0), (tela_largura/2 , tela_altura))


# aqui está o limite da tela
x = 0
y = 0
descendo = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    tela.blit(bola,(x,y))

    if descendo:
        x = x + 1 
        y = y + 1 
    else: 
        x = x - 1
        y = y - 1

    if x > 900 or y > 600:
        descendo = False
    if x < 0 or y < 0:
        descendo = True
        
    pygame.display.update()

    

#Temos que determinar limites para a bola nao escapar, juntamente com isso se ela passar significa
#que algum dos lados terao recebido um ponto
