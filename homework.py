class Dog:
    species = "Dog"    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
d1 = Dog("Labrador", "Buddy")
d2 = Dog("Shepherd", "Max")
print(d1.name, d1.breed, Dog.species)
print(d2.name, d2.breed, Dog.species)
