#Controls input from keyboard and sets gameModes
import curses

def getInput(screen, mode, battleRow, secondaryRow, menus):
    key = screen.getch()

    #Default Menu Controls (1d)

    if mode == 'battleMenu':
        #Control left and right
        if key == curses.KEY_LEFT and battleRow > 0:
            battleRow -= 1
        elif key == curses.KEY_RIGHT and battleRow < 3:
            battleRow += 1

        #If "Z" is pressed
        elif key == 122:
            if battleRow == 0:
                return key, battleRow, "Fight", secondaryRow
            elif battleRow == 1:
                return key, battleRow, "Act", secondaryRow
            elif battleRow == 2:
                return key, battleRow, "Item", secondaryRow
            elif battleRow == 3:
                return key, battleRow, "Mercy", secondaryRow
        return key, battleRow, mode, secondaryRow


    #Secondary Menu Controls (2d)
    if mode in menus:
        if key == 120:
            return key, battleRow, "battleMenu", secondaryRow

        elif key == 122:
            return key, battleRow, menus[mode][secondaryRow], secondaryRow

        elif key == curses.KEY_DOWN and secondaryRow%3 != 2 and secondaryRow < len(menus[mode])-1:
            return key, battleRow, mode, secondaryRow + 1

        elif key == curses.KEY_UP and secondaryRow%3 != 0:
            return key, battleRow, mode, secondaryRow - 1

        elif key == curses.KEY_LEFT and secondaryRow >= 3:
            return key, battleRow, mode, secondaryRow - 3

        elif key == curses.KEY_RIGHT and secondaryRow < len(menus[mode])-3:
            return key, battleRow, mode, secondaryRow + 3
        return key, battleRow, mode, secondaryRow
