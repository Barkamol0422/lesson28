class vehicle:
    def __init__(self, max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
a=vehicle(200,12)
print("The maximum speed of this car is", a.max_speed)
print("The mileage of this car is",a.mileage)
