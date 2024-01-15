class weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

rock = weapon("rock", 5)
rope = weapon("rope", 10)
crowbar = weapon("crowbar", 30)
magical_wand = weapon("magical wand", 100)
m_wand = weapon("m wand", 50)


class enemy():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
King_M = enemy("King Minus", 100)

