class Vehicle():
    fare =100
    def __init__(self,seatingCapacity):
        self.seatingCapacity=seatingCapacity

    def fareCalculation(self):
        return f"Fare is : {self.seatingCapacity*self.fare}"


class Bus(Vehicle):
    fare = 110
    

vehicle1 = Vehicle(40)
bus1 = Bus(40)
print(vehicle1.fareCalculation())
print(bus1.fareCalculation())