import pygame

pygame.init()
tempo = pygame.time.Clock()

#musicas
menu_som = pygame.mixer.Sound('menu.mp3')
batida = pygame.mixer.Sound('batida.mp3')


# Configuração da tela
tela_largura = 1000
tela_altura = 480
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("obstaculo")

# obstaculo
obs_altura = 70
obs_larguea = 70
obstaculo = pygame.image.load('obstaculo.png').convert_alpha()
obstaculo = pygame.transform.scale(obstaculo, (obs_larguea, obs_altura))
obstaculo_pos = pygame.Rect(tela_largura + 100, tela_altura / 2, obs_larguea, obs_altura) 

# Carregar a imagem de fundo
fundo = pygame.image.load('cam.png').convert()
fundo = pygame.transform.scale(fundo, (tela_largura, tela_altura))

# Configuração dos objetos
jogador = pygame.Rect(tela_largura - 20, tela_altura / 2 - 70, 10, 140)
oponente = pygame.Rect(10, tela_altura / 2 - 70, 10, 140)
bola = pygame.Rect(tela_largura / 2 - 15, tela_altura / 2 - 15, 30, 30)

# imagens menu 

img1 = pygame.image.load('menu1.png').convert_alpha()
img1 = pygame.transform.scale(img1, [1000,480])
img2 = pygame.image.load('menu2.png').convert_alpha()
img2 = pygame.transform.scale(img2, [1000,480])

# imagem over 

img3 = pygame.image.load('over1.png').convert_alpha()
img3 = pygame.transform.scale(img3, [1000,480])
img4 = pygame.image.load('over2.png').convert_alpha()
img4 = pygame.transform.scale(img4, [1000,480])

 #Configuração da velocidade da bola/ jogadores
velo_bola_em_y = 6
velo_bola_em_x = 6
velo_jogadorx = 0
velo_jogadory = 0
velo_oponente = 0
velo_obstaculo= 1
velo_oponente = 9
velo_oponentey = 0
velo_oponentex = 0

#PLACAR INICIAL
jogador_score = 0
oponente_score = 0

# Configuração das cores
cor_para_tras = pygame.Color('grey12')
preto = (0, 0, 0)

azul = (0,0,250)
vermelho = (250,0,0)

fonte = pygame.font.Font("freesansbold.ttf",28)