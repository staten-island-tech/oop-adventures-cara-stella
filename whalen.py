
class Room():
        def __init__self(self, number, items):
                self.number = number
                self.items = items
class Room_one(Room):
        def __init__self(self, number, hallway, items):
                super().__init__(number, hallway, items)
        def message(self, item):  
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {item}")



item = "frog"
hallway = 1
room_one = Room_one(1, [1, 2, 3], ["frog", "spatula", "book"]) # replace spatula in second hallway room one
room_one.message(item, hallway)

class Room_two(Room):
        def __init__self(self, number, hallway, items):
                super().__init__(number, hallway, items)
        def message(self, item):
                print(f"You hesitantly open the door, to find a master bedroom. With a few minutes of searching you find an {item}")
                pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                if pickup == "yes":
                        print("Congratulations, you have won the game.")
item = "necklace"
hallway = 1
room_two = Room_two(2, [1, 2, 3], ["necklace", "briefcase", "crown"])
room_two.message(item, hallway)

class Room_three(Room):
        def __init__self(self, number, hallway, items):
                super().__init__(number, hallway, items)
        def message(self, item):
                print(f"This is obviously the bathroom, and an elaborate one at that. Who needs four showers? You find {item}")
                pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                if pickup == "yes":
                        print("Congratulations, you have won the game.")
item = "tophat"
hallway = 1
room_three = Room_three(3, [1, 2, 3], ["tophat", "vase", "unbrella"])
room_two.message(item, hallway)





