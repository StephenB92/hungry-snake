"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""
import curses
from curses import textpad

PLAYING = True

# Create window


def main(stdscr):
    """
    Code to create the game board
    """
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    box = [[3, 3], [height-3, width-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    # Defining the snake variable and positioning in center of screen
    snake = [[height // 2, width // 2 + 1], [height // 2, width // 2],
             [height // 2, width // 2 - 1]]
    direction = curses.KEY_RIGHT

    for y, x in snake:
        stdscr.addstr(y, x, '=')

    stdscr.getch()

    # Allowing user key presses to control the snake
    while PLAYING is True:

        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP,
                   curses.KEY_DOWN]:
            direction = key

        head = snake[0]
        new_head = [0]

        if key == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]

        # Code to create an extra '=' in snakes movement
        # direction and remove its tail

        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '=')

        stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        snake.pop()

        stdscr.refresh()


curses.wrapper(main)

# Food

# Keeping Score

# Game Over

# Difficulty Levels
