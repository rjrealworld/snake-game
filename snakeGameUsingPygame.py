import random
import time
import pygame

#pygame window iniitialization
pygame.init()
clock = pygame.time.Clock()


#declare color rgb values
orangecolor = (255, 123, 7)
blackcolor = (0, 0, 0)
redcolor = (213, 50, 80)
bluecolor = (50, 153, 213)
greencolor = (0, 255, 0)


#display wondow's width and height
displayWidth = 600
displayHeight = 400
dis = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snake Game')
snake_block = 10
snake_speed = 15


#define ssnake structure and position
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolor, [x[0], x[1], snake_block, snake_block])

def snakeGame():
    game_over = False
    game_end = False
    #coordinates of the snake
    x1 = displayWidth / 2
    y1 = displayHeight / 2
    #when the snake moves
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, displayWidth - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, displayHeight - snake_block) / 10.0) * 10.0   

    while not game_over:
        while game_end == True:
            dis.fill(bluecolor)
            font_style = pygame.font.SysFont("comicsansms", 25)
            mesg = font_style.render("You Lost! Wanna play again? Press P", True, redcolor )
            dis.blit(mesg, [displayWidth / 6, displayHeight / 3])
            
            #display score
            score = length_of_snake - 1
            score_font = pygame.font.SysFont ("comicsansms", 35)
            value = score_font.render("Your score : " + str(score), True, greencolor)
            dis.blit(value, [displayWidth / 3, displayHeight / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakeGame()
                if event.type == pygame.QUIT:
                    game_over = True #game window is still open
                    game_end = False #game is ended

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= displayWidth or x1 < 0 or y1 >= displayHeight or y1 < 0:
            game_end = True
        
        #update coordinate with changed positions
        x1 += x1_change
        y1 += y1_change
        dis.fill((0,0,0))
        pygame.draw.rect(dis, greencolor, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        #when the length of snake exceeds, delete the snake_list which will end the game
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        #when snake hits itself, game ends
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()

        #when snake hits food, length is increased by one 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, displayWidth - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, displayHeight - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.display.update()
    pygame.quit()
    quit()

snakeGame()
