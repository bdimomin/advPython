from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):

    def noofsides(self):
        print("I have 6 sides")

three = Triangle()
three.noofsides()

four = Quadrilateral()
four.noofsides()

five = Pentagon()
five.noofsides()

six = Hexagon()
six.noofsides()