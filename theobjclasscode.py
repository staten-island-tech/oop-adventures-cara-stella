# vase, briefcase,book,spatula, frog,crown,tophat,necklace,umbrella
class obj():
    def __init__(self,color, size, charecteristic):
        self.color = color
        self.size = size
        self.charecteristic = charecteristic
# do we use this???
Vase = obj("blue", "medium size","floral design")
print(Vase.color, Vase.size, Vase.charecteristic)
Briefcase = obj("black","small size","leather material")
print(Briefcase.color, Briefcase.size, Briefcase.charecteristic)
Book = obj("red", "small size", "title is magic school")
print(Book.color, Book.size, Book.charecteristic)
Spatula = obj( "blue", "small size", "greasy")
print(Spatula.color, Spatula.size,Spatula.charecteristic)
Frog = obj("green", "small size", "spotted")
print(Frog.color, Frog.size, Frog.charecteristic)
Crown = obj( "gold","medium size", "has red and green gems belonging to King Whalen the second")
print(Crown.color, Crown.size, Crown.charecteristic)
Tophat = obj( "black", "medium size", "has a velvet strip around")
print(Tophat.color, Tophat.size, Tophat.charecteristic)
Necklace = obj("silver", "small size","has charms that symbolize family members")
print(Necklace.color, Necklace.size, Necklace.charecteristic)
Umbrella =  obj( "pink","large size","the interior of the umbrella is a sunset")
print(Umbrella.color, Umbrella.size, Umbrella.charecteristic)


