from abc import ABC,abstractmethod

class Bank(ABC):

    @abstractmethod
    def bankDetails():
        pass

    @abstractmethod
    def deposit():
        pass
    
    @abstractmethod
    def withdrew():
        pass

    @abstractmethod
    def balance():
        pass

class BankStatement(Bank):

    def __init__(self,name,acc,contact,dep_amount,with_amount):
        self.name = name
        self.acc =acc
        self.contact =contact
        self.dep_amount=dep_amount
        self.with_amount = with_amount

    def bankDetails(self):
        print("Name: {}, Account: {}, Contact: {}".format(self.name,self.acc, self.contact))
    
    def deposit(self):
        print("{} is deposited successfully.".format(self.dep_amount))
    
    def withdrew(self):
        print("{} is withdrew successfully.".format(self.with_amount))

    def balance(self):
        print("Current balance is : {}".format(self.dep_amount-self.with_amount))



bank1 = BankStatement("ABC","178.56.80.9825","01711111111",50000,10000)
bank1.bankDetails()
bank1.deposit()
bank1.withdrew()
bank1.balance()