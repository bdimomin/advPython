class Vehicle():
    def __init__(self,name,speed,mileage):
        self.name =name
        self.speed=speed
        self.mileage =mileage

    def details(self) :
        return f"Vehical Name: {self.name}, Speed: {self.speed}, Mileage:{self.mileage}"

class Bus(Vehicle):
    
   pass
      
    
bus1 = Bus("School Volbo",180,12)
print(bus1.details())