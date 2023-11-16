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


firsthallway = input("There are three hallways to walk down.  Which do you choose?")

if firsthallway == "hallway one":
    print("As you walk down the eerie hallway, you realize that you can enter three rooms.")
    firstroom = input("Which do you choose to enter first?")
    if firstroom == "room one":
        print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {frog}")
        pickup = input(print("Do you want to pick the frog up, if you believe it is the required item?"))
        #if pickup == "yes":






