from weapon1enemy1 import *

class player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
    def attack(rock): #like this?
        x = King_M.health - 5
        print(f"Health lowered to {x}")
    def attack(rope):
        King_M.health - 10
        print(f"Health lowered to {King_M.health}")
    def attack(crowbar):
        King_M.health - 30
        print(f"Health lowered to {King_M.health}")
    def attack(magical_wand):
        King_M.health - 100
        print(f"Health lowered to {King_M.health}")
              
        # want to know how to specify attack based on weapon
        
        


