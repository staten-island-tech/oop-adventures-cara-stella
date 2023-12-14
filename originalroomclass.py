import random
obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'top hat', 'necklace', 'crown' ])
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

room_one_one = Room_one(1, item = "frog") # i added the item = but lets see if it works

room_two_one = Room_one(1, item = "spatula")
#print(room_two_one.item)
room_three_one = Room_one(1, item = "book")

roomsone = [Room_one(1, item = "frog"), Room_one(1, item = "spatula"), Room_one(1, item = "book")]
class Room_two(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item




def pick_up():
        pick_up = input(print("If you believe this is the required item, will you pick it up?"))
        if pick_up == "yes":
                if obj != item:
                        print


        if pick_up == "no":
                hchoice = print("choose a different room to go into.")
                if hchoice == "one":
                        rchoice = input(print("Choose a room - one, two, or three. Remember you may have already travelled inside some."))
                        if rchoice == "one":
                                room_one_one #fix the rooms bc i want the code to run but the item to change per each room in same hallway
                                room_one_one.message()
                                pick_up()
                        if rchoice == "two":
                                room_two_one
                                room_two_one.message()
                                pick_up()
                        if rchoice == "three":
                                room_three_one
                                room_three_one.message()
                                pick_up()
                elif hchoice == "two":
                        if rchoice == "one":
                                room_one_two #same for these
                                room_one_two.message()
                                pick_up()
                        if rchoice == "two":
                                room_two_two
                                room_two_two.message()
                                pick_up()
                        if rchoice == "three":
                                room_three_two
                                room_three_two.message()
                                pick_up()
                elif hchoice == "three":
                        if rchoice == "one":
                                room_one_three #and these
                                room_one_three.message()
                                pick_up()
                        if rchoice == "two":
                                room_two_three
                                room_two_three.message()
                                pick_up()
                        if rchoice == "three":
                                room_three_three
        
                                room_three_three.message()
                                pick_up()
                
