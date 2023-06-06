class Animal():

    def __init__(self,color):
       self.color = color

    def animalColor(self):
        print("Animal color: ",self.color)
    def sleep(self):
        print("Animal sleeps during daytime")
    def eat(self):
        print("Animal eats both grace and meat.")
    def height(self):
        print("Animal has several heights.")

class Dog(Animal):
   
    def __init__(self, color,gender):
       super().__init__(color)
       self.gender =gender

    def dogColor(self):
        print("The color of the dog is : ", self.color)
    def dogGender(self):
        print("It is a {} dog".format(self.gender))

class Horse(Animal):
    def __init__(self, color,types):
        super().__init__(color)
        self.types=types

    def horseTypes(self):
        print("Its a/an {} type horse".format(self.types))
    def sleep(self):
        print("Horse sleeps standing.")

class Snake(Animal):
    def __init__(self, species):
        super().__init__(species)
        
dog1 =Dog("Brown","Male")
dog1.dogColor()
dog1.dogGender()
dog1.sleep()

horse1 = Horse("Black","Arabian")
horse1.horseTypes()
horse1.sleep()