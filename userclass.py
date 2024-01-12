#fixinghallway2.1copy copy HAS MORE RECENT UPDATES

from weapon1enemy1 import *
class enemy():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
King_M = enemy("King Minus", 100)

class player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
    def attack(weapon): #like this?
        King_M.health -= weapon.damage
        print(f"You have succesfully hit the king with a weapon and his health went do to {King_M.health}")
        
        



