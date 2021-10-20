from curses import textpad
import curses
from textControl import *
#This controls the creation and printing of the menu system

#Base class for the battle tabs
class battleTab:
    def __init__(self, yPos, xPos, text):
        self.yPos = yPos
        self.xPos = xPos
        self.text = text


#Innitializes the battle menu
def makeBattleMenu(screen, menu):
    battleMenu = {}
    sh, sw = screen.getmaxyx()
    for num, text in enumerate(menu):
        xVal = sw//4 * (num + 1) - sw//8 - 3
        battleMenu.update({text: battleTab(sh-2, xVal, text)})
    return battleMenu


#-----------------------------------------------#
#Prints the battle menu and colors
def printBattleMenu(screen, menu, currentRow, mode, menus, secondaryRow, mainText, newMainText, inventory):

    #Draw main screen box
    sh, sw = screen.getmaxyx()
    mainBox = [[sh//2 + 5, sw//4-sw//8],[sh - 5, sw//4 * 4 - sw//8]]
    textpad.rectangle(screen, mainBox[0][0], mainBox[0][1], mainBox[1][0], mainBox[1][1])


#Printing Text in Box

    #If I want to fully reset text, set both to ''
    #Only set mainText to '' to not have text animation
    if mode == 'battleMenu' and newMainText:
        newMainText = printMain(screen, mainBox, "Testing lol", mode)


#----------------------------------------------#
#Printing Menu's



#--Default Menu--------------------------------#


    if mode == 'battleMenu':
        #Write menu
        for row, tab in enumerate(menu):
            if row == currentRow:
                screen.attron(curses.color_pair(1))
                screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
                textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)
                screen.attroff(curses.color_pair(1))
            else:
               screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
               textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)

        #Write text (Does 1 by 1 if new)
        if newMainText:
            mode, mainText, newMainText = printMain(screen, mainBox, "Alphys is cool", mode, mainText)
        else:
            xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
            yRange = mainBox[1][0] - mainBox[0][0]
            screen.addstr((sh//2) + (yRange//3 + 1), (sh//2) + (yRange//3), "* Alphys is cool")


#--Fight Men--------------------------------#


    if mode == "Fight":
        screen.addstr(sh-10, sw//2, "Fight Menu")
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)


#--Act Men----------------------------------#


    if mode == "Act":
        screen.addstr(sh-10, sw//2, "Act Menu")
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)


#--Item Menu--------------------------------#


    if mode == "Item" and len(menus['Item']) > 0:
        xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
        yRange = mainBox[1][0] - mainBox[0][0]
        #Print Item Menu
        for num, item in enumerate(menus['Item']):
            if num == secondaryRow:
                screen.attron(curses.color_pair(1))
                screen.addstr((sh//2) + (yRange//3 + 1) * (num%3 + 1), xRange//4 * (num//3+1), "* {}".format(item))
                screen.attroff(curses.color_pair(1))
            else:
                screen.addstr((sh//2) + (yRange//3 + 1) * (num%3 + 1), xRange//4 * (num//3+1), "* {}".format(item))

         #Print defaul menu
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)

        #Tip Menu
        tipBox = [[sh//2+5, xRange//4 * 3],[sh -5, xRange]]
        textpad.rectangle(screen, tipBox[0][0], tipBox[0][1], tipBox[1][0], tipBox[1][1])

        screen.addstr(tipBox[0][0] + 2, tipBox[0][1] + 2, "* {}".format(
        inventory[menus['Item'][secondaryRow]].name))

        screen.addstr(tipBox[0][0] + 5, tipBox[0][1] + 4, "Heals for {}".format(
        inventory[menus['Item'][secondaryRow]].health))

        screen.addstr(tipBox[0][0] + 7, tipBox[0][1] + 4, "Has {} uses left".format(
        inventory[menus['Item'][secondaryRow]].useAmount))

        #This deals with wrapping text due to long tips
        xBuffer = 0
        yBuffer = 0
        for x in range(len(inventory[menus['Item'][secondaryRow]].tip)):
            if tipBox[0][1] + 4 + xBuffer >=  xRange - 8 and inventory[menus['Item'][secondaryRow]].tip[x] == " ":
                xBuffer = -1
                yBuffer += 1

            screen.addstr(tipBox[0][0] + 9 + yBuffer, tipBox[0][1] + 4 + xBuffer, "{}"
                    .format(inventory[menus['Item'][secondaryRow]].tip[x]))
            xBuffer += 1


#--Out Of Items----------------------------------#


    elif mode == "Item" and len(menus['Item']) == 0:
        xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
        yRange = mainBox[1][0] - mainBox[0][0]
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)
        screen.nodelay(0)
        screen.addstr((sh//2) + (yRange//3 + 1), (sh//2) + (yRange//3), "* You are out of items")
        screen.getch()
        screen.nodelay(1)
        return mainText, newMainText, "battleMenu"


#--Special text for using item-----------------#


    if mode in menus['Item']:
        xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
        yRange = mainBox[1][0] - mainBox[0][0]
        text = "* You ate the {} and gained {} health.".format(inventory[menus['Item'][secondaryRow]].name, inventory[menus['Item'][secondaryRow]].health)
        inventory[menus['Item'][secondaryRow]].use()
        if inventory[menus['Item'][secondaryRow]].useAmount == 0:
            inventory.pop(menus['Item'][secondaryRow])
            menus['Item'].remove(menus['Item'][secondaryRow])

    #Print defaul menu
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)
        #Exit
        screen.nodelay(0)
        screen.addstr((sh//2) + (yRange//3 + 1), (sh//2) + (yRange//3), text)
        screen.getch()
        screen.nodelay(1)
        return mainText, newMainText, "battleMenu"


#--Mercy Menu--------------------------------#


    if mode == "Mercy":
        xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
        yRange = mainBox[1][0] - mainBox[0][0]
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)
        for num, item in enumerate(menus['Mercy']):
            if num == secondaryRow:
                screen.attron(curses.color_pair(1))
                screen.addstr((sh//2) + (yRange//3 + 1) * (num%3 + 1), xRange//4 * (num//3+1), "* {}".format(item))
                screen.attroff(curses.color_pair(1))
            else:
                screen.addstr((sh//2) + (yRange//3 + 1) * (num%3 + 1), xRange//4 * (num//3+1), "* {}".format(item))


    return mainText, newMainText, mode


#--Mercy Menu Mode's------------------------#


    if mode in menus['Mercy']:
        xRange = mainBox[1][1] - mainBox[0][1] + sw//4-sw//8
        yRange = mainBox[1][0] - mainBox[0][0]
        for row, tab in enumerate(menu):
            screen.addstr(menu[tab].yPos, menu[tab].xPos, menu[tab].text)
            textpad.rectangle(screen, menu[tab].yPos - 1, menu[tab].xPos - 2, menu[tab].yPos + 1, menu[tab].xPos + 8)
        #if mode == "Run":
