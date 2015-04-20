__author__ = 'Administrator'

import pygame
from pygame.locals import *
from sys import exit


class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bullet.gif')
        self.rect = self.image.get_rect()
        self.rect.midtop = init_pos
        self.speed = 10

    def move(self):
        self.rect.centerx += self.speed
        # screen.blit(self.image,self.rect)
        #pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('right.png')
        self.rect = self.image.get_rect()
        self.rect.center = first_location
        # print self.rect.center

    def turn(self, distance):
        center = self.rect.center
        self.image = pygame.image.load(Player_image[distance])
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self, temper):
        temper = int(temper)
        if temper == 0:
            for temp in range(1, 10):
                self.rect.centerx -= 3
            print self.rect.centerx
        if temper == 1:
            self.rect.centerx += 30
            print self.rect.centery
        if temper == 2:
            self.rect.centery -= 30
            print self.rect.centery
        if temper == 3:
            self.rect.centery += 30
        if 0 > self.rect.centerx or self.rect.centerx > screen.get_width():
            self.rect.centerx = -self.rect.centerx
        if 0 > self.rect.centery or self.rect.centery > screen.get_height():
            self.rect.centery = -self.rect.centery

    def shoot(self):
        bullet = Bullet(self.rect.midtop)
        Bullets.append(bullet)


background_image_filename = 'gamestart.png'
start_image = 'bg2.png'
Player_image = ['left.png', 'right.png']
x = 0
y = 0
pygame.init()
screen = pygame.display.set_mode([1365, 768])
first_location = [screen.get_width() / 2, screen.get_height() / 2]
background = pygame.image.load(background_image_filename).convert()
pygame.key.set_repeat(100, 100)
clock = pygame.time.Clock()
flag = 0
Bullets = []
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if flag == 0:
                if event.key == pygame.K_1:
                    background = pygame.image.load(start_image).convert()
                    player = Player()
                    print screen.get_width()
                    print screen.get_height()
                    flag = 1
            elif event.key == pygame.K_4:
                exit()
            elif event.key == pygame.K_RIGHT:
                if flag == 1:
                    player.turn(1)
                    player.move(1)
                    # flag == 1
            elif event.key == pygame.K_LEFT:
                if flag == 1:
                    player.turn(0)
                    player.move(0)
            elif event.key == pygame.K_UP:
                if flag == 1:
                    player.move(2)
                    # flag == 1
            elif event.key == pygame.K_DOWN:
                if flag == 1:
                    player.move(3)
            elif event.key == pygame.K_x:
                if flag == 1:
                    player.shoot()
                    print("shoot")
    screen.blit(background, (x, y))
    if flag == 1:
        screen.blit(player.image, player.rect)
        for bullet in Bullets:
            bullet.move()
            screen.blit(bullet.image, bullet.rect)
    pygame.display.update()
    if flag == 0:
        pygame.display.update()



