import curses
from curses import textpad

def playerAttack(screen, mode, frameCounter):
    #Draw the Box
    sh, sw = screen.getmaxyx()
    mainBox = [[sh//2 + 5, sw//4-sw//8],[sh - 5, sw//4 * 4 - sw//8]]
    textpad.rectangle(screen, mainBox[0][0], mainBox[0][1], mainBox[1][0], mainBox[1][1])
    xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
    yRange = mainBox[1][0] - mainBox[0][0]
    screen.addstr(20, 20, str(xRange-sw//4+sw//8-1))
    attrOn = False
    for line in range(xRange-sw//4+sw//8-1):
        if line == frameCounter:
            screen.attron(curses.color_pair(1))
            attrOn = True
        screen.addch(mainBox[0][0] + yRange//2, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= 20 and line <= 129:
            screen.addch(mainBox[0][0] + yRange//2+1, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-1, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= 40 and line <= 109:
            screen.addch(mainBox[0][0] + yRange//2+2, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-2, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= 60 and line <= 89:
            screen.addch(mainBox[0][0] + yRange//2+3, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-3, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= 70 and line <= 79:
            screen.addch(mainBox[0][0] + yRange//2+4, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-4, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= 73 and line <= 76:
            screen.addch(mainBox[0][0] + yRange//2+5, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-5, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= 74 and line <= 75:
            screen.addch(mainBox[0][0] + yRange//2+6, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-6, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if attrOn == True:
            screen.attroff(curses.color_pair(1))
            attrOn = False
