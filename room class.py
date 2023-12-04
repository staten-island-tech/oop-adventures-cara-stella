import random
obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'top hat', 'necklace', 'crown' ])
print(f"You are required to find {obj} within the house. Good luck.")

item = 'hi'

class Room():
        def __init__(self, hallway):
                self.hallway = hallway
class Room_one(Room):
        def __init__(self,  hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self, item):
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {item}")
                

#item = "frog"
#hallway = 1
#room_one = Room_one(1, ["frog", "spatula", "book"]) # replace spatula in second hallway room one
#room_one.message(item, hallway)
room_one_one = Room_one(1, item = ["frog"]) # i added the item = but lets see if it works
print(room_one_one.item)
room_two_one = Room_one(1, ["spatula"])
room_three_one = Room_one(1, ["book"])

class Room_two(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self, item):
                print(f"You hesitantly open the door, to find a master bedroom. With a few minutes of searching you find an {item}")
                #pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                #if pickup == "yes":
                #        print("Congratulations, you have won the game.")
                        
#item = "necklace"
#hallway = 1
#room_two = Room_two(2, [1, 2, 3], ["necklace", "briefcase", "crown"])
#room_two.message(item, hallway)

room_one_two = Room_two(2, ['necklace'])
room_two_two = Room_two(2, ["briefcase"])
room_three_two = Room_two(2, ["crown"])

class Room_three(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self, item):
                print(f"This is obviously the bathroom, and an elaborate one at that. You find {item}")
                pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                if pickup == "yes":
                        print("Congratulations, you have won the game.")
#item = "tophat"
#hallway = 1
#room_three = Room_three(3, [1, 2, 3], ["tophat", "vase", "unbrella"])
#room_two.message(item, hallway)

room_one_three = Room_three(3, ["tophat"])
room_two_three = Room_three(3, ["vase"])
room_three_three = Room_three(3, ["umbrella"])




""" def pick_up():
        print("If you believe this is the required item, will you pick it up?")
        if pick_up == "yes":
                if 

 """


