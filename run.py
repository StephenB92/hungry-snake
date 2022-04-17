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

# Initialise the screen
sc = curses.initscr()
height, width = 30, 60
win = curses.newwin(height, width, 0, 0)

win.keypad(1)  # Allows user key presses to be recognised
# curses.curs_set(0)
curses.noecho()

# Starting snake and food positions
snake_head = [10, 15]
snake_position = [[15, 10], [14, 10], [13, 10]]
food_position = [20, 20]
SCORE = 0

# display food
win.addch(food_position[0], food_position[1], '*')

PREV_BUTTON_DIRECTION = 1
BUTTON_DIRECTION = 1
KEY = curses.KEY_RIGHT
PREV_KEY = KEY


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


a = []
while KEY != 27:
    win.border(0)
    win.timeout(100)

    next_key = win.getch()

    if next_key == -1:
        KEY = win.getch()
    else:
        KEY = next_key

    if KEY == ord(' '):
        KEY = - 1
        while KEY != ord(' '):
            key = win.getch()
        KEY = PREV_KEY
        continue

    # 0 = Left, 1 = Right, 3 = Up, 2 = Down
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

    # Increase Snake length on eating food
    if snake_head == food_position:
        food_position, SCORE = collect_food(SCORE)
        snake_position.insert(0, list(snake_head))
        a.append(food_position)
        win.addch(food_position[0], food_position[1], '*')

    else:
        snake_position.insert(0, list(snake_head))
        last = snake_position.pop()
        win.addch(last[0], last[1], ' ')

    # Display Snake
    win.addch(snake_position[0][0], snake_position[0][1], '=')

    # Game Over Conditions
    if (collision_with_boundaries(snake_head) == 1 or
            collision_with_self(snake_position) == 1):
        break


sc.addstr(f"Game Over. You helped the snake eat {SCORE} piece(s) of food!")
sc.refresh()
time.sleep(2)
curses.endwin()
print(a)
print(width, height)
