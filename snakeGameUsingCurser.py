import curses
from curses import textpad
import random

def create_food(snake, box):
    food = None

    while food is None:
        food = [random.randint(box[0][0] + 1, box[1][0] - 1), 
                random.randint(box[0][1] + 1, box[1][1] - 1)]

        if food in snake:
            food = None
    return food

def print_score(stdscr, score):
    sh, sw = stdscr.getmaxyx()
    score_text = 'Score: {}'.format(score)
    stdscr.addstr (0, sw//2 - len(score_text)//2, score_text)
    stdscr.refresh()



def main(stdscr):
    #To stop cursor blinking
    curses.curs_set(0)
    # Wait for the user to enter something for 150 ms before moving on
    stdscr.nodelay(1)
    stdscr.timeout(150)

    #Get the height and width of the screen
    sh, sw = stdscr.getmaxyx()

    #Coordinates of the rectangular box
    box = [[3, 3], [sh - 3, sw - 3]]

    #Draw a rectangle inside which snake moves
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    
    # Snake body will be displayed as ### i.e. in the x - direction 321>>> in the beginning 
    snake = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2-1]]
    direction = curses.KEY_RIGHT
    for y, x in snake:
        stdscr.addstr(y, x, "#")

    #Display the food 
    food = create_food (snake, box)
    stdscr.addstr(food[0], food[1], '*')
    
    #Define the score of user
    score = 0
    print_score(stdscr, score)

    #Changing the snakes direction as per the input
    while 1:
        key = stdscr.getch()
        
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            direction = key
        head = snake[0]
        if direction == curses.KEY_RIGHT:
            new_head = [head[0],head[1] + 1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0],head[1] - 1]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1,head[1]]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1,head[1]]

        # One # will add up in the snake body in the head direction 
        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '#')
        
        #Increase the score if snake has got the food else remove the extra #
        if snake[0] == food:
            food = create_food (snake, box)
            stdscr.addstr(food[0], food[1], '*') 
            score += 1
            print_score(stdscr, score)
        else:
             # Replace the last head i.e. the tail with a blank space
             stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
             # Remove the tail part that we changed with the blank space
             snake.pop() 
            
        # Losing condition
        if (snake[0][0] in [box[0][0], box[1][0]] or #If the y co-ordinate is on boundary of rectangle
            snake[0][1] in [box[0][1], box[1][1]] or #If the x co-ordinate is on the boundary of rectangle
            snake[0] in snake[1:]): #If the head has touched the body 
            msg = 'Game Over!'
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            
            #To wait for the user to press any key
            stdscr.nodelay(0)
            stdscr.getch()
            break

    #Update screen with new changes
    stdscr.refresh()
    #Get a key to exit
    stdscr.getch()



curses.wrapper(main)
