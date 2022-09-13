# 13:45 https://www.youtube.com/watch?v=txKBWtvV99Y

import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.init_pair(1)
    RED = curses.init_pair(2)

    for i in enumerate(maze):


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)

    # stdscr.clear()
    # stdscr.addstr(5, 5, 'Hello World!', blue_and_black)
    # stdscr.refresh()
    # stdscr.getch()


wrapper(main)
