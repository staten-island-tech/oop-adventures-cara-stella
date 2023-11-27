
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

item = "Frog"
room_one = Room_one(1, ["Frog", "Comb"])
room_one.message(item)
