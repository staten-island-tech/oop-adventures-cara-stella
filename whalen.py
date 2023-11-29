
class Room():
        def __init__self(self, number, items):
                self.number = number
                self.items = items
class Room_one(Room):
        def __init__self(self, number, items):
                super().__init__(number, items)
        def message(self, item):  
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {item}")
                pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                if pickup == "yes":
                        print("Congratulations, you have won the game.")

item = "frog"
room_one = Room_one(1, ["frog", "spatula", "book"]) # replace spatula in second hallway room one
room_one.message(item)

class Room_two(Room):
        def __init__self(self, number, items):
                super().__init__(number, items)
        def message(self, item):
                print(f"You hesitantly open the door, to find a master bedroom. With a few minutes of searching you find an {item}")
                pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                if pickup == "yes":
                        print("Congratulations, you have won the game.")
item = "necklace"
room_two = Room_two(2, ["necklace", "briefcase", "crown"])

class Room_three(Room):
        def __init__self(self, number, items):
                super().__init__(number, items)
        def message(self, item):
                print(f"This is obviously the bathroom, and an elaborate one at that. Who needs four showers? You find {item}")
                pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                if pickup == "yes":
                        print("Congratulations, you have won the game.")
item = "tophat"
room_three = Room_three(3, ["tophat", "vase", "unbrella"])