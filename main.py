import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()

MOVE_SPEED = 4
ENEMY_SPEED = 1
BULLET_SPEED = 2
MAX_ENEMIES = 200
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

hit_sound = pygame.mixer.Sound("bullet_sound.wav")

mixer.music.load("bg_music_jsb.mp3")
mixer.music.play(-1)
enemies = []
bullets = []

def findTopPlayerY():
    global enemies
    min_y=screen.get_height()

    for car in enemies:
        if car[1]<min_y:
            min_y=car[1]
    return min_y 

def generateEnemies():
    global enemies
    if (findTopPlayerY()> player.get_size()[1]) and (len(enemies)<MAX_ENEMIES):
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
    for enemy in enemies:
        enemy[1]+= ENEMY_SPEED

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
    
    RECT_PLAYER = Rect(player_x, player_y, PLAYER_SIZE[0] * 0.55, PLAYER_SIZE[1] * 0.55)
    for enemy in enemies:
        RECT_ENEMY = Rect(enemy[0], enemy[1], ENEMY_SIZE[0] * 0.55, ENEMY_SIZE[1] * 0.55)
        collide = pygame.Rect.colliderect(RECT_PLAYER, RECT_ENEMY)
        if collide:
            sys.exit()
            print("you have been hit")
            score = 0
def generate_bullets():
    global player_x
    global player_y
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN: 
    #         if event.key == pygame.K_j: 
    #             bullets.append([player_x, player_y])
    action = pygame.key.get_pressed()
    if action[pygame.K_j]:
        bullets.append([player_x, player_y])

def show_bullets():
    global screen
    for bullet in bullets:
        screen.blit(player, (bullet[0], bullet[1]))


def move_bullets():
    global bullets
    for bullet in bullets:
        bullet[1] -= BULLET_SPEED


def bullet_detect():
    global enemies
    global bullets
    for enemy in enemies:
        RECT_ENEMY = Rect(enemy[0], enemy[1], ENEMY_SIZE[0] * 0.55, ENEMY_SIZE[1] * 0.55)
        for bullet in bullets:
            RECT_BULLET = Rect(bullet[0], bullet[1], PLAYER_SIZE[0] * 0.55, PLAYER_SIZE[1] * 0.55)
            collide_2 = pygame.Rect.colliderect(RECT_BULLET, RECT_ENEMY)
            if collide_2:
                if enemy in enemies:
                    enemies.remove(enemy)
                    hit_sound.play()
            


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
    generateEnemies()
    moveEnemies()
    showEnemies()
    generate_bullets()
    show_bullets()
    move_bullets()
    bullet_detect()
    collision_detect()
    check_boundaries()
    remove_enemies()
    
    txtsurf = font.render("score:"+str(score), True, (255,255,0))
    screen.blit(txtsurf,(250,10))
    screen.blit(player, (player_x,player_y))
    score += 1
    pygame.display.update()
# while True:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#         # Handle key press events for movement
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             player_x -= MOVE_SPEED
#         if keys[pygame.K_RIGHT]:
#             player_x += MOVE_SPEED
#         if keys[pygame.K_UP]:
#             player_y -= MOVE_SPEED
#         if keys[pygame.K_DOWN]:
#             player_y += MOVE_SPEED

#         # Handle key press event for shooting (the 'j' key)
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_j:
#                 bullets.append([player_x, player_y])

#     screen.blit(bg, (0, 0))
#     generateEnemies()
#     moveEnemies()
#     showEnemies()
#     show_bullets()
#     move_bullets()
#     collision_detect()
#     check_boundaries()
#     remove_enemies()

#     txtsurf = font.render("score:" + str(score), True, (255, 255, 0))
#     screen.blit(txtsurf, (250, 10))
#     screen.blit(player, (player_x, player_y))
#     score += 1
#     pygame.display.update()
