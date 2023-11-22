import random 

obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'top hat', 'necklace', 'crown' ])
print(f"You are required to find {obj} within the house. Good luck.")

#object class
#vase = "vase"
#book = "book"
#frog = "frog"
#umbrella = "umbrella"
#spatula = "spatula"
#briefcase = 'briefcase'
#tophat = "tophat"
#necklace = "necklace"
#crown = "crown"
  

# hallway class?
def secondhallway():
    print("As you walk down the colorful hallway that reminds you of candyland, you realize you can enter three rooms.")
    firstroom = input("Which do you choose to enter first?")
    if firstroom == "room one":
        x = "crown"
        roomone()
        return x
    if firstroom == "room two":
        b = "book"
        roomtwo()
        return b
    if firstroom == "room three":
        y = "vase"
        roomthree()
        return y
# rooms class
# add var in ()?
def roomthree():
            print(f"You search through the room and find a {y}")
            pickup = input("Do you want to pick the item up, if you believe it is the required item?")
            if pickup != "yes":
                print("Move to the next hallway: hallway two.")
                secondhallway()
            if pickup == "yes":
                if obj == y:
                    print("Congratulations, you have won the game.")
                    quit()
                if obj != x:
                     print("You lost. Womp womppp")
def roomtwo():
            print(f"You search through the room and find a {b}")
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



firsthallway = input("There are three hallways to walk down.  Which do you choose? (hallway one, two, or three)")

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
        x = "crown"
        roomone()
    if firstroom == "room two":
        b = "book"
        roomtwo()
    if firstroom == "room three":
         y = "vase"
         roomthree()
if firsthallway == "hallway three":
     print("This hallway is surpisingly normal, nothing out of the ordinary or especially creative. You know this one, like the others, has three rooms.")
     firstroom = input("Which do you choose to enter first?")
     if firstroom == "room one":
          x = "umbrella"
          roomone()
     if firstroom == "room two":
          b = "spatula"
     if firstroom == "room three":
          y = "briefcase"
        