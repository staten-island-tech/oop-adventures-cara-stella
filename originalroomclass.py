import random
obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'top hat', 'necklace', 'crown' ])
obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'tophat', 'necklace', 'crown' ])
print(f"You are required to find {obj} within the house. Good luck.")


class Room():
        def __init__(self, hallway):
                self.hallway = hallway
class Room_one(Room):
        self.item = item
        def message(self):
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {self.item}")
                pick_up()
                pick_up(self.item)

room_one_one = Room_one(1, item = "frog") # i added the item = but lets see if it works

room_two_one = Room_one(1, item = "spatula")
#print(room_two_one.item)
room_three_one = Room_one(1, item = "book")

roomsone = [Room_one(1, item = "frog"), Room_one(1, item = "spatula"), Room_one(1, item = "book")]
class Room_two(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item

                
