# vase, briefcase,book,spatula, frog,crown,tophat,necklace,umbrella 
class obj():
    def __init__(self,color, size ):
        self.color = color
        self.size = size

class vase(obj):
    def __init__(self, color, size, design):
        super().__init__(color, size)
        self.design = design
        def __str__(self):
            return f"{self.color},{self.size}, {self.design}"

class briefcase(obj):
    def __init__(self, color, size, material):
        super().__init__(color, size)
        self.material = material
        def __str__(self):
            return f"{self.color},{self.size}, {self.material}"
class book(obj):
    def __init__(self, color, size,title,author):
        super().__init__(color, size)
        self.title = title
        self.author = author
        def __str__(self):
            return f"{self.color},{self.size}, {self.title},{self.author}"
class spatula(obj):
    def __init__(self, color, size, shape):
        super().__init__(color, size)
        self.shape = shape
        def __str__(self):
            return f"{self.color},{self.size}, {self.shape}"
class frog(obj):
    def __init__(self, color, size, animal):
        super().__init__(color, size)
        self.animal = animal
        def __str__(self):
            return f"{self.color},{self.size}, {self.animal}"
class crown(obj):
    def __init__(self, color, size, luster):
        super().__init__(color, size)
        self.luster = luster
        def __str__(self):
            return f"{self.color},{self.size}, {self.luster}"
class tophat(briefcase):
    def __init__(self, color, size, material):
        super().__init__(color, size, material)
        def __str__(self):
            return f"{self.color},{self.size}, {self.material}"
class necklace(crown):
    def __init__(self, color, size, luster):
        super().__init__(color, size, luster)
        def __str__(self):
            return f"{self.color},{self.size}, {self.luster}"
class umbrella(vase):
    def __init__(self, color, size, design):
        super().__init__(color, size, design)
        def __str__(self):
            return f"{self.color},{self.size}, {self.design}"

