class player:
    def __init__(self,name, inventory):
        self.name = name
        self.inventory = inventory
    def pickup(self, item):
        self.inventory.append(item)
        print(self.inventory)
