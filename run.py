"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""
import curses

# Create window

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
