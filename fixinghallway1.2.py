import random

def choosing():
        #global obj
        obj = random.choice(['vase','book','frog', 'umbrella','spatula', 'briefcase', 'tophat', 'necklace', 'crown' ])
        print(f"You are required to find {obj} within the house. Good luck.")

from userclass import *
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
                
room_one_one = Room_one(1, item = "frog") # i added the item = but lets see if it works

room_two_one = Room_one(1, item = "spatula")
#print(room_two_one.item)
room_three_one = Room_one(1, item = "book")
#item = "frog"
#hallway = 1
#room_one = Room_one(1, ["frog", "spatula", "book"]) # replace spatula in second hallway room one
#room_one.message(item, hallway)

roomsone = [Room_one(1, item = "frog"), Room_one(1, item = "spatula"), Room_one(1, item = "book")]
Room_one_one = Room_one(1, item = "frog")

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
        r = 0
        if inp == "one":
                r = 1
        elif inp == "two":
                r = 2
        elif inp == "three":
                r = 3
        return r

def room_choice():
        #originally toNum again instead of int
        hchoice = toNum(input("what hallway do you want to travel down?  One, two, or three?"))
        if hchoice != "1" or hchoice != "2" or hchoice != "3":
                print("Too many errors. Game has ended.")
                quit()
        else:
                rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
                allrooms[hchoice -1][rchoice -1].message()


def pick_up(item):
    pick_up = input("If you believe this is the required item, will you pick it up?")
    if pick_up == "yes":
        print(item, obj)  # checking
        if item == obj:
            print("You have won the game, congratulations.")
            #item_found()
        else:
            print("You have lost. The game has ended.")
        exit()
    elif pick_up == "no":
        c = input("Would you like to travel down a different hallway? If no, you will stay in the current hallway and pick a different room.")
        if c == "yes":
            global hchoice
            hchoice = toNum(input("Choose a different hallway to travel down."))
            if hchoice not in [1, 2, 3]:
                print("Error, please pick an actual hallway.")  # check this
                pick_up(item)
            #global rchoice
            rchoice = toNum(input("Choose a room - one, two, or three. Remember you may have already traveled inside some."))
            allrooms[hchoice - 1][rchoice - 1].message()
        #testing for the c == "no"
        elif c == "no":
            print(f"{user} chooses to stay in the same hallway.")
            rchoice = toNum(input("Choose a room - one, two, or three. Remember you may have already traveled inside some."))
            allrooms[hchoice -1][rchoice -1].message()
          
            
#import random
#from roomclass import *
#from userclass import *
#from theobjclasscode import *
user = input("Choose your character's name.")
#name = player(user, []) #check this
# testing to see if the new code works here, not actual game
print(f"{user} was strolling on a walk with their grandmother when suddenly a rainbow van with frogs blocks your path.")
print(f"{user} blinks for one second, and suddenly, their grandmother is gone.")
print("They begin to panic frantically, and try to remember a minor detail from the van...")
#a = input("Thinking...")
print(f"The one thing {user} was able to recall was the name printed on the van: Evil King M the third")
print("They enter the name into their phone and recieved coordinates of the mansion")
print("You type the coordinates into google maps and follow the directions")
print("Suspiciously and carefully, you stumble into the mansion in the middle of an enigmatic forest, desperate to return your grandma to her retirement home")
print("Suddenly, a mysterious figure appears from the shadows.")
a = input("'Hello, my name is King M the Third. Would you like to play a game young one? If you win, you get your grandma back.' (yes or no)")
if a == "yes":
    import random
    obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'tophat', 'necklace', 'crown' ])
    print(f"You are required to find {obj} within the house. Good luck.")
    print("Before long, the mansion comes into sight. The door is unlocked.")
    hchoice = toNum(input("what hallway do you want to travel down? One, two, or three?"))
    #if hchoice != "one" or hchoice != "two" or hchoice != "three":
    #    print("Error, please pick an actual hallway.") #check this
    #    pick_up()
    rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
    #print(n)
    #print(rchoice)
    allrooms[hchoice -1][rchoice -1].message()


if a == "no":
    print("Then I guess you won't be getting your grandma back.")
    print("There is an ominous, final silence.")
    exit()
            




