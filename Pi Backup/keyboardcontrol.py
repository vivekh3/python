import curses
screen=curses.initscr()
cureses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char=screen.getch()
        if char==ord('q'):
            break
        elif char==curses.KEY_UP:
            print ("up")
        elif char == curese.KEY_DOWN:
            print ("down")

finally:
    curses.nocbreak(); screen.keypad(0);curses.echo()
    curses.endwin()
