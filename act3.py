class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
a=parrot("Grey parrot",12)
b=parrot("Buderiger",24)
print("Grey parrot is a ",a.species)
print("Buderiger parrot is a",b.species)
print("Age of grey parrot is",a.age)
print("Age of buderiger parrot is",b.age)
