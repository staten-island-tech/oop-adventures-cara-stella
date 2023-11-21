import random 

print(" Find the object in one of the three rooms of the selected hallway. ")
obj = ['vase','book','frog', 'umbrella','spatula', ' breifcase', 'top hat', 'necklace', 'crown' ]
r = (random.shuffle(obj))
print(*obj)

input(' ')

if r == "None":
    print("Game over ")
    quit()