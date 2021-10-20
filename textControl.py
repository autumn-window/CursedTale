import curses
from curses import textpad
import time

def printMain(screen, box, text, gameMode):
    sh, sw = screen.getmaxyx()
    xRange = box[1][1] - box[0][1] + sw//4-sw//8
    yRange = box[1][0] - box[0][0]
    for num in range(len(text)):
        if num == 0:
            screen.addstr((sh//2) + (yRange//3 + 1), (sh//2) + (yRange//3 + num), "* {}".format(text[num]))
        else:
            screen.addstr((sh//2) + (yRange//3 + 1), (sh//2) + (yRange//3 + num + 2), text[num])
        screen.refresh()
        time.sleep(.05)
    return False


def printSub(screen, gameMode, text):
    pass
