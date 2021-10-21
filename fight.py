import curses
from curses import textpad
import time
from menuControl import *
import fpstimer
from getInput import *
from itemControl import *
from playerAttack import *
def main(screen):

    #innitializing
    possibleInputs = [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT, 122, 120]
    screen.nodelay(1)
    timer = fpstimer.FPSTimer(60)
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    currentRow = 0
    secondaryRow = 0
    menu = ["Fight", "Act", "Item", "Mercy"]
    items = ["Glamburger", "Snowman Piece", "Hot Dog", "Banana", "Butterscotch Pie"]
    mercys = ["Spare", "Run"]
    acts = ["Talk"]
    fights = ["Alphys"]
    menus = {}
    menus.update({"Item": items})
    menus.update({"Mercy": mercys})
    menus.update({"Act": acts})
    menus.update({"Fight": fights})
    #make a dict of menu's here
    battleMenu = makeBattleMenu(screen, menu)
    inventory = makeItem(menus)
    mainText = ''
    newMainText = True
    gameMode = 'battleMenu'
    modeCheck = 'battleMenu'
    frameCounter = 0
    #Actual Main
    #1. Get game state
    #2. Get input
    #3a. Change // print menu
    #    or
    #3b. Change // print game
    #4.
    while 1:
        screen.clear()
        currentInput, currentRow, gameMode, secondaryRow = getInput(screen, gameMode, currentRow, secondaryRow, menus)
        mainText, newMainText, gameMode = printBattleMenu(screen, battleMenu, currentRow, gameMode, menus, secondaryRow, mainText, newMainText, inventory)
        if gameMode == "Alphys":
            playerAttack(screen, gameMode, frameCounter)
            frameCounter += 1
            if frameCounter == 149:
                frameCounter = 0
        screen.addstr(5, 5, str(currentInput))
        screen.addstr(10, 10, "hi")
        if not newMainText:
            screen.addstr(5, 15, str(secondaryRow))
            screen.addstr(10, 15, gameMode)
        if modeCheck != gameMode:
            secondaryRow = 0
        modeCheck = gameMode
        screen.refresh()
        timer.sleep()


curses.wrapper(main)
