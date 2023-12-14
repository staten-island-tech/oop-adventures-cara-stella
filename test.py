import random
from roomclass import Room
from roomclass import Room_one
from roomclass import toNum
from roomclass import pick_up
# testing to see if the new code works here, not actual game
print("You were strolling on a walk with your grandmother when suddenly a rainbow van with frog blocks your path.")
print("You blink for one second, and suddenly, your grandmother is gone.")
print("You begin to panic frantically, and try to remember a minor detail from the van.")
print("The one thing you were able to recall was the name printed on the van: Evil King M the third")
print("Your enter the name into your phone and recieved coordinates of the mansion")
print("You type the coordinates into google maps and follow the directions")
print("Suspiciously and carefully, you stumble into the mansion in the middle of an enigmatic forest, desperate to return your grandma to her retirement home")
print("Suddenly, a mysterious figure appears from the shadows.")
a = input("'Hello, my name is King M the Third. Would you like to play a game young one? If you win, you get your grandma back.'") #press enter 
if a == "yes":
    import random
    obj = random.choice(['vase','book','frog', 'umbrella','spatula', ' briefcase', 'tophat', 'necklace', 'crown' ])
    print(f"You are required to find {obj} within the house. Good luck.")

    n = toNum(input("what hallway do you want to travel down?"))
    if n == 1: #type out "one"
        print 

        
#if a == "no":
 #   print("byebye grandma :)")
  #  exit()




