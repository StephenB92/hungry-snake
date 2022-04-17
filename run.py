"""
The curses module is used to handle user keypresses,
allowing them to move the snake. The  random module
is used to randomly generate where food will appear.
The time module is used to time out the game over screen
and game window.
"""
import curses
import random
import time

# Credit to The AI Learner and the article "Snake Game using Python Curses"
# For code and logic used as this projects template.

# Initialise the screen
sc = curses.initscr()
height, width = 20, 80
win = curses.newwin(height, width, 0, 0)
win.keypad(1)  # Allows user key presses to be recognised
curses.noecho()  # Prevents user key presses registering on terminal window

# Starting snake and food positions
snake_head = [10, 15]
snake_position = [[15, 10], [14, 10], [13, 10]]
food_position = [18, 18]

SCORE = 0

# Display food
win.addch(food_position[0], food_position[1], '*')

# Initial key press values
PREV_BUTTON_DIRECTION = 1
BUTTON_DIRECTION = 1
KEY = curses.KEY_RIGHT
PREV_KEY = KEY

# Credit to The AI Learner and the article "Snake Game using Python Curses"
# For code and logic used as this projects template.


def collect_food(SCORE):
    """
    This function increases the users score when food is
    collected and randomly generates the next piece of food
    """
    food_position = [random.randint(1, height - 2),
                     random.randint(1, width - 2)]
    SCORE += 1
    return food_position, SCORE


def collision_with_boundaries(snake_head):
    """
    This function detects when the snake head touches
    the edges of the screen
    """
    if (snake_head[0] >= height - 1 or snake_head[0] <= 0 or
            snake_head[1] >= width - 1 or snake_head[1] <= 0):
        return 1
    else:
        return 0


def collision_with_self(snake_position):
    """
    This function detects when the snake head touches
    another part of the snake
    """
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0


# Main game loop
# Credit to The AI Learner and the article "Snake Game using Python Curses"
# For code and logic used as this projects template.
a = []
# Credit to sanchitgangwar on Github, for the code to make the
# while loop dependent on the ESC key being pressed
while KEY != 27:  # Ensures that the game runs until ESC is pressed
    win.border(0)
    win.timeout(100)

    next_key = win.getch()
    # If statement allowing control of snake
    if next_key == -1:
        KEY = win.getch()
    else:
        KEY = next_key
    # If statement that handles "Pause" feature
    # Credit to sanchitgangwar on Github,
    # for code used for the pause game feature.
    if KEY == ord(' '):
        KEY = - 1
        while KEY != ord(' '):
            pause = "*PAUSE*"
            # Credit to YouTube user Indian Pythonista and their video
            # "Creating Snake Game for Terminal | Intro to curses in Python
            # (Part-3)" for the code used to place the *PAUSED* text
            win.addstr(height // 2, width // 2 - len(pause) // 2, pause)
            KEY = win.getch()
        KEY = PREV_KEY
        win.addstr(height // 2, width // 2 - len(pause) // 2, "       ")
        continue

    # 0 = Left, 1 = Right, 3 = Up, 2 = Down
    # If statement controlling snake movement and preventing users
    # being able to press a reverse direction key and crash snake into self
    if KEY == curses.KEY_LEFT and PREV_BUTTON_DIRECTION != 1:
        BUTTON_DIRECTION = 0
    elif KEY == curses.KEY_RIGHT and PREV_BUTTON_DIRECTION != 0:
        BUTTON_DIRECTION = 1
    elif KEY == curses.KEY_UP and PREV_BUTTON_DIRECTION != 2:
        BUTTON_DIRECTION = 3
    elif KEY == curses.KEY_DOWN and PREV_BUTTON_DIRECTION != 3:
        BUTTON_DIRECTION = 2
    else:
        pass

    PREV_BUTTON_DIRECTION = BUTTON_DIRECTION

    # Changes snake head position based on key direction
    if BUTTON_DIRECTION == 1:
        snake_head[1] += 1
    elif BUTTON_DIRECTION == 0:
        snake_head[1] -= 1
    elif BUTTON_DIRECTION == 2:
        snake_head[0] += 1
    elif BUTTON_DIRECTION == 3:
        snake_head[0] -= 1

    # Increase snake length on eating food
    if snake_head == food_position:
        food_position, SCORE = collect_food(SCORE)
        snake_position.insert(0, list(snake_head))
        a.append(food_position)
        win.addch(food_position[0], food_position[1], '*')
    else:
        snake_position.insert(0, list(snake_head))
        last = snake_position.pop()
        win.addch(last[0], last[1], ' ')

    # Display snake
    win.addch(snake_position[0][0], snake_position[0][1], '#')

    # Game over conditions
    if (collision_with_boundaries(snake_head) == 1 or
            collision_with_self(snake_position) == 1):
        break


sc.addstr(f"Thankssssss!! You helped the snake eat {SCORE} piece(s) of food!")
sc.refresh()
time.sleep(2)
curses.endwin()
print(a)
print(width, height)
