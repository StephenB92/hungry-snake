"""
The curses module is used to handle user keypresses,
allowing them to move the snake and the  random module
is used to randomly generate where food will appear
"""
import curses
from curses import textpad
import random

PLAYING = True


def spawn_food(snake, box):
    """
    This function generates food at random places
    on the board
    """
    food = None

    while food is None:
        food = [random.randint(box[0][0] + 1, box[1][0] - 1),
                random.randint(box[0][1] + 1, box[1][1] - 1)]
        if food in snake:
            food = None
    return food

# Create window


def main(stdscr):
    """
    Code to create the game board
    """
    curses.curs_set(0)
    # stdscr.nodelay(1)
    # stdscr.timeout(100)
    height, width = stdscr.getmaxyx()
    box = [[3, 3], [height-3, width-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    # Defining the snake variable and positioning in center of screen
    snake = [[height // 2, width // 2 + 1], [height // 2, width // 2],
             [height // 2, width // 2 - 1]]
    direction = curses.KEY_RIGHT
    # Creating the snake
    for y, x in snake:
        stdscr.addstr(y, x, '=')
    # Creating the food
    food = spawn_food(snake, box)
    stdscr.addstr(food[0], food[1], '*')
    # Displays the user's score
    score = 0
    score_text = f"Score: {score}"
    stdscr.addstr(0, width // 2 - len(score_text) // 2, score_text)

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

        # Increases the size of the snake when food is eaten

        if snake[0] == food:
            food = spawn_food(snake, box)
            stdscr.addstr(food[0], food[1], '*')
            score += 1
            score_text = f"Score: {score}"
            stdscr.addstr(0, width // 2 - len(score_text) // 2, score_text)
        else:
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        # Logic for Game Over conditions
        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]] or
                snake[0] in snake[1:]):
            game_over = "Oops!! Watch where you're going next time!"
            stdscr.addstr(height // 2, width // 2
                          - len(game_over) // 2, game_over)
            stdscr.nodelay(0)
            stdscr.getch()
            break

        stdscr.refresh()


curses.wrapper(main)


# Keeping Score

# Game Over

# Difficulty Levels
