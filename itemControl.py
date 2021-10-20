class usable:
    def __init__(self, name, health, useAmount, tip):
        self.name = name
        self.health = health
        self.useAmount = useAmount
        self.tip = tip

    def use(self):
        self.useAmount -= 1

def makeItem(menus):
    inventory = {}
    for item in menus['Item']:
        if item == "Glamburger":
            inventory.update({item: usable(item, 40, 1, "It's a hamburger.")})
        elif item == "Snowman Piece":
            inventory.update({item: usable(item, 30, 1, "Piece of a snowman. It want's to go on an adventure.")})
        elif item == "Hot Dog":
            inventory.update({item: usable(item, 20, 1, "Hot Dob. The bun looks soggy. Guess you shouldn't have put it in your pocket.")})
        elif item == "Banana":
            inventory.update({item: usable(item, 25, 1, "Kris. Get the banana.")})
        elif item == "Banana Bunch":
            inventory.update({item: usable(item, 15, 4, "Wow, those banana's are not ripe.")})
        elif item == "Butterscotch Pie":
            inventory.update({item: usable(item, 40, 1, "A delicious looking pie. Smells like home.")})
    return inventory
