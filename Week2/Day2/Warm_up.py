class Plant():
    def __init__(self, type, size, is_blooming = False):
        self.type = type
        self.size = size
        self.is_blooming = is_blooming

    def grow(self):
        if self.size =="small":
            self.size ="medium"
        else:
            self.size ="large"

class Plan():
    def start_blooming(self):
        self.is_blooming = True

    def stop_blooming(self):
        self.is_blooming = False

    def status(self):
        print(f"Type: {self.type}, size: {self.size}, is_blooming: {self.is_blooming}")

my_plant = Plant("flower", "small")
my_plant.status()

my_plant =[Plant("rose", "small"),
           Plant("sunflower", "large"),
           Plant("cactus", "small", True),
           Plant("tulip", "medium"),
           Plant("orchid", "small", True), ]

for plant in my_plant:
    plant.grow()
    plant.bloom()
    plant.status()
my_plant[0].bloom()
