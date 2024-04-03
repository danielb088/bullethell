import pygame
import sys
import random
from pygame.locals import *

MOVE_SPEED = 4
ENEMY_SPEED = 2
MAX_PALYERS = 2
LEFT_LANE_X = 0
RIGHT_LANE_X = 360
 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((360,640))

bg = pygame.image.load("background.png")
player = pygame.image.load("character.png")
enemy = pygame.image.load("enemies.png")


player_x = screen.get_width()/2 + 10
player_y = screen.get_height() - player.get_size()[1]

players = []

def findTopPlayerY():
    global players
    min_y=screen.get_height()

    for car in players:
        if car[1]<min_y:
            min_y=car[1]
    return min_y 



def generatePalyers():
    global players
    if (findTopPlayerY()> player.get_size()[1]) and (len(players)<MAX_PALYERS):
        x = random.randint(0,1)
        print(x)
        if x==0:
            x = random.randint(LEFT_LANE_X,LEFT_LANE_X+player.get_size()[0])
            print(x)
            players.append([x,0])
        else:
            x = random.randint(screen.get_width()//2 + 10,RIGHT_LANE_X)
            players.append([x,0])


def showPlayers():
    print(players)
    global screen
    for car in players:
        screen.blit(enemy, (car[0],car[1]))


def movePlayers():
    global players
    for car in players:
        car[1]+= ENEMY_SPEED


def check_boundries():
    global player_x
    if player_x<0:
        player_x=0
    if player_x>screen.get_width()-player.get_size()[0]:
        player_x = screen.get_width()-player.get_size()[0]




pygame.display.set_caption('bullet hell shooter')

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == K_LEFT:
            player_x -= MOVE_SPEED
        if event.key == K_RIGHT:
            player_x += MOVE_SPEED
        if event.key == K_UP:
            player_y -= MOVE_SPEED
        if event.key == K_DOWN:
            player_y += MOVE_SPEED
        
    screen.blit(bg,(0,0))
    movePlayers()
    generatePalyers()
    showPlayers()
    check_boundries()
    
    screen.blit(player, (player_x,player_y))


    pygame.display.update()
