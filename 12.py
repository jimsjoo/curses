import curses

screen = curses.initscr()
curses.nocbreak()   # Turn off cbreak mode
curses.echo()       # Turn echo back on
curses.curs_set(1)  # Turn cursor back on
# If initialized like `my_screen = curses.initscr()`
screen.keypad(0) # Turn off keypad keys