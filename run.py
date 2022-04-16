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
win.addch(food_position[0], food_position[1], curses.ACS_DIAMOND)

PREV_BUTTON_DIRECTION = 1
BUTTON_DIRECTION = 1
KEY = curses.KEY_RIGHT
