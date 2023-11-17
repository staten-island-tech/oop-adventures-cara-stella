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

def firstroom():
    if firstroom == "room one":
            print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {frog}")
            pickup = input("Do you want to pick the item up, if you believe it is the required item?")
            if pickup == "yes":
                if obj == "frog":
                    print("Congratulations, you have won the game.")
                    quit()


firsthallway = input("There are three hallways to walk down.  Which do you choose?")

if firsthallway == "hallway one":
    print("As you walk down the eerie hallway, you realize that you can enter three rooms.")
    firstroom = input("Which do you choose to enter first?")
    if firstroom == "room one":
        if firstroom == "room one":
            print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {frog}")
            pickup = input("Do you want to pick the item up, if you believe it is the required item?")
            if pickup == "yes":
                if obj == "frog":
                    print("Congratulations, you have won the game.")
                    quit()
    if firstroom == "room two":
        print(f"This room appears to be a master bedroom, unoccupied for a while now. After searching, you find an old {necklace}")
        pickup = input("Do you want to pick the item up, if you believe it is the required item?")
        if pickup == "yes":
            if obj == "necklace":
                print("Congratulations, you have won the game.")
                quit()
        else:
            if o
    if firstroom == "room three":
        print(f"This room is clearly the living room. You find a {tophat}")
        pickup = input("Do you want to pick the item up, if you believe it is the required item?")
        if pickup == "yes":
            if obj == "tophat":
                print("Congratulations, you have won the game.")
                quit()
if firsthallway == "hallway two":
    print("As you walk down the colorful hallway that reminds you of candyland, you realize you can enter three rooms.")
    firstroom = input("Which do you choose to enter first?")
    if firstroom == "room one":
        print(f"This is the bathroom. You somehow find a {crown} belonging to King Michael Whalen the First.")
        pickup = input("Do you want to pick the item up, if you believe it is the required item?")
        if pickup == "yes":
            if obj == "crown":
                print("Congratulations, you have won the game.")
                quit()
         
                
            	           

