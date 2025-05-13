








import math
import random
import pygame
#inicio del juego#
from pygame import mixer


pygame.int()

#se crea el fondo de pantalla#
screen = pygame.display.set_mode({1000,800})

#fondo de pantalla#
background = pygame,image.load('/media/pc07/MARI/Programación/Juego MariangelNB/Fondo.png')

#sonido#
mixer.music.load('/media/pc07/MARI/Programación/Juego MariangelNB/UTF-8background.wav')
mixer.music.play(-1)

#titulo e icono#
pygame.display.set_caption("Perdidos en ")
icon = pygame.image.load('/media/pc07/MARI/Programación/Juego MariangelNB/Enemigo_1-removebg-preview.png')
pygame.display.set_icon(icon)

#jugador#
PlayerIng=pygame.image.load('/media/pc07/MARI/Programación/Juego MariangelNB/Enemigo_1-removebg-preview.png')
playerX=370
playery=480
playerx_change=0


#enemigos#
enemyIng=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=20

for i in range ("num_of_enemies"):
    enemyIng.append(pygame).iamge.load('/media/pc07/MARI/Programación/Juego MariangelNB/Enemigo_2-removebg-preview.png')
    enemyX.append(random.randint(0.736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append (4)
    enemyY_change.append (40)

#disparo, proyectl, bala

armaIng=pygame.iamge.load('/media/pc07/MARI/Programación/Juego MariangelNB/Bala-removebg-preview.png')
arma=0
armaX_change=0
armaX_change=10
arma_estado="ready"

#puntaje#

score_value=0
Front = pygame.font.Font('freesansbolt.ttf',32)


textX=10
textY=10

#Juego terminado#
over_front =pygame.font.Font('freesansbolt.ttf',64)

def show_puntaje(x,y):
    score=font.render("Score : "+str(score_value,True,255,255,255))
    screen.blit(score,(x,y))
def gameover_text():
    over_text= over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(PlayerImg,(x,y))
def enemy(x,y,i):
     screen.blit(enemyImg[i],(x,y))
def Iniciar_disparo(x,y):
    global bulletstate
    arma_estado = "Fire"
    screen.blit(armaImg,(x+16,y+10))
def iscollision(enemyX,enemyY,armaX,armaY):
    distance=math,sqrt(math.pow(enemyX-armaX)+(math.pow(enemyY-armaY,2)))
    if distance<27:
        return True
    else : return False

#ciclo de juego#
running = True
while running:
    screen.fill((0,0,0))
    #imagen de fondo#
    screen.blit(background,(0,0))
    for event in pygame,event,get():
        if event.type == pygame.quit:
            running =False


            #si presiona derecha o izquierda#
            if event.type==pygame.KEYDOWN:
                if playerX_change==pygame.K_LEFT:
                    playerX_change=-5
                    event.key==pygame.K_RIGHT:
                    playerX_change=5
                    
                    