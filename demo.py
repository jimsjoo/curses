import curses
import traceback
import random
import time

def print_center(message):
    num_rows, num_cols = stdscr.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    stdscr.addstr(middle_row, x_position, message, curses.A_REVERSE)
    stdscr.refresh()
    # win = curses.newwin(5, 20, 10, 10)
    # win.border(0) 
    # win.addstr(10,10,message)   
    # win.refresh()   

try:
    # -- Initialize --
    stdscr = curses.initscr()   # initialize curses screen
    curses.curs_set(0)    
    print_center(" [theBANDER], Autonomous trading ")
    curses.napms(2000)    
    stdscr.clear()

    stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc
    stdscr.border(0)
    curses.noecho()             # turn off auto echoing of keypress on to screen
    curses.cbreak()             # enter break mode where pressing Enter key

    stdscr.addstr(0, 0, " theBANDER  ---- Press q to exit ---- ", curses.A_REVERSE)
    # win = curses.newwin(15, 20, 0, 0)
    # win.border(0) 
    # win.addstr(1, 1, str(num_rows))   
    # win.refresh()   
    
    stdscr.refresh()
    while True:
        # stay in this loop till the user presses 'q'        
        ch = stdscr.getch()
        if ch == ord('q'):
            break
except:
    traceback.print_exc()     # print trace back log of the error
    
finally:
    # --- Cleanup on exit ---
    stdscr.keypad(0)
    curses.echo()

    curses.nocbreak()
    curses.endwin()

# The wrapper() helper function.
# While the basic invocation above is easy enough, the curses package provides the wrapper(func, ...) helper function. The example below contains the equivalent of above:

# main(scr, *args):
#     # -- Perform an action with Screen --
#     scr.border(0)
#     scr.addstr(5, 5, 'Hello from Curses!', curses.A_BOLD)
#     scr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)

#     while True:
#         # stay in this loop till the user presses 'q'
#         ch = scr.getch()
#         if ch == ord('q'):
    
# curses.wrapper(main)