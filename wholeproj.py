import random
from roomclass import *
from userclass import *
#from theobjclasscode import *
name = input("Choose your character's name.")
user1 = player(name, []) #check this

# testing to see if the new code works here, not actual game
print(("You were strolling on a walk with your grandmother when suddenly a rainbow van with frogs blocks your path."))
print("You blink for one second, and suddenly, your grandmother is gone.")
print("You begin to panic frantically, and try to remember a minor detail from the van...(press enter to continue)")
a = input("Thinking...")
print("The one thing you were able to recall was the name printed on the van: Evil King M the third")
print("Your enter the name into your phone and recieved coordinates of the mansion")
print("You type the coordinates into google maps and follow the directions")
print("Suspiciously and carefully, you stumble into the mansion in the middle of an enigmatic forest, desperate to return your grandma to her retirement home")
print("Suddenly, a mysterious figure appears from the shadows.")
a = input("'Hello, my name is King M the Third. Would you like to play a game young one? If you win, you get your grandma back.' (yes or no)")
if a == "yes":
    import random
    obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'tophat', 'necklace', 'crown' ])
    print(f"You are required to find {obj} within the house. Good luck.")
    print("Before long, the mansion comes into sight. The door is unlocked.")
    n = toNum(input("what hallway do you want to travel down?"))
    rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
    #print(n)
    #print(rchoice)
    allrooms[n -1][rchoice -1].message()


if a == "no":
    print("Then I guess you won't be getting your grandma back.")
    print("There is an ominous, final silence.")
    exit()




