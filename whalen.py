class Room():
        def __init__(self,  hallway):
                self.hallway = hallway
class Room_one(Room):
        def __init__(self,  hallway, item):
                super().__init__(hallway)
                self.item = item
        def test(self):
                print(self.item, self.hallway)
        def message(self, item):
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {item}")
                




room_one_two = Room_one(2, ["necklace"])
room_one_two.test()