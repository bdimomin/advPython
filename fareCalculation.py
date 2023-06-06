class Vehicle():
    
    def __init__(self,seatingCapacity):
        self.seatingCapacity=seatingCapacity

    def fareCalculation(self):
        return f"Vehicle Fare is : {self.seatingCapacity*100}"


class Bus(Vehicle):
    def __init__(self, seatingCapacity):
        super().__init__(seatingCapacity)
    def fareCalculation(self):
        return f"BUS Fare is : {self.seatingCapacity*110}"
    

vehicle1 = Vehicle(50)
bus1 = Bus(50)
print(vehicle1.fareCalculation())
print(bus1.fareCalculation())