class Animal():
    def __init__(self,species):
       self.species = species

    def sleep(self):
        print("Animal sleeps during daytime")
    def eat(self):
        print("Animal eats both grace and meat")
    def height(self):
        print("Animal has several heights")

class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)
       
    def sleep(self):
        print("Cat sleeps during night time")
    def eat(self):
        print("Cat eats fish mostly")
    def height(self):
        print("Cat is lower in height")

class Snake(Animal):
    def __init__(self, species):
        super().__init__(species)
        
    def sleep(self):
        print("Snake sleeps during night time")
    def eat(self):
        print("Snake eats fish mostly")
    def height(self):
        print("Snake is lower in height")
    def feet(self):
        print("Snake has no foot")

class Horse(Animal):
    def __init__(self, species):
        super().__init__(species)

    def sleep(self):
        print("Horse sleeps standing.")
    def eat(self):
        print("Horse eats grace mostly.")
    def height(self):
        print("Horse is higher in height.")
    def feet(self):
        print("Horse has 4 foots")

cat1 =Cat("Mammal")
cat1.eat()