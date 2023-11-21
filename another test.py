import random 

obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'top hat', 'necklace', 'crown' ])
print(f"You are required to find {obj} within the house. Good luck.")

vase = "vase"
book = "book"
frog = "frog"
umbrella = "umbrella"
spatula = "spatula"
briefcase = 'briefcase'
tophat = "tophat"
necklace = "necklace"
crown = "crown"
  
x = "frog"
b = "necklace"
y = "tophat"

add = "...seeing that it is a guest room,"
def roomthree():
            print(f"You search through the room {add} and find a {y}")
            pickup = input("Do you want to pick the item up, if you believe it is the required item?")
            if pickup != "yes":
                print("Move to room three")
                roomthree()
            if pickup == "yes":
                if obj == y:
                    print("Congratulations, you have won the game.")
                    quit()
                if obj != x:
                     print("You lost. Womp womppp")
def roomtwo():
            add = " - its the master bedroom, once magnificent but now covered in dust,"
            print(f"You search through the room {add} and find a {b}")
            pickup = input("Do you want to pick the item up, if you believe it is the required item?")
            if pickup != "yes":
                print("move to room three")
                roomthree()
            if pickup == "yes":
                if obj == "frog":
                    print("Congratulations, you have won the game.")
                    quit()
                if obj != x:
                     print("You lost. Womp womppp")
def roomone():
            print(f"You search through the room. Somehow, you find a {x}")
            pickup = input("Do you want to pick the item up, if you believe it is the required item?")
            if pickup != "yes":
                print("Move to room two, you find your feet moving on your own.")
                roomtwo()
            if pickup == "yes":
                if obj == x:
                    print("Congratulations, you have won the game.")
                    quit()
                if obj != x:
                     print("You lost. Womp womppp")



firsthallway = input("There are three hallways to walk down.  Which do you choose?")

if firsthallway == "hallway one":
    print("As you walk down the eerie hallway, you realize that you can enter three rooms.")
    firstroom = input("Which do you choose to enter first?")
    if firstroom == "room one":
        roomone()
    if firstroom == "room two":
        roomtwo()
    if firstroom == "room three":
        roomthree()
if firsthallway == "hallway two":
    print("As you walk down the colorful hallway that reminds you of candyland, you realize you can enter three rooms.")
    firstroom = input("Which do you choose to enter first?")
    if firstroom == "room one":
        x = crown
        roomone()
    if firstroom == "room two":
        b = book
        roomtwo()
    if firstroom == "room three":
         y = vase
         roomthree()
#put code from that pull request into this new branch I made and then push