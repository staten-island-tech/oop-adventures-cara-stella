import random

def choosing():
        global obj
        obj = random.choice(['vase', 'book', 'frog', 'umbrella', 'spatula', 'briefcase', 'tophat', 'necklace', 'crown'])
        print(f"You are required to find {obj} within the house. Good luck.")

from userclass import *
class Room():
        def __init__(self, hallway):
                self.hallway = hallway
class Room_one(Room):
        def __init__(self,  hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"You search through the room, quickly realizing it is a kitchen. Somehow, you find a {self.item}")
                pick_up(self.item)
                
room_one_one = Room_one(1, item = "frog") # i added the item = but lets see if it works

room_two_one = Room_one(1, item = "spatula")
#print(room_two_one.item)
room_three_one = Room_one(1, item = "book")
#item = "frog"
#hallway = 1
#room_one = Room_one(1, ["frog", "spatula", "book"]) # replace spatula in second hallway room one
#room_one.message(item, hallway)

roomsone = [Room_one(1, item = "frog"), Room_one(1, item = "spatula"), Room_one(1, item = "book")]
Room_one_one = Room_one(1, item = "frog")

class Room_two(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"You hesitantly open the door, to find a master bedroom. With a few minutes of searching you find an {self.item}")
                #coin in hallway thing goes here
                pick_up(self.item)
            
                        
#item = "necklace"
#hallway = 1
#room_two = Room_two(2, [1, 2, 3], ["necklace", "briefcase", "crown"])
#room_two.message(item, hallway)


roomstwo = [Room_two(2, item = 'necklace'), Room_two(2, item = "briefcase"), Room_two(2, item = "crown")]
class Room_three(Room):
        def __init__(self, hallway, item):
                super().__init__(hallway)
                self.item = item
        def message(self):
                print(f"This is obviously the bathroom, and an elaborate one at that. You find {self.item}")
                
                #pickup = input("Do you want to pick the item up, if you believe it is the required item? this will repeat, please repeat answer")
                #if pickup == "yes":
                        #print("Congratulations, you have won the game.")
                pick_up(self.item)
#item = "tophat"
#hallway = 1
#room_three = Room_three(3, [1, 2, 3], ["tophat", "vase", "unbrella"])
#room_two.message(item, hallway)


roomsthree = [Room_three(3, item = 'tophat'), Room_three(3, item = "vase"), Room_three(3, item = "umbrella")]
allrooms = [roomsone, roomstwo, roomsthree]
itemlist = []
# the problem is that the variable "item" below is not defined. How do I make self.item be recognized?
def toNum(inp):
        r = 0
        if inp == "one":
                r = 1
        elif inp == "two":
                r = 2
        elif inp == "three":
                r = 3
        return r

def room_choice():
        hchoice = toNum(input("what hallway do you want to travel down?  One, two, or three?"))
        if hchoice not in [1,2,3]:
                print("Too many errors. Game has ended.")
                quit()
        else:
                rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
                allrooms[hchoice -1][rchoice -1].message()


def pick_up(item):
    pick_up = input("If you believe this is the required item, will you pick it up?")
    if pick_up == "yes":
        #print(item, obj)  # checking
        if item == obj:
            print("You have found the item, congratulations.")
            item_found()
        else:
            print("You have lost. The game has ended.")
        exit()
    elif pick_up == "no":
        c = input("Would you like to travel down a different hallway? If no, you will stay in the current hallway and pick a different room.")
        if c == "yes":
            global hchoice
            hchoice = toNum(input("Choose a different hallway to travel down."))
            if hchoice not in [1, 2, 3]:
                print("Error, please pick an actual hallway.")  
                pick_up(item)
            #global rchoice
            rchoice = toNum(input("Choose a room - one, two, or three. Remember you may have already traveled inside some."))
            allrooms[hchoice - 1][rchoice - 1].message()
        #testing for the c == "no"
        elif c == "no":
            print(f"{user} chooses to stay in the same hallway.")
            rchoice = toNum(input("Choose a room - one, two, or three. Remember you may have already traveled inside some."))
            allrooms[hchoice -1][rchoice -1].message()
          
#COIN CODE 
total_coins = 0 #wip

