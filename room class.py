import random
obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'top hat', 'necklace', 'crown' ])
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
                pick_up()
                

#item = "frog"
#hallway = 1
#room_one = Room_one(1, ["frog", "spatula", "book"]) # replace spatula in second hallway room one
#room_one.message(item, hallway)
room_one_one = Room_one(1, item = "frog") # i added the item = but lets see if it works

room_two_one = Room_one(1, item = "spatula")
#print(room_two_one.item)
room_three_one = Room_one(1, item = "book")

class Room_two(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"You hesitantly open the door, to find a master bedroom. With a few minutes of searching you find an {self.item}")
                #pickup = input("Do you want to pick the item up, if you believe it is the required item?")
                #if pickup == "yes":
                #        print("Congratulations, you have won the game.")
                pick_up()
            
                        
#item = "necklace"
#hallway = 1
#room_two = Room_two(2, [1, 2, 3], ["necklace", "briefcase", "crown"])
#room_two.message(item, hallway)

room_one_two = Room_two(2, item = 'necklace')
#room_one_two.message()
room_two_two = Room_two(2, item = "briefcase")
room_three_two = Room_two(2, item = "crown")

class Room_three(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"This is obviously the bathroom, and an elaborate one at that. You find {self.item}")
                pick_up()
                #pickup = input("Do you want to pick the item up, if you believe it is the required item? this will repeat, please repeat answer")
                #if pickup == "yes":
                        #print("Congratulations, you have won the game.")
#item = "tophat"
#hallway = 1
#room_three = Room_three(3, [1, 2, 3], ["tophat", "vase", "unbrella"])
#room_two.message(item, hallway)

room_one_three = Room_three(3, item = 'tophat')
room_two_three = Room_three(3, item = "vase")
room_three_three = Room_three(3, item = "umbrella")


item = []

def pick_up():
        pick_up = input(("If you believe this is the required item, will you pick it up?"))
        if pick_up == "yes":
                item.append
                print (item)
                if item == obj:
                        print("You have won the game, congratulations.")
                if item != obj:
                        print("You have lost. The game has ended.")
        if pick_up == "no":
                hchoice = input(("Choose a different hallway to travel down."))
                if hchoice == "one":
                        rchoice = input(("Choose a room - one, two, or three. Remember you may have already travelled inside some."))
                        if rchoice == "one":
                                room_one_one.message()
                                pick_up()
                        if rchoice == "two":
                                room_two_one.message()
                                pick_up()
                        if rchoice == "three":
                                room_three_one.message()
                                pick_up()
                if hchoice == "two":
                        rchoice = input(("Choose a room - one, two, or three. Remember you may have already travelled inside some."))
                        if rchoice == "one":
                                room_one_two.message()
                                pick_up()
                        if rchoice == "two":
                                room_two_two.message()
                                pick_up()
                        if rchoice == "three":
                                room_three_two.message()
                                pick_up()
                if hchoice == "three":
                        rchoice = input(("Choose a room - one, two, or three. Remember you may have already travelled inside some."))
                        if rchoice == "one":
                                room_one_three.message()
                                pick_up()
                        if rchoice == "two":
                                room_two_three.message()
                                pick_up()
                        if rchoice == "three":
                                room_three_three.message()
                                pick_up()

#room_three_three.message()
pick_up()

                



