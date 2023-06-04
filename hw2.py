class Vehicle():
    def __init__(self,seatingCapacity):
        self.seatingCapacity=seatingCapacity

    def fareCalculation(self):
        return f"Fare is : {self.seatingCapacity*100}"


class Bus(Vehicle):

    def __init__(self, seatingCapacity):
         super().__init__(seatingCapacity)
   
    def fareCalculation(self):
        return f"BUS Fare is : {(self.seatingCapacity*100)+(self.seatingCapacity*100)*.1}"
      
    
vehicle1 = Vehicle(40)
print(vehicle1.fareCalculation())

    
bus1 = Bus(40)
print(bus1.fareCalculation())