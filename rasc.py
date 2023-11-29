import pygame
import random

black = pygame.Color(0, 0 , 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Little Snake Game')

# rect for snake and fruit
snake = pygame.Rect(300, 230, 20, 20)
fruit = pygame.Rect(20, 20, 20, 20)

pads = [snake, fruit]

snake_speed = 15

# FPS
clock = pygame.time.Clock()

# snake position and fruit position
snake_position = [100, 50]

def spawn_fruit():
    global fruit
    fruit = [random.randrange(1, (640//10) * 10),
                      random.randrange(1, (480//10) * 10)]

# snake default direction
direction = 'RIGHT'

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if snake.collidelist(pads) >= 0:
        pygame.QUIT

    pygame.draw.rect(screen, white, snake)

    for pad in pads:
        pygame.draw.rect(screen, white, pad)

    pygame.display.update()

    clock.tick(snake_speed)