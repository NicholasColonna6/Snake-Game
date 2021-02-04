import pygame
import random

DISPLAY_W = 600
DISPLAY_H = 400
BLOCK_SIZE = 10
SNAKE_SPEED = 30

pygame.init()
dis = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
pygame.display.set_caption("Snake Game by Nick Colonna")
pygame.display.update()
clock = pygame.time.Clock()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
grey = (125,125,125)
white = (255,255,255)
cyan = (0,255,255)
dis.fill(grey)
font_style = pygame.font.SysFont("freesans", 20)
lose_message = font_style.render("You Lost! Press SPACE to Play Again or Q to Quit",True,cyan)


# build snake based on locations in snake_list
def build_snake(snake_list):
    for i, block in enumerate(snake_list):
        if len(snake_list) % 2 == 0:
            if i % 2 == 0:
            	pygame.draw.rect(dis, blue, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))
            else:
            	pygame.draw.rect(dis, red, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))
        else:
            if i % 2 == 0:
                pygame.draw.rect(dis, red, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))
            else:
                pygame.draw.rect(dis, blue, (block[0],block[1],BLOCK_SIZE,BLOCK_SIZE))


# keep track of score at top of screen
def keep_score(snake_length):
    score_message = font_style.render("Score: {}".format(snake_length),True,white)
    dis.blit(score_message, [5,5])


# main game loop
def game_loop():
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
        while(game_lose == True):
            dis.fill(black)
            dis.blit(lose_message, [75,185])
            pygame.display.update()
            for event in pygame.event.get():
                # if 'X' was clicked to quit program
                if event.type == pygame.QUIT:
                    game_over = True
                    game_lose = False

                if event.type == pygame.KEYDOWN:
                    #if 'q' pressed, quit game
                    if event.key == pygame.K_q:
                        game_over = True
                        game_lose = False
                    #if 'space' pressed, restart game
                    elif event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            # if 'X' was clicked to quit program
            if event.type == pygame.QUIT:
                game_over = True

            # check if arrow key was clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = BLOCK_SIZE
                elif event.key == pygame.K_LEFT:
                    dx= -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0

        snake_x += dx
        snake_y += dy
        #if snake hits the edge of display, game over
        if (snake_x < 0) or (snake_x > DISPLAY_W-BLOCK_SIZE) or (snake_y < 0) or (snake_y > DISPLAY_H-BLOCK_SIZE):
            game_lose = True

        dis.fill(grey)
        pygame.draw.rect(dis, cyan, (food_x, food_y,BLOCK_SIZE,BLOCK_SIZE))
        
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # if snake eats itself, you lose
        for block in snake_list[:-1]:
            if block == snake_head:
                game_lose = True
        
        build_snake(snake_list)
        
        # if snake eats food, grow in size by one and generate more food
        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            food_x = BLOCK_SIZE * random.randint(0, DISPLAY_W/BLOCK_SIZE-1)
            food_y = BLOCK_SIZE * random.randint(0, DISPLAY_H/BLOCK_SIZE-1)
        
        keep_score(snake_length - 1)
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()

#initial game call
game_loop()