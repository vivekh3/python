import curses
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad()

while (True):
    char=screen.getch()
    if char==ord('q'):
        break
    elif char==KEY_UP:
        print("Up")
    elif char==KEY_DOWN:
        print("Down")
    elif char==KEY_LEFT:
        print("Left")
    elif char==KEY_RIGHT:
        print("Right")

curses.echo()
curses.nocbreak()
screen.keypad(0)
curses.endwin()

