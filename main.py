import pygame
import sys
from pygame.locals import *

MOVE_SPEED = 20

clock = pygame.time.Clock()
screen = pygame.display.set_mode((562,600))

bg = pygame.image.load("bgimage.webp")
car = pygame.image.load("gohstpng.png")


car_x = screen.get_width()/2 + 10
car_y = screen.get_height() - car.get_size()[1]



def check_boundries():
    global car_x
    if car_x<0:
        car_x=0
    if car_x>screen.get_width()-car.get_size()[0]:
        car_x = screen.get_width()-car.get_size()[0]




pygame.display.set_caption('bullet hell shooter')

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                car_x -= MOVE_SPEED
            elif event.key == K_RIGHT:
                car_x += MOVE_SPEED
    
    check_boundries()
    screen.blit(bg,(0,0))
    screen.blit(car, (car_x,car_y))


    pygame.display.update()
