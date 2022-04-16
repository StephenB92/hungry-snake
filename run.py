"""
The curses module is used to handle user keypresses,
allowing them to move the snake. The  random module
is used to randomly generate where food will appear.
The time module is used to make the snake continue in
the direction of the last direction key pressed by the
user, until they press another direction key.
"""
import curses
import random
import time

# Initialise the screen
sc = curses.initscr()
height, width = sc.getmaxyx()
win = curses.newwin(height, width, 0, 0)
win.keypad(1)  # Allows user key presses to be recognised
curses.curs_set(0)

# Starting snake and food positions
snake_head = [10, 15]
snake_position = [[15, 10], [14, 10], [13, 10]]
food_position = [20, 20]
SCORE = 0

# display food
# win.addch(food_position[0], food_position[1], curses.ACS_DIAMOND)

PREV_BUTTON_DIRECTION = 1
BUTTON_DIRECTION = 1
key = curses.KEY_RIGHT


a = []
while True:
    win.border(0)
    win.timeout(100)
    next_key = win.getch()

    if next_key == -1:
        key = win.getch()
    else:
        key = next_key

    # 0 = Left, 1 = Right, 3 = Up, 2 = Down
    if key == curses.KEY_LEFT and PREV_BUTTON_DIRECTION != 1:
        BUTTON_DIRECTION = 0
    elif key == curses.KEY_RIGHT and PREV_BUTTON_DIRECTION != 0:
        BUTTON_DIRECTION = 1
    elif key == curses.KEY_UP and PREV_BUTTON_DIRECTION != 2:
        BUTTON_DIRECTION = 3
    elif key == curses.KEY_DOWN and PREV_BUTTON_DIRECTION != 3:
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

    # Display Snake
    win.addch(snake_position[0][0], snake_position[0][1], '#')

sc.refresh()
time.sleep(2)
curses.endwin()
print(a)
