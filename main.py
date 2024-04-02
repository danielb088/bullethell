import pygame
import sys
from pygame.locals import *

MOVE_SPEED = 4

clock = pygame.time.Clock()
screen = pygame.display.set_mode((360,640))

bg = pygame.image.load("background.png")
player = pygame.image.load("character.png")


player_x = screen.get_width()/2 + 10
player_y = screen.get_height() - player.get_size()[1]



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
        elif event.key == K_RIGHT:
            player_x += MOVE_SPEED
    
    check_boundries()
    screen.blit(bg,(0,0))
    screen.blit(player, (player_x,player_y))


    pygame.display.update()
