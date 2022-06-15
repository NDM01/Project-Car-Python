x\import pygame
import random
import math
from pygame import mixer
from time import sleep

# Iniciar o pygame
pygame.init()

# Criar o screen
screen = pygame.display.set_mode((300, 650))

background = pygame.image.load('fundo.jpg')


def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (50, 300))

# Música
mixer.music.load('car.wav')
mixer.music.play(-1)


# Titlo e Icon
pygame.display.set_caption("Project Car")
icon = pygame.image.load('racing-flag.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('teste.png')
playerX = 115
playerY = 550
playerX_change = 0
playerY_change = 0

# Inimigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('car2.png'))
    enemyX.append(random.randint(0, 240))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(4)
    enemyY_change.append(1)

font = pygame.font.Font('freesansbold.ttf', 32)

# Texto Game Over

over_font = pygame.font.Font('freesansbold.ttf', 64)


def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 30:
        return True
    else:
        return False


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg[i], (x, y))


# Game Loop
running = True
while running:

    # RGB -Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Teclas
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 240:
        playerX = 240

    for i in range(num_of_enemies):

        if enemyY[i] == 630:
            for j in range(num_of_enemies):
                enemyX[i] = random.randint(0, 240)
                enemyY[j] = 0

            break

        # enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]
        if enemyY[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] = 0
        elif enemyX[i] >= 240:
            enemyX_change[i] = -1

        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if collision:
            game_over_text()
            sleep(1)
            break

        enemy(enemyX[i], enemyY[i])

    player(playerX, playerY)
    pygame.display.update()
