class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.name=name
    def seating_capacity(self,capacity):
        return "capicity is "+str(capacity)
class Bus(Vehicle):
    # def __init__(self,name,max_speed,mileage,seating_capacity=50):
    #     super().__init__(name,max_speed,mileage)
    #     self.seating_capacity=seating_capacity
    def seating_capacity(self,capacity=50):
        return "capacity is "+str(capacity)

car=Vehicle("car",80,20)

print(car.seating_capacity(100))
bus=Bus("bus",20,10)
print(bus.seating_capacity())



