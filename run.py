"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""
import curses
from curses import textpad

# Create window


def main(stdscr):
    """
    Code to create the game board
    """
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.refresh()
    stdscr.getch()

# Snake

# Food

# Keeping Score

# Game Over

# Difficulty Levels
