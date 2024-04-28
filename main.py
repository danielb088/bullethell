import pygame
import sys
import random
from pygame.locals import *

pygame.init()

MOVE_SPEED = 4
ENEMY_SPEED = 1
MAX_PLAYERS = 10
LEFT_BORDER = 0
RIGHT_BORDER = 360
score = 0

font = pygame.font.SysFont("Arial", 26)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((360,640))

bg = pygame.image.load("background.png")
player = pygame.image.load("character.png")
enemy = pygame.image.load("enemies.png")

ENEMY_SIZE = enemy.get_size()
PLAYER_SIZE = player.get_size()

player_x = screen.get_width()/2 + 10
player_y = screen.get_height() - player.get_size()[1]

enemies = []

def findTopPlayerY():
    global enemies
    min_y=screen.get_height()

    for car in enemies:
        if car[1]<min_y:
            min_y=car[1]
    return min_y 

def generateEnemies():
    global enemies
    if (findTopPlayerY()> player.get_size()[1]) and (len(enemies)<MAX_PLAYERS):
        x = random.randint(0,1)
        print(x)
        if x==0:
            x = random.randint(LEFT_BORDER,LEFT_BORDER+screen.get_width())
            print(x)
            enemies.append([x,0])
        else:
            x = random.randint(0,RIGHT_BORDER)
            enemies.append([x,0])

def showEnemies():
    print(enemies)
    global screen
    for player in enemies:
        screen.blit(enemy, (player[0],player[1]))


def moveEnemies():  #move the enemies on screen
    global enemies
    for car in enemies:
        car[1]+= ENEMY_SPEED



def check_boundaries():
    global player_x
    global player_y
    if player_x < 0:
        player_x = 0
    if player_x>screen.get_width()-player.get_size()[0]:
        player_x = screen.get_width()-player.get_size()[0]
    if player_y < 0:
        player_y = 0
    if player_y > screen.get_height()-player.get_size()[1]:
        player_y = screen.get_height()-player.get_size()[1]

def remove_enemies():
    global enemies
    for player in enemies:
        if player[1] > screen.get_height()-enemy.get_size()[1]:
            enemies.remove(player)

def collision_detect():
    global enemies
    global PLAYER_SIZE
    global ENEMY_SIZE
    global player_x
    global player_y
    global score

    RECT_PLAYER = Rect(player_x, player_y, PLAYER_SIZE[0], PLAYER_SIZE[1])
    for enemy in enemies:
        RECT_ENEMY = Rect(enemy[0], enemy[1], ENEMY_SIZE[0], ENEMY_SIZE[1])
        collide = pygame.Rect.colliderect(RECT_PLAYER, RECT_ENEMY)
        if collide:
            print("you have been hit")
            score = 0
            
pygame.display.set_caption('bullet hell shooter')

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # MOVEMENT NO. 1:        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += MOVE_SPEED
    if keys[pygame.K_UP]:
        player_y -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        player_y += MOVE_SPEED
    #MOVEMENT NO. 2:
    # if event.type == pygame.KEYDOWN:
    #     if event.key == K_LEFT:
    #         player_x -= MOVE_SPEED
    #     if event.key == K_RIGHT:
    #         player_x += MOVE_SPEED
    #     if event.key == K_UP:
    #         player_y -= MOVE_SPEED
    #     if event.key == K_DOWN:
    #         player_y += MOVE_SPEED
        
    screen.blit(bg,(0,0)) 
    moveEnemies()
    generateEnemies()
    showEnemies()
    collision_detect()
    check_boundaries()
    remove_enemies()
    
    txtsurf = font.render("score:"+str(score), True, (255,255,0))
    screen.blit(txtsurf,(260,10))
    screen.blit(player, (player_x,player_y))
    score += 1
    pygame.display.update()
