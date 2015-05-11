import random

__author__ = 'Administrator'

from pygame.locals import *
from Class import *
from sys import exit


background_image_filename = 'resources/image/gamestart.png'
start_image = 'resources/image/bg2.png'
dead_image = 'resources/image/dead.png'

Score = 0
x = 0
y = 0
pygame.init()
pygame.mixer.init()
background = pygame.image.load(background_image_filename).convert()
pygame.key.set_repeat(100, 100)
clock = pygame.time.Clock()

pygame.mixer.music.load("resources/music/butterflylove.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

button_music = pygame.mixer.Sound("resources/music/bullet.wav")
button_music.set_volume(10)
# music

def Waitkey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    exit()
                if event.key == K_RETURN:
                    return
# font
flag = 0
button_flag = 0
enemies = []
enemies_down = []
enemy_frequency = 0
running = True
while running:
    clock.tick(60)
    if enemy_frequency % 50 == 0:
        enemy1_pos = [screen.get_width(), random.randint(0, screen.get_height())]
        enemy1 = Enemy(enemy1_pos)
        enemies.append(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0
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
                    button_flag = 0
                    # flag == 1
                    print "buttonflag" and button_flag
            elif event.key == pygame.K_LEFT:
                if flag == 1:
                    player.turn(0)
                    player.move(0)
                    button_flag = 1
                    print "buttonflag" and button_flag
            elif event.key == pygame.K_UP:
                if flag == 1:
                    player.turn(3)
                    player.move(2)
                    button_flag = 3
                    # flag == 1
            elif event.key == pygame.K_DOWN:
                if flag == 1:
                    player.turn(2)
                    player.move(3)
                    button_flag = 2
            elif event.key == pygame.K_x:
                if flag == 1:
                    player.shoot()
                    button_music.play()
                    print("shoot")
    screen.blit(background, (x, y))
    if flag == 1:
        score_font = pygame.font.Font(None, 50)
        score_surf = score_font.render("Score: " + str(Score), 1, (0, 0, 0))
        screen.blit(score_surf, [10, 10])
        screen.blit(player.image, player.rect)
        for enemy in enemies:
            enemy.move()
            screen.blit(enemy.image, enemy.rect)
            if enemy.rect.left < 0:
                enemies.remove(enemy)
                break
            if pygame.sprite.collide_circle(enemy, player):
                enemies_down.append(enemy)
                enemies.remove(enemy)
                # player.is_hit = True
                Score -= 1
                # Game_Over()
                break
        for bullet in Bullets:
            bullet.move(button_flag)
            screen.blit(bullet.image, bullet.rect)
            for enemy in enemies:
                if pygame.sprite.collide_circle(bullet, enemy):
                    enemies_down.append(enemy)
                    enemies.remove(enemy)
                    Bullets.remove(bullet)
                    Score += 1
                    break
            if bullet is not None:
                if bullet.rect.bottom < 0 or bullet.rect.centerx > screen.get_width() or bullet.rect.centerx < 0:
                    Bullets.remove(bullet)
        if Score < -10:
            background_dead = pygame.image.load(dead_image).convert()
            screen.blit(background_dead, (x, y))
    pygame.display.update()
    if flag == 0:
        pygame.display.update()



