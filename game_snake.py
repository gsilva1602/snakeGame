import pygame
import random
import time

snake_speed = 15

# screen size
screen_x = 640
screen_y = 500

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# start pygame
pygame.init()

# start the game screen
pygame.display.set_caption('Little Snake Game')
game_window = pygame.display.set_mode((screen_x, screen_y))

# FPS
clock = pygame.time.Clock()

# snake default position
snake_position = [100, 50]

# first blocks of snake
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
fruit_position = [random.randrange(1, (screen_x//10) * 10),
                  random.randrange(1, (screen_y//10) * 10)]

fruit_spawn = True

# default snake direction
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# display score function
def display_score(choice, color, font, size):
    # font object
    score_font = pygame.font.SysFont(font, size)

    # display surface object
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # draw rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
    # creating font object
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface
    game_over_surface = my_font.render('Your Score was: ' + str(score), True, red)

    # create a rectangular object for the text
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (screen_x/2, screen_y/4)

    # draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # quit the program after 2 seconds
    time.sleep(2)

    # exit pygame library
    pygame.quit()

    # quit the program
    quit()

def spawn_fruit():
    global fruit_position
    while True:
        fruit_position = [random.randrange(1, (screen_x//10 - 1) * 10),
                        random.randrange(1, (screen_y//10 - 1) * 10)]
        if (
            abs(fruit_position[0] - snake_position[0]) > 20 or
            abs[fruit_position[1] - snake_position[1] > 20]
        ):
            break

# main program
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

    # if two keys pressed
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10    
    
    # snake body growing up

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # draw fruit
    fruit = pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    # colision with fruit
    snake_body_rects = [pygame.Rect(pos[0], pos[1], 10, 10) for pos in snake_body]
    snake_body.insert(0, list(snake_position))

    if any(snake_rect.colliderect(fruit) for snake_rect in snake_body_rects):
        spawn_fruit()
        score += 10
        snake_body.append(list(snake_position))
    else:
        snake_body.pop()
    

    # game over conditions
    if (snake_position[0] < 0 or snake_position[0] >= screen_x or 
        snake_position[1] < 0 or snake_position[1] >= screen_y):
        game_over()

    # touching the snake body
    for snake_rect in snake_body_rects[1:]:
        if snake_position[0] == snake_rect[0] and snake_position[1] == snake_rect[1]:
            game_over()
        
    # displaying score countinuously
    display_score(1, white, 'times new roman', 20)

    # update game screen
    pygame.display.update()

    pygame.display.flip()

    # fps
    clock.tick(snake_speed)        
