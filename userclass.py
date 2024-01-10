from weapon1enemy1 import *

class player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
    def attack(rock): #like this?
        print(f"{King_M.health - rock.damage}")
        
    def attack(rope):
        King_M.health - 10
        #print(f"Health lowered to {King_M.health}")
        print(King_M.health)
    def attack(crowbar):
        King_M.health - 30
        #print(f"Health lowered to {King_M.health}")
        print(King_M.health)
    def attack(magical_wand):
        King_M.health - 100
        #print(f"Health lowered to {King_M.health}")
        print(King_M.health) 
        # want to know how to specify attack based on weapon
        
        
class enemy():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
King_M = enemy("King Minus", 100)


print("fughgddg")
player.attack(rock)

