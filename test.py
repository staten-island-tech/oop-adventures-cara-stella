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
firstroom()