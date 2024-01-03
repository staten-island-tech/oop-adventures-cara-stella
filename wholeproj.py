import random
from roomclass import *
from userclass import *
#from theobjclasscode import *
user = input("Choose your character's name.")
#name = player(user, []) #check this
# testing to see if the new code works here, not actual game
print(f"{user} was strolling on a walk with their grandmother when suddenly a rainbow van with frogs blocks your path.")
print(f"{user} blinks for one second, and suddenly, their grandmother is gone.")
print("They begin to panic frantically, and try to remember a minor detail from the van...(press enter to continue)")
a = input("Thinking...")
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
    hchoice = toNum(input("what hallway do you want to travel down?"))
    rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
    #print(n)
    #print(rchoice)
    allrooms[hchoice -1][rchoice -1].message()


if a == "no":
    print("Then I guess you won't be getting your grandma back.")
    print("There is an ominous, final silence.")
    exit()




