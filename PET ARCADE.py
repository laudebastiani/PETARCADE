import pygame, sys
from pygame import key
mainClock = pygame.time.Clock()
from pygame.locals import *
from pygame import mixer
import random 
from random import randint, randrange, choice
import time

pygame.init()
pygame.display.set_caption('PET ARCADE')
logo=pygame.image.load("snake/logosite.png")
pygame.display.set_icon(logo)

tela = pygame.display.set_mode((600, 600))

fundo_menu=pygame.image.load('menu/menu.png')
fundo_jogos=pygame.image.load('menu/jogos.png')
fundo_sobre=pygame.image.load('menu/sobre.png')
fundo_controles=pygame.image.load('menu/controles.png')


record1=0
record2=0
record3=0
record4=0
 
#snake variaveis
lista_cobra = []
comprimento_inicial = 5
x_maca = randint(40, 520)
y_maca = randint(170, 520)
x_cobra = int(300) 
y_cobra = int(360)
lista_cabeca = []
morreu = False

#dino variaveis
velocidade_jogo = 10
colidiu = False
velocidade_tela=velocidade_jogo-5
escolha_obstaculo = choice([0, 1])
xfundo=0

#space variaveis
pontos3=0
pontuação=0
highscore=0

musica_fundo = pygame.mixer.music.load('menu/musicamenu.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.045)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def menu_principal():
    global click
    while True:
 
        tela.blit(fundo_menu,(0,0))
        borda_1 = pygame.draw.rect(tela, (0, 0 , 0), (0,0,2,600))
        borda_2 = pygame.draw.rect(tela, (0, 0 , 0), (0,0,600,2))        
        borda_3 = pygame.draw.rect(tela, (0, 0 , 0), (598,0,2,600))
        borda_4 = pygame.draw.rect(tela, (0, 0 , 0), (0,598,600,2))
        
        mx, my = pygame.mouse.get_pos()
 
        b_jogar = pygame.Rect(190, 50, 300, 211)
        b_sobre = pygame.Rect(190, 50, 300, 298)
        b_sair = pygame.Rect(190, 50, 300, 387)
       
        if b_jogar.collidepoint((mx, my)):
            if click:
                jogos()
        if b_sobre.collidepoint((mx, my)):
            if click:
                sobre()
        if b_sair.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()    

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def jogos():
    global click
    running = True
    while running:
        
        tela.blit(fundo_jogos, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        b_snake = pygame.Rect(100, 100, 164, 220)
        b_dino = pygame.Rect(100, 100, 425, 220)
        b_space = pygame.Rect(100, 100, 165, 410)
        b_bird = pygame.Rect(100, 100, 425, 410)
        b_controles = pygame.Rect(236, 60, 300, 540)
        sair = pygame.Rect(0,0,64,64)

        click=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
                
        if b_snake.collidepoint((mx, my)):
            if click:
                snake()
        if b_dino.collidepoint((mx, my)):
            if click:
                dinossauro()
        if b_space.collidepoint((mx, my)):
            if click:
                space()
        if b_bird.collidepoint((mx, my)):
            if click:
                bird()
        if b_controles.collidepoint((mx, my)):
            if click:
                controles()
        if sair.collidepoint((mx, my)):
            if click:
                running=False
                menu_principal()
        
        pygame.display.update()
        mainClock.tick(60)
 
def sobre():
    global click
    running = True
    while running:
        tela.blit(fundo_sobre, (0,0))
 
        mx, my = pygame.mouse.get_pos()
        click=False
        sair1 = pygame.Rect(0,0,64,64)
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    menu_principal()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if sair1.collidepoint((mx, my)):
            if click:
                running = False
                menu_principal()
        
        pygame.display.update()
        mainClock.tick(60)

def controles():
    global click
    running = True
    while running:
        tela.blit(fundo_controles, (0,0))

        mx, my = pygame.mouse.get_pos()
        sair1 = pygame.Rect(0,0,64,64)
            
        click=False    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if sair1.collidepoint((mx, my)):
            if click:
                running = False
                jogos()

            
        pygame.display.update()
        mainClock.tick(60)

def snake(): 
    global click, record1, key
    running=True
    pygame.mixer.music.set_volume(0.025)
    musica_snake = pygame.mixer.music.load('snake/musica1.wav')
    pygame.mixer.music.play(-1)

    barulho_colisao = pygame.mixer.Sound('snake/coin.wav')
    barulho_perdeu = pygame.mixer.Sound('snake/fireball.wav')
    barulho_perdeu.set_volume(0.5)
    largura = 600
    altura = 600

    x_cobra = int(300) 
    y_cobra = int(360)

    velocidade = 11.5
    x_controle = velocidade
    y_controle = 0

    x_maca = randint(40, 520)
    y_maca = randint(170, 520)

    pontos = 0
    
    fonte = pygame.font.Font('ka1.ttf', 25, bold=True, italic=True)
    fonte2 = pygame.font.SysFont('arial', 20, True, True)

    tela = pygame.display.set_mode((largura, altura))
    relogio = pygame.time.Clock()
    lista_cobra = []
    comprimento_inicial = 5
    morreu = False

    imagens=["snake/lightning.png", "snake/gears.png", "snake/calculus2.png", "snake/calculus.png", "snake/atom.png", "snake/magnet.png", "snake/motherboard.png", "snake/coding.png", "snake/graduation.png", "snake/logosite.png"]
    i=0

    maça=pygame.image.load(imagens[i])
    maça=pygame.transform.scale(maça, (40,40))

    headu=pygame.image.load('snake/head_up.png')
    headd=pygame.image.load('snake/head_down.png')
    headr=pygame.image.load('snake/head_right.png')
    headl=pygame.image.load('snake/head_left.png')
    head=headr

    bodyr=pygame.image.load('snake/body_right.png')
    bodyl=pygame.image.load('snake/body_left.png')
    bodyu=pygame.image.load('snake/body_up.png')
    bodyd=pygame.image.load('snake/body_down.png')
    corpo=bodyr


    banner=pygame.image.load("snake/banner.png")
    banner=pygame.transform.scale(banner, (600,120))
    grama=pygame.image.load("snake/grama.png")
    grama=pygame.transform.scale(grama, (600,480))

    def aumenta_cobra(lista_cobra):
        for XeY in lista_cobra:
            #XeY = [x, y]
            #XeY[0] = x
            #XeY[1] = y

            pygame.draw.rect(tela, (247,132,17), (XeY[0], XeY[1], 20, 20))
            tela.blit(corpo, (XeY[0], XeY[1]))
            tela.blit(head, (x_cobra-2.5,y_cobra-2.5))


    while running:
        relogio.tick(30)
        tela.fill((0,0,0))

        tela.blit(banner, (0,0))
        
        borda1 = pygame.draw.rect(tela, (255, 0 , 0), (0,120,600,5))
        borda2 = pygame.draw.rect(tela, (255, 0 , 0), (595,120,5,480))
        borda3 = pygame.draw.rect(tela, (255, 0 , 0), (0,595,600,5))
        borda4 = pygame.draw.rect(tela, (255, 0 , 0), (0,120,5,475))
        
        tela.blit(grama, (0,120))

        
        mensagem = f'{pontos}'
        recorde = f'{record1}'
        texto_formatado = fonte.render(mensagem, True, (0,50,0))
        texto2 = fonte.render(recorde,True, (255,0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    head=headl
                    corpo=bodyl
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_RIGHT:
                    head=headr
                    corpo=bodyr
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_UP:
                    head=headu
                    corpo=bodyu
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                if event.key == K_DOWN:
                    head=headd
                    corpo=bodyd
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    running=False
                    pygame.mixer.music.set_volume(0.045)
                    musica_fundo = pygame.mixer.music.load('menu/musicamenu.wav')
                    pygame.mixer.music.play(-1)
                    jogos()


        x_cobra = x_cobra + x_controle
        y_cobra = y_cobra + y_controle
            
        cobra = pygame.draw.rect(tela, (247,132,17), (x_cobra-2.5,y_cobra-2.5,25,25))
        maca = pygame.draw.rect(tela, (0,255,0), (x_maca,y_maca,25,25))
        tela.blit(maça, (x_maca-7,y_maca-10))


        if cobra.colliderect(maca):
            x_maca = randint(50, 520)
            y_maca = randint(170, 520)
            pontos += 1
            barulho_colisao.play()
            i+=1
            comprimento_inicial+=1
            maça=pygame.image.load(imagens[i])
            maça=pygame.transform.scale(maça, (40,40))
            retmaça=maça.get_rect()
            if i==9:
                i=-1
        
        if pontos>record1:
            record1=pontos
        
        lista_cabeca = []
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)
        

        lista_cobra.append(lista_cabeca)

        if (lista_cobra.count(lista_cabeca) > 1) or cobra.colliderect(borda1) or cobra.colliderect(borda2) or cobra.colliderect(borda3) or cobra.colliderect(borda4):
            barulho_perdeu.play()
            mensagem = 'Game over! Pressione a tecla R para jogar novamente.'
            texto_formatado = fonte2.render(mensagem, True, (255,255,0))
            ret_texto = texto_formatado.get_rect() 
            i==0 
            
            morreu = True
            while morreu:
                tela.fill((0,0,0))
                
                velocidade=11.5

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:                       
                            snake()
                        if event.key == K_ESCAPE:
                            pygame.mixer.music.stop()
                            running=False
                            pygame.mixer.music.set_volume(0.045)
                            musica_fundo = pygame.mixer.music.load('menu/musicamenu.wav')
                            pygame.mixer.music.play(-1)
                            jogos()
                                                                                                  

                ret_texto.center = (largura//2, altura//2) 
                tela.blit(texto_formatado, ret_texto)
                pygame.display.update()

        
        if x_cobra > largura:
            x_cobra = 0
        if x_cobra < 0:
            x_cobra = largura
        if y_cobra < 0:
            y_cobra = altura
        if y_cobra > altura:
            y_cobra = 0

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]

        aumenta_cobra(lista_cobra)

        tela.blit(texto_formatado, (450,17))
        tela.blit(texto2, (530,72))

        pygame.display.set_caption("PET ARCADE")
        
        pygame.display.update()



def dinossauro():
    global click, record2

    LARGURA = 600
    ALTURA = 600
        
    BRANCO = (255,255,255)
    PRETO = (0,0,0)
    AMARELO = (255,255,0)
    AZUL = (0,0,255)
    VERMELHO = (255,0,0)

    tela = pygame.display.set_mode((LARGURA, ALTURA))

    pygame.display.set_caption('PET ARCADE')

    fundo = pygame.image.load('dino/fundo.png')

    banner = pygame.image.load('dino/banner.png')
    banner = pygame.transform.scale(banner, (600,120))

    sprite_sheet = pygame.image.load('dino/dinoSpritesheet.png').convert_alpha()
    sprite_sheet2 = pygame.image.load('dino/obstaculos.png').convert_alpha()

    pygame.mixer.music.set_volume(0.025)
    musica=pygame.mixer.music.load('dino/musica.wav')
    pygame.mixer.music.play(-1)

    som_colisao = pygame.mixer.Sound('dino/death_sound.wav')
    som_colisao.set_volume(0.5)


    colidiu = False

    escolha_obstaculo = choice([0, 1])

    n=1
    pontos = 0
  
    xfundo = 0
    velocidade_jogo = 10
    velocidade_tela = velocidade_jogo-5

    def exibe_mensagem(msg, tamanho, cor):
        fonte = pygame.font.Font('ka1.ttf', tamanho)
        mensagem = f'{msg}' 
        texto_formatado = fonte.render(mensagem, True, cor)
        return texto_formatado

    class Dino(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.imagens_dinossauro = []
            for i in range(3):
                img = sprite_sheet.subsurface((i * 32,0), (32,32))
                img = pygame.transform.scale(img, (32*3, 32*3))
                self.imagens_dinossauro.append(img)
            
            self.index_lista = 0
            self.image = self.imagens_dinossauro[self.index_lista]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.pos_y_inicial = ALTURA - 64 - 96//2
            self.rect.topleft = (100, self.pos_y_inicial) 
            self.pulo = False

        def pular(self):
            self.pulo = True


        def update(self):

            if self.pulo == True:
                if self.rect.y <= self.pos_y_inicial - 150:
                    self.pulo = False
                self.rect.y -= 15

            else:
                if self.rect.y >= self.pos_y_inicial:
                    self.rect.y = self.pos_y_inicial
                else:
                    self.rect.y += 15
            
    
            if self.index_lista > 2:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro[int(self.index_lista)]


    class Cacto(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = sprite_sheet2.subsurface((0*32, 0), (32,32))
            self.image = pygame.transform.scale(self.image, (32*2, 32*2))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.escolha = escolha_obstaculo
            self.rect.center = (LARGURA,  ALTURA - 64)
            self.rect.x = LARGURA

        def update(self):
            
            if self.escolha == 0:
                if self.rect.topright[0] < 0:
                    self.rect.x = LARGURA
                self.rect.x -= velocidade_jogo
        
            if velocidade_jogo<16:
                self.image = sprite_sheet2.subsurface((0*32, 0), (32,32))
                self.image = pygame.transform.scale(self.image, (32*2, 32*2))       
            
            if velocidade_jogo==16:
                self.image = sprite_sheet2.subsurface((1*32, 0), (32,32))
                self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        
            if velocidade_jogo==19:
                self.image = sprite_sheet2.subsurface((2*32, 0), (32,32))
                self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        
            if velocidade_jogo==22:
                self.image = sprite_sheet2.subsurface((3*32, 0), (32,32))
                self.image = pygame.transform.scale(self.image, (32*2, 32*2))
            
            if velocidade_jogo==25:
                self.image = sprite_sheet2.subsurface((4*32, 0), (32,32))
                self.image = pygame.transform.scale(self.image, (32*2, 32*2))
            
            if velocidade_jogo==28:      
                self.image = sprite_sheet2.subsurface((5*32, 0), (32,32))
                self.image = pygame.transform.scale(self.image, (32*2, 32*2))
                    

    class DinoVoador(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.imagens_dinossauro = []
            for i in range(3,5):
                img = sprite_sheet.subsurface((i*32, 0), (32,32))
                img = pygame.transform.scale(img, (32*3, 32*3))
                self.imagens_dinossauro.append(img)

            self.index_lista = 0
            self.image = self.imagens_dinossauro[self.index_lista]
            self.mask = pygame.mask.from_surface(self.image)
            self.escolha = escolha_obstaculo
            self.rect = self.image.get_rect()
            self.rect.center = (LARGURA, 420)
            self.rect.x = LARGURA
        
        def update(self):
            if self.escolha == 1:
                if self.rect.topright[0] < 0:
                    self.rect.x = LARGURA
                self.rect.x -= velocidade_jogo

                if self.index_lista > 1:
                    self.index_lista = 0
                self.index_lista += 0.25
                self.image = self.imagens_dinossauro[int(self.index_lista)]

    todas_as_sprites = pygame.sprite.Group()
    dino = Dino()
    todas_as_sprites.add(dino)

    cacto = Cacto()
    todas_as_sprites.add(cacto)

    dino_voador = DinoVoador()
    todas_as_sprites.add(dino_voador)

    grupo_obstaculos = pygame.sprite.Group()
    grupo_obstaculos.add(cacto)
    grupo_obstaculos.add(dino_voador)

    relogio = pygame.time.Clock()
    while True:
        relogio.tick(30)
        tela.fill(PRETO)
        tela.blit(banner,(0,0))
        xfundo-=velocidade_tela
        tela.blit(fundo,(xfundo,120))
        
        tela.blit(fundo,(xfundo+14000,120))
        tela.blit(fundo,(xfundo+2*14000,120))
        tela.blit(fundo,(xfundo+3*14000,120))
        tela.blit(fundo,(xfundo+4*14000,120))
        tela.blit(fundo,(xfundo+5*14000,120))
        tela.blit(fundo,(xfundo+6*14000,120))
        tela.blit(fundo,(xfundo+7*14000,120))
        tela.blit(fundo,(xfundo+8*14000,120))
        tela.blit(fundo,(xfundo+9*14000,120))
        tela.blit(fundo,(xfundo+10*14000,120))
        tela.blit(fundo,(xfundo+11*14000,120))
        tela.blit(fundo,(xfundo+12*14000,120))
        tela.blit(fundo,(xfundo+13*14000,120))
        tela.blit(fundo,(xfundo+14*14000,120))
        tela.blit(fundo,(xfundo+15*14000,120))
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and colidiu == False:
                    if dino.rect.y != dino.pos_y_inicial:
                        pass
                    else:
                        dino.pular()

                if event.key == K_r and colidiu == True:
                    dinossauro()

                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    running=False
                    pygame.mixer.music.set_volume(0.045)
                    musica_fundo = pygame.mixer.music.load('menu/musicamenu.wav')
                    pygame.mixer.music.play(-1)   
                    jogos()

        colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)

        todas_as_sprites.draw(tela)

        if cacto.rect.topright[0] <= 0 or dino_voador.rect.topright[0] <= 0:
            escolha_obstaculo = choice([0, 1])
            cacto.rect.x = LARGURA
            dino_voador.rect.x = LARGURA
            cacto.escolha = escolha_obstaculo
            dino_voador.escolha = escolha_obstaculo

        if colisoes and colidiu == False:
            pygame.mixer.music.stop() 
            som_colisao.play()
            colidiu = True

        
        if colidiu == True:
            if pontos % 100 == 0:
                pontos += 1
            game_over = exibe_mensagem('GAME OVER', 40, (255,255,0))
            tela.blit(game_over, (LARGURA//2 -40, ALTURA//2))
            restart = exibe_mensagem('Pressione r para reiniciar', 19, (AMARELO))
            tela.blit(restart, (LARGURA//2 -80, (ALTURA//2) + 60))
            velocidade_jogo=0
            velocidade_tela=0
            i=0
        

        else:
            pontos += 1
            if pontos>record2:
                record2=pontos
            todas_as_sprites.update()
            texto_pontos = exibe_mensagem(pontos, 25, (AZUL))
            texto_record = exibe_mensagem(record2,25,(VERMELHO))
        
        if pontos % 100 == 0:
            if velocidade_jogo >= 28:
                velocidade_jogo += 0
            else:
                velocidade_jogo += 1
                velocidade_tela = velocidade_jogo-5
            
        tela.blit(texto_pontos, (415, 17))
        tela.blit(texto_record, (487, 72))
        barreira=pygame.draw.rect(tela, PRETO, (0,120,600,4))

        pygame.display.flip()    

def space():
    global pontos3

    pontos3=0
    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()

    clock = pygame.time.Clock()
    fps = 60

    largura = 600
    altura = 600

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('PET ARCADE')

    
    font30 = pygame.font.Font('ka1.ttf', 20)
    font35 = pygame.font.Font('ka1.ttf', 25)
    font40 = pygame.font.Font('ka1.ttf', 30)


    explosion2_fx = pygame.mixer.Sound("space/explosion2.wav")
    explosion2_fx.set_volume(0.025)

    laser_fx = pygame.mixer.Sound("space/laser.wav")
    laser_fx.set_volume(0.02)

    musicabspace=pygame.mixer.music.load('space/musicaspace.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    linhas = 4
    colunas = 5
    alien_cooldown = 1000
    last_alien_shot = pygame.time.get_ticks()
    countdown = 3
    last_count = pygame.time.get_ticks()
    game_over = 0

    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    yellow = (255,255,0)


    bg = pygame.image.load("space/bg.png")
    banner = pygame.image.load("space/banner.png")
    banner = pygame.transform.scale(banner, (600, 120))  

    def draw_bg():
        tela.blit(bg, (0, 0))
        tela.blit(banner, (0,0))


    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        tela.blit(img, (x, y))


    class Spaceship(pygame.sprite.Sprite):
        def __init__(self, x, y, health):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("space/nave.png")
            self.image = pygame.transform.scale(self.image, (70,70))
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.health_start = health
            self.health_remaining = health
            self.last_shot = pygame.time.get_ticks()


        def update(self):
            
            speed = 8
            
            cooldown = 500
            game_over = 0

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= speed
            if key[pygame.K_RIGHT] and self.rect.right < largura:
                self.rect.x += speed

            time_now = pygame.time.get_ticks()
        
            if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
                laser_fx.play()
                bullet = Bullets(self.rect.centerx, self.rect.top)
                bullet_group.add(bullet)
                self.last_shot = time_now


            self.mask = pygame.mask.from_surface(self.image)

            pygame.draw.rect(tela, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
            if self.health_remaining > 0:
                pygame.draw.rect(tela, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
            elif self.health_remaining <= 0:
                explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
                explosion_group.add(explosion)
                self.kill()
                game_over = -1
            return game_over


    class Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("space/bala_nave.png")
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]

        def update(self):
            global pontos3, record3, pontuação, highscore
            self.rect.y -= 5
            if self.rect.bottom < 0:
                self.kill()
            if pygame.sprite.spritecollide(self, alien_group, True):
                self.kill()
                explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
                explosion_group.add(explosion)  
                pontos3+=1
                if record3<pontos3:
                    record3=pontos3      
            


    class Aliens(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("space/alien" + str(random.randint(1, 5)) + ".png")
            self.image = pygame.transform.scale(self.image, (40,40))  
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.move_counter = 0
            self.move_direction = 1

        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 75:
                self.move_direction *= -1
                self.move_counter *= self.move_direction



    class Alien_Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("space/bala_alien.png")
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]

        def update(self):
            self.rect.y += 2
            if self.rect.top > altura:
                self.kill()
            if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
                self.kill()
                explosion2_fx.play()

                spaceship.health_remaining -= 1
                explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
                explosion_group.add(explosion)



    class Explosion(pygame.sprite.Sprite):
        def __init__(self, x, y, size):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            for num in range(1, 6):
                img = pygame.image.load(f"space/exp{num}.png")
                if size == 1:
                    img = pygame.transform.scale(img, (20, 20))
                if size == 2:
                    img = pygame.transform.scale(img, (40, 40))
                if size == 3:
                    img = pygame.transform.scale(img, (160, 160))

                self.images.append(img)
            self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.counter = 0


        def update(self):
            explosion_speed = 3

            self.counter += 1

            if self.counter >= explosion_speed and self.index < len(self.images) - 1:
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]

            if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                self.kill()



    spaceship_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    alien_group = pygame.sprite.Group()
    alien_bullet_group = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()


    def create_aliens():

        for linha in range(linhas):
            for item in range(colunas):
                alien = Aliens(100 + item * 100, 175 + linha * 70)
                alien_group.add(alien)

    create_aliens()

    spaceship = Spaceship(int(largura / 2), altura - 50, 3)
    spaceship_group.add(spaceship)


    run = True
    while run:

        clock.tick(fps)

      
        draw_bg()
    
        
        if countdown == 0:

            time_now = pygame.time.get_ticks()

            if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
                attacking_alien = random.choice(alien_group.sprites())
                alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                alien_bullet_group.add(alien_bullet)
                last_alien_shot = time_now

          
            if len(alien_group) == 0:
                game_over = 1

            if game_over == 0:

                game_over = spaceship.update()

            
                bullet_group.update()
                alien_group.update()
                alien_bullet_group.update()
            else:
                if game_over == -1:
                    draw_text('GAME OVER!', font40, yellow, int(largura / 2 - 125), int(altura / 2 + 150))
                    draw_text('Pressione R para reiniciar', font30, yellow, int(largura / 2 - 200), int(altura / 2 + 200))
                if game_over == 1:
                    draw_text('Voce passou em todas as materias!', font30, yellow, int(largura / 2 - 250), int(altura / 2 ))
                    draw_text('Pressione R para reiniciar', font30, yellow, int(largura / 2 - 200), int(altura / 2 + 50))

        if countdown > 0:
            draw_text(str(countdown), font40, yellow, int(largura / 2 - 15), int(altura / 2 + 140))
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer

        key = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if (game_over==1 or game_over==-1) and key[pygame.K_r]:
                pontos3=0
                space()
                game_over=0
            if key[pygame.K_ESCAPE]:
                    running=False
                    pygame.mixer.music.stop()
                    musica_fundo = pygame.mixer.music.load('menu/musicamenu.wav')
                    pygame.mixer.music.set_volume(0.045)
                    pygame.mixer.music.play(-1)
                    jogos()


        
        pts = f'{pontos3}' 
        hs = f'{record3}'
        pontuação = font40.render(pts, True, yellow)
        highscore = font35.render(hs, True, green)
            
        explosion_group.update()


        spaceship_group.draw(tela)
        bullet_group.draw(tela)
        alien_group.draw(tela)
        alien_bullet_group.draw(tela)
        explosion_group.draw(tela)

        tela.blit(pontuação, (500, 13))
        tela.blit(highscore, (540, 72))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update() 

    pygame.quit()

def bird():
    global record4

    clock = pygame.time.Clock()
    fps = 60

    largura = 600
    altura = 600

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('PET ARCADE')


    font = pygame.font.Font('ka1.ttf', 28)


    white = (255, 255, 255)
    yellow = (255,255,0)
    purple = (255,0,255)

 
    ground_scroll = 0
    scroll_speed = 4
    flying = False
    game_over = False
    pipe_gap = 150
    pipe_frequency = 1500 
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    score = 0
    pass_pipe = False


    som_morreu = pygame.mixer.Sound('bird/fireball.wav')
    musicabird=pygame.mixer.music.load('bird/musicabird.wav')
    pygame.mixer.music.play(-1)


    bg = pygame.image.load('bird/fundo.png')
    bg = pygame.transform.scale(bg, (600,480))
    banner = pygame.image.load('bird/banner.png')
    ground_img = pygame.image.load('bird/ground.png')
    button_img = pygame.image.load('bird/restart.png')


    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        tela.blit(img, (x, y))


    def reset_game():
        pipe_group.empty()
        flappy.rect.x = 100
        flappy.rect.y = int(altura / 2)
        score = 0
        return score



    class Bird(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            self.index = 0
            self.counter = 0
            for num in range(1, 4):
                img = pygame.image.load(f'bird/bird{num}.png')
                self.images.append(img)
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.clicked = False

        def update(self):

            if flying == True:

                self.vel += 0.5
                if self.vel > 8:
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)

            if game_over == False:

                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                self.counter += 1
                flap_cooldown = 5

                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                self.image = self.images[self.index]

                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
            else:
                self.image = pygame.transform.rotate(self.images[self.index], -90)



    class Pipe(pygame.sprite.Sprite):
        def __init__(self, x, y, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('bird/pipe.png')
            self.rect = self.image.get_rect()

            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(pipe_gap / 2) + 80]
            if position == -1:
                self.rect.topleft = [x, y + int(pipe_gap / 2)+80]

        def update(self):
            self.rect.x -= scroll_speed
            if self.rect.right < 0:
                self.kill()


    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):

            action = False

            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    action = True

            tela.blit(self.image, (self.rect.x, self.rect.y))

            return action

    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()

    flappy = Bird(100, int((altura/2)+120))

    bird_group.add(flappy)

    button = Button(largura // 2 - 50, altura // 2 , button_img)

    run = True
    while run:

        clock.tick(fps)

        tela.blit(bg, (0,120))

        bird_group.draw(tela)
        bird_group.update()
        pipe_group.draw(tela)

        tela.blit(banner, (0,0))
        linha =  pygame.draw.rect(tela, (0, 0 , 0), (0,0,600,1))
        linha2 =  pygame.draw.rect(tela, (0, 0 , 0), (0,120,600,1))

        tela.blit(ground_img, (ground_scroll, 768))

        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
                if score>record4:
                    record4=score


        draw_text(str(score), font, yellow, 435, 15)
        draw_text(str(record4), font, purple, 510, 71)

        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            game_over = True

        if flappy.rect.bottom >= 600:
            game_over = True
            flying = False


        if game_over == False and flying == True:

            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipe(largura, int(altura / 2) + pipe_height, -1)
                top_pipe = Pipe(largura, int(altura / 2) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now

            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0

            pipe_group.update()

        if game_over == True:
            if button.draw() == True:
                game_over = False
                score = reset_game()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                flying = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        pygame.mixer.music.stop()
                        running=False
                        pygame.mixer.music.set_volume(0.045)
                        musica_fundo = pygame.mixer.music.load('menu/musicamenu.wav')
                        pygame.mixer.music.play(-1)
                        jogos()

        pygame.display.update()

    pygame.quit()

menu_principal()