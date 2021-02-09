# Nick Colonna

import pygame
import random

DISPLAY_W = 600
DISPLAY_H = 400
BLOCK_SIZE = 10
SNAKE_SPEED = 25

pygame.init()
dis = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
pygame.display.set_caption("Snake Game by Nick Colonna")
pygame.display.update()
clock = pygame.time.Clock()
red = (255,0,0)
cyan = (0,255,255)
grey = (125,125,125)
black = (0,0,0)
white = (255,255,255)
dis.fill(grey)
font_style = pygame.font.SysFont("comicsansms", 20)
lose_message = font_style.render("You Lost! Press Q to Quit or SPACE to Play Again",True,cyan)


# Function builds the body of the snake using coordinates from snake_list
def build_snake(snake_list):
    for i, block in enumerate(snake_list):
        if len(snake_list) % 2 == 0:    # alternate snake body colors - snake head is always red
            if i % 2 == 0:
            	pygame.draw.rect(dis, white, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))
            else:
            	pygame.draw.rect(dis, red, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))
        else:
            if i % 2 == 0:
                pygame.draw.rect(dis, red, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))
            else:
                pygame.draw.rect(dis, white, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))


# Score keeping function to display score on screen
def keep_score(snake_length):
    score_message = font_style.render("Score: {}".format(snake_length),True,white)
    dis.blit(score_message, [5,5])


# Function contains the core game controls
def snake_game():
    game_over = False
    game_lose = False
    snake_x = int(DISPLAY_W / 2) 
    snake_y = int(DISPLAY_H / 2)
    dx = 0
    dy = 0
    food_x = BLOCK_SIZE * random.randint(0,(DISPLAY_W/BLOCK_SIZE)-1)
    food_y = BLOCK_SIZE * random.randint(0,(DISPLAY_H/BLOCK_SIZE)-1)
    snake_list = []
    snake_length = 1
    
    while game_over == False:
        while(game_lose == True):   #Only runs when player loses
            dis.fill(black)
            keep_score(snake_length - 1)
            dis.blit(lose_message, [75,185])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # Quit program if window is clicked closed
                    game_over = True
                    game_lose = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #Quit game if Q
                        game_over = True
                        game_lose = False
                    elif event.key == pygame.K_SPACE: #Restart game is Space
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Quit program if window is clicked closed
                game_over = True

            if event.type == pygame.KEYDOWN:    # Check for movement key press
                if event.key == pygame.K_UP:
                    if dy==BLOCK_SIZE and snake_length > 1:   # You cannot switch directions if snake is bigger than one cube
                        pass
                    else:
                        dx = 0
                        dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    if dy==-BLOCK_SIZE and snake_length > 1:
                        pass
                    else:
                        dx = 0
                        dy = BLOCK_SIZE
                elif event.key == pygame.K_LEFT:
                    if dx==BLOCK_SIZE and snake_length > 1:
                        pass
                    else:
                        dx = -BLOCK_SIZE
                        dy = 0
                elif event.key == pygame.K_RIGHT:
                    if dx==-BLOCK_SIZE and snake_length > 1:
                        pass
                    else:
                        dx = BLOCK_SIZE
                        dy = 0

        snake_x += dx
        snake_y += dy
        
        if (snake_x < 0) or (snake_x > DISPLAY_W-BLOCK_SIZE) or (snake_y < 0) or (snake_y > DISPLAY_H-BLOCK_SIZE):  # Game over when snake hits boundaries
            game_lose = True

        if ((snake_length-1)//5) % 2 == 1:
            dis.fill(black)
        else:
            dis.fill(grey)

        pygame.draw.rect(dis, cyan, (food_x, food_y,BLOCK_SIZE,BLOCK_SIZE))
        
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for block in snake_list[:-1]:   # trigger Game Over message if snake eats itself
            if block == snake_head:
                game_lose = True
        
        build_snake(snake_list)
        
        if snake_x == food_x and snake_y == food_y:     # Grow snake after it eats food and generate more food
            snake_length += 1
            food_x = BLOCK_SIZE * random.randint(0, DISPLAY_W/BLOCK_SIZE-1)
            food_y = BLOCK_SIZE * random.randint(0, DISPLAY_H/BLOCK_SIZE-1)
        
        keep_score(snake_length - 1)
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()


# Starts the game
snake_game() 