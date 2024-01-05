import random
from roomclass import *
from userclass import *
#from theobjclasscode import *
user = input("Choose your character's name.")
#name = player(user, []) #check this

print(f"{user} was strolling on a walk with their grandmother when suddenly a rainbow van with frogs blocks their path.")
print(f"{user} blinks for one second, and suddenly, their grandmother is gone.")
print("They begin to panic frantically, and try to remember a minor detail from the van...")
print("The rainbow and frogs were odd, but any specific words?")
#a = input("[Write 'Evil King M the third']")
#if a == 'Evil King M the third':
print(f"The one thing {user} was able to recall was the name printed on the van: Evil King M the third")
print("They enter the name into their phone and recieved coordinates of the mansion")
print("They type the coordinates into google maps and follow the directions")
print("Suspiciously and carefully, you stumble into the mansion in the middle of an enigmatic forest, desperate to return your grandma to her retirement home")
print("Suddenly, a mysterious figure appears from the shadows.")
#b = input(f"{user} stumbles back in shock, heart beating rapidly in their chest. They need a minute...")
a = input("'Hello, my name is King M the Third. Would you like to play a game young one? If you win, you get your grandma back.' (yes or no)")
if a == "yes":
    import random
    #obj = random.choice(['vase','book','frog','umbrella','spatula','briefcase','tophat','necklace','crown'])
    #print(f"You are required to find {obj} within the house. Good luck.")
    choosing()
    print("Before long, the mansion comes into sight. The door is unlocked.")
    # toNum was b/w = and (input
    hchoice = int(input("what hallway do you want to travel down? 1, 2, or 3?")) #originally letters not num
    if hchoice != "1" or hchoice != "2" or hchoice != "3":
        print("Error, please pick an actual hallway.") #check this
        print (hchoice)
        room_choice()
    elif hchoice == "1" or hchoice == "2" or hchoice == "3":
        #another toNum = and (
        rchoice = int(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
    #print(n)
    #print(rchoice)
        allrooms[hchoice -1][rchoice -1].message()


        

if a == "no":
    print("Then I guess you won't be getting your grandma back.")
    print("There is an ominous, final silence.")
    exit()




