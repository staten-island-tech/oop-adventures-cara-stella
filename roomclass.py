import random
obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'tophat', 'necklace', 'crown' ])
print(f"You are required to find {obj} within the house. Good luck.")


class Room():
        def __init__(self, hallway):
                self.hallway = hallway
class Room_one(Room):
        def __init__(self,  hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {self.item}")
                pick_up(self.item)
                

#item = "frog"
#hallway = 1
#room_one = Room_one(1, ["frog", "spatula", "book"]) # replace spatula in second hallway room one
#room_one.message(item, hallway)

roomsone = [Room_one(1, item = "frog"), Room_one(1, item = "spatula"), Room_one(1, item = "book")]
class Room_two(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"You hesitantly open the door, to find a master bedroom. With a few minutes of searching you find an {self.item}")
                #pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                #if pickup == "yes":
                #        print("Congratulations, you have won the game.")
                pick_up(self.item)
            
                        
#item = "necklace"
#hallway = 1
#room_two = Room_two(2, [1, 2, 3], ["necklace", "briefcase", "crown"])
#room_two.message(item, hallway)


roomstwo = [Room_two(2, item = 'necklace'), Room_two(2, item = "briefcase"), Room_two(2, item = "crown")]
class Room_three(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"This is obviously the bathroom, and an elaborate one at that. You find {self.item}")
                
                #pickup = input("Do you want to pick the item up, if you believe it is the required item? this will repeat, please repeat answer")
                #if pickup == "yes":
                        #print("Congratulations, you have won the game.")
                pick_up(self.item)
#item = "tophat"
#hallway = 1
#room_three = Room_three(3, [1, 2, 3], ["tophat", "vase", "unbrella"])
#room_two.message(item, hallway)


roomsthree = [Room_three(3, item = 'tophat'), Room_three(3, item = "vase"), Room_three(3, item = "umbrella")]
allrooms = [roomsone, roomstwo, roomsthree]
itemlist = []
# the problem is that the variable "item" below is not defined. How do I make self.item be recognized?
def toNum(inp):
        if inp == "one":
                r = 1
        elif inp == "two":
                r = 2
        elif inp == "three":
                r = 3
        return r
def pick_up(item):
        pick_up = input(("If you believe this is the required item, will you pick it up?"))
        if pick_up == "yes":
                itemlist.append()
                print(item)
                if item == obj:
                        print("You have won the game, congratulations.")
                else:
                        print("You have lost. The game has ended.")
                exit()
        if pick_up == "no":
                hchoice = toNum(input(("Choose a different hallway to travel down.")))
                rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
                allrooms[hchoice -1][rchoice -1].message()