def item_found():
        print(f"Sighing with relief, {user} brings the item outside. Minus is waiting expectantly for them.")
        print("They hear a familiar voice yell their name and turn to see their grandmother, unharmed..for now.")
        print("'Not so fast,' Minus says, and a spherical green forcefield surrounds your grandmother. 'You think I'd give up this easily?'")
        global fightforg1
        fightforg1 = input("Overcome with anger, do you... a) attempt to attack him or b) take leave, fearing for your own life? Enter 'a' or 'b'")
        if fightforg1 == "a":
                murder()
        if fightforg1 == "b":
               print("You run from the forest, leaving your grandmother behind to die.")
               quit()
        
class weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

rock = weapon("rock", 5)
rope = weapon("rope", 10)
crowbar = weapon("crowbar", 30)
magical_wand = weapon("magical wand", 100)

class enemyweapon():
        def __init__(self, evilname, evildamage):
                self.evilname = evilname
                self.evildamage = evildamage

m_wand = enemyweapon("m wand", 50)

     
    #hchoice = toNum(input("What hallway do you want to travel down? One, two, or three?"))
    #if hchoice != "one" or hchoice != "two" or hchoice != "three":
    #    print("Error, please pick an actual hallway.") #check this
    #    pick_up()
    #rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
    #print(n)
    #print(rchoice)
    #allrooms[hchoice -1][rchoice -1].message()

class player:
    def __init__(self, name, health):
        self.name = name
        self.inventory = []
        self.health = health

    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def attack(self, weapon): 
        King_M.health -= weapon.damage
        print(f"You have successfully attacked the King! King Minus' health has been lowered to {King_M.health}.")




def murder():
        #comp picks random number - (1-30 = rock, 30-60 = rope, 60-90 = crowbar, 90-100 = magical wand)
        print("Your bravery is commended by the Gods! You have earned one gold coin.")
        global total_coins
        total_coins += 1
        print(f"Your total number of coins is {total_coins}.")
        print(f"{user} looks around desperately for anything to use as a weapon. They hears a voice from Heaven:  I AM ZEUS, HEAR ME NOW. I HAVE SELECTED A RANDOM WEAPON FOR YOU.")
        weapon_number = random.randint(1, 100)
        if 1<= weapon_number <= 30:
                print("You have a rock.")
                #separate function for rock fight
                player1.attack(rock)
                print("Ah...looks like luck wasn't in your favor. It doesn't look like you can win this by fighting.")
                i = input("Do you choose to continue fighting, a,  or use persuasion tactics, b?")
                if i == "a":
                        player_death()
                if i == "b":
                       print(f"{user} suddenly comes up with an idea.")
                       print("'Uh - sir,' you say, 'Did you know that in some areas, people eat frog legs?")
                       print("He looks horrified and drops his wand. 'WHAT?!'")
                       print("After telling him about said food, he forgets all about tormenting your life.")
                       print("He vanishes, muttering bloody murder.")
        
        if 31<= weapon_number <= 60:
               print("You have a rope.")
                #separate function for rope fight
               player1.attack(rope)
               fcr()
        if 61<= weapon_number <= 90:
               print("You have a crowbar!")
                #separate function for crowbar fight
               player1.attack(crowbar)
               fcc()
        if 91 <= weapon_number <= 100:
               print("Holy moly, you beat the odds! You get a gold coin and a magical wand.")
               total_coins += 1
               print(f"Your total number of coins is now {total_coins}.")
               player1.attack(magical_wand)
               successful()
               
        #else:
        #       print("my error")
        #       quit()


def fcr():
       print("The rope slashed him across the face, and he fell, landing backwards.")
       print("From his shock, the forcefield broke - and your grandmother quickly began running.")
       print("He seems disoriented. Maybe you gave him a concussion?")
       print("You run quickly after her.")

def m_attack2():
        global dodge
        dodge = random.randint(1, 10)
        if 1<= dodge <= 5: #is there a better way to organize this
                print(f"{user} is unable to dodge the firebeam and is hit directly in the chest. This severely decreases their health...")
                player1.health -= m_wand.evildamage #MAKE SURE THIS WORKS
                print(f"{user} health has decreased to {player1.health}")
                print(f"Adrenaline surging, {user} manages one more heavy hit-")
                player1.attack(magical_wand)
                successful()
        if 6 <= dodge <= 10:
               print(f"{user} successfully dodges and rolls to their feet.  They whirl around and prepare to attack again.")
               player1.attack(crowbar)
               print(f"Adrenaline surging, {user} manages one more heavy hit-")
               player1.attack(magical_wand)
               successful()
