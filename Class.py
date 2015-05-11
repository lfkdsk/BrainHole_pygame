__author__ = 'Administrator'
import pygame

Window_width = 1365
Window_height = 768
screen = pygame.display.set_mode((Window_width, Window_height))
first_location = [screen.get_width() / 2, screen.get_height() / 2]
Player_image_up = ['resources/image/up-1.png', 'resources/image/up-2.png', 'resources/image/up-3.png',
                   'resources/image/up-4.png']
Player_image_down = ['resources/image/down-1.png', 'resources/image/down-2.png', 'resources/image/down-3.png',
                     'resources/image/down-4.png']
Player_image_left = ['resources/image/left-1.png', 'resources/image/left-2.png', 'resources/image/left-3.png',
                     'resources/image/left-4.png']
Player_image_right = ['resources/image/right-1.png', 'resources/image/right-2.png', 'resources/image/right-3.png',
                      'resources/image/right-4.png']
Enemy_image = ["resources/image/zm-1.png", "resources/image/zm-2.png"]
Bullets = []


class Enemy(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/image/zm-2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 2
        self.down_index = 0
        self.walk = 0

    def move(self):
        topleft = self.rect.topleft
        if self.walk > 40:
            self.walk = 0
            self.image = pygame.image.load("resources/image/zm-2.png")
        if self.walk == 20:
            self.image = pygame.image.load("resources/image/zm-1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.walk += 1
        self.rect.centerx -= self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/image/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = init_pos
        self.speed = 10
        self.walk = 0

    def move(self, button_flag):
        if button_flag == 1:
            self.rect.centerx -= self.speed
        elif button_flag == 0:
            self.rect.centerx += self.speed
        elif button_flag == 2:
            self.rect.centery += self.speed
        elif button_flag == 3:
            self.rect.centery -= self.speed
            # self.rect.centery += self.speed
            # screen.blit(self.image,self.rect)
            # pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/image/down-1.png')
        self.rect = self.image.get_rect()
        self.rect.center = first_location
        self.is_hit = False
        self.speed = 15
        self.down = 0
        self.left = 0
        self.right = 0
        self.up = 0
        # print self.rect.center

    def turn(self, distance):
        center = self.rect.center
        if distance == 2:
            if self.down > 3:
                self.down = 0
            self.image = pygame.image.load(Player_image_down[self.down])
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.down += 1
            # screen.blit(player.image, player.rect)
        elif distance == 0:
            if self.left > 3:
                self.left = 0
            self.image = pygame.image.load(Player_image_left[self.left])
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.left += 1
        elif distance == 3:
            if self.up > 3:
                self.up = 0
            self.image = pygame.image.load(Player_image_up[self.up])
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.up += 1
        elif distance == 1:
            if self.right > 3:
                self.right = 0
            self.image = pygame.image.load(Player_image_right[self.right])
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.right += 1

    def move(self, temper):
        temper = int(temper)
        if temper == 0:
            for temp in range(1, 10):
                self.rect.centerx -= 3
            print self.rect.centerx, self.rect.centery
        if temper == 1:
            self.rect.centerx += self.speed
            print self.rect.centery
        if temper == 2:
            self.rect.centery -= self.speed
            print self.rect.centerx, self.rect.centery
        if temper == 3:
            self.rect.centery += self.speed
        if 0 > self.rect.centerx or self.rect.centerx > screen.get_width():
            self.rect.centerx = -self.rect.centerx
        if 0 > self.rect.centery or self.rect.centery > screen.get_height():
            self.rect.centery = -self.rect.centery

    def shoot(self):
        bullet = Bullet(self.rect.midtop)
        Bullets.append(bullet)
