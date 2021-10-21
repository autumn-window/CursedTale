import curses
from curses import textpad

def playerAttack(screen, mode, frameCounter, key):
    #Draw the Box
    sh, sw = screen.getmaxyx()
    mainBox = [[sh//2 + 5, sw//4-sw//8],[sh - 5, sw//4 * 4 - sw//8]]
    textpad.rectangle(screen, mainBox[0][0], mainBox[0][1], mainBox[1][0], mainBox[1][1])
    xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
    yRange = mainBox[1][0] - mainBox[0][0]
    screen.addstr(20, 20, str(xRange-sw//4+sw//8-1))
    attrOn = False
    if key == 122 and frameCounter != 0:
        return "Attack"
    screen.addstr(20, 20, str(key))
    for line in range(xRange-sw//4+sw//8-1):
        if line == frameCounter:
            screen.attron(curses.color_pair(1))
            attrOn = True
        screen.addch(mainBox[0][0] + yRange//2, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= int(xRange//(xRange/20)) and line <= int((xRange - (xRange//(xRange/20)+xRange//8))):
            screen.addch(mainBox[0][0] + yRange//2+1, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-1, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= int(xRange//(xRange/40))-3 and line <= int((xRange - (xRange//(xRange/40)+xRange//8)))-3:
            screen.addch(mainBox[0][0] + yRange//2+2, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-2, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= int(xRange//(xRange/60))-3 and line <= int((xRange - (xRange//(xRange/60)+xRange//8)))-3:
            screen.addch(mainBox[0][0] + yRange//2+3, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-3, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= int(xRange//(xRange/70))-3 and line <= int((xRange - (xRange//(xRange/70)+xRange//8)))-3:
            screen.addch(mainBox[0][0] + yRange//2+4, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-4, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= int(xRange//(xRange/73))-3 and line <= int((xRange - (xRange//(xRange/73)+xRange//8)))-3:
            screen.addch(mainBox[0][0] + yRange//2+5, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-5, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if line >= int(xRange//(xRange/77))-3 and line <= int((xRange - (xRange//(xRange/77)+xRange//8)))-3:
            screen.addch(mainBox[0][0] + yRange//2+6, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
            screen.addch(mainBox[0][0] + yRange//2-6, line+1 + sw//4-sw//8, curses.ACS_CKBOARD)
        if attrOn == True:
            screen.attroff(curses.color_pair(1))
            attrOn = False
    return mode