def fcc():
        print("You've gotten a powerful hit in, but M has become far angrier.")
        m_attack2()


def successful():
        print(f"Sighing with relief, {user} stares at the fallen body. Their grandmother is released from her prison and they hug her in relief.")
        print("What a wild day.")

def player_death():
       print("That wasn't very effective...")
       print("He stares at you with an amused expression before casting a spell on you with his wand-")
       print("You are now helplessly in pain - as if you were brutally stung by millions of angry wasps.")
       print("You slowly and painfully begin to pass away. King Minus viciously laughs as you leave the mortal life.")
       print("Thanks so much for participating and playing our preppy game. Hope you enjoyed !!")
       #written by stella



#import random
#from roomclass import *
#from userclass import *
#from theobjclasscode import *
global user

user = input("Choose your character's name.")

player1 = player(user, 100) #make sure this works

#name = player(user, []) #check this
# testing to see if the new code works here, not actual game
print(f"{user} was strolling on a walk with their grandmother when suddenly a rainbow van with frogs blocks your path.")
print(f"{user} blinks for one second, and suddenly, their grandmother is gone.")
print("They begin to panic frantically, and try to remember a minor detail from the van...")
#a = input("Thinking...")
print(f"The one thing {user} was able to recall was the name printed on the van: 'Evil King Minus the third'")
print("They enter the name into their phone and recieved coordinates of the mansion")
print("They type the coordinates into google maps and follow the directions")
print(f"Suspiciously and carefully, {user} stumbled into the mansion in the middle of an enigmatic forest, desperate to return their grandma to her retirement home")
print("Suddenly, a mysterious figure appears from the shadows.")
a = input("'Hello, my name is King Minus the Third. Would you like to play a game young one? If you win, you get your grandma back. Hehehe' (yes or no)")
if a == "yes":
    import random
    obj = random.choice(['vase','book','frog', 'umbrella','spatula', 'briefcase', 'tophat', 'necklace', 'crown' ]) #earlier copies had " briefcase"
    print(f"You are required to find {obj} within the house. Good luck.")
    print("Before long, the mansion comes into sight. The door is unlocked.")
    hchoice = toNum(input("what hallway do you want to travel down? Type one, two, or three?")) #originally letters not num
    if hchoice not in [1, 2, 3]:
                print("Error, please pick an actual hallway.") #check this
                print (hchoice)
                room_choice()
    elif hchoice in [1, 2, 3]:
        #another toNum = and (
                rchoice = toNum(input(("Choose a room - one, two, or three. Remember you may have already travelled inside some.")))
        #print(hchoice)
        #print(rchoice)
                allrooms[hchoice -1][rchoice -1].message()
    else:
           print("my error")
           print(hchoice)

def m_attack():
        global dodge
        dodge = random.randint(1, 10)
        if 1<= dodge <= 5: #is there a better way to organize this
                print(f"{user} is unable to dodge the firebeam and is hit directly in the chest. This severely decreases their health...")
                player1.health -= m_wand.evildamage #MAKE SURE THIS WORKS
                print(f"{user} health has decreased to {player.health}")
        if 6 <= dodge <= 10:
               print(f"{user} successfully dodges and rolls to their feet.  They whirl around and prepare to attack again.")
               current_weapon = weapon
               player1.attack(current_weapon) #check this too
#CHANGING PLAYER TO PLAYER 1?? "probably"


King_M = enemy("King Minus", 100)


        

if a == "no":
    print("'Then I guess you won't be getting your grandma back.'")
    print("There is an ominous, final silence.")
    exit()
            
class player:
    def __init__(self, name, health):
        self.name = name
        self.inventory = []
        self.health = health

    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def attack(self, weapon): 
        King_M.health -= weapon.damage
        print(f"You have successfully attacked the King! King Minus' health has been lowered to {King_M.health}.")


player1 = player(user, 100) #make sure this works

class enemy():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack_player(self, m_wand):
        print("King Minus uses his magical wand and readies an attack...")
        m_attack()





