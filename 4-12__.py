# class car:
#     def info(self):
#         print("is a car")

#     def start(self):
#         print("car is starting ")

#     def stop(self):
#         print("car is stoped ")


# class toyota:
#     def toy_info(self):
#         print("toyota car ")
#         super().start()
#         super().stop()

# class A():
# #  def _init_(self):
# #   pass
#  def sleep(sleep):
#      print("sleep fun")

# class B(A):
#     # def _init_(self):
#     #    super()._init_()
    
#     def display(self):
#         self.sleep()
#         print(issubclass(B,A))
        
# obj=B()
# obj.display() 




# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
        


class bankaccount():
    def __init__(self,acount_number,balance):
        self.acount_number=acount_number
        self.balance=balance 
    
    def deposite(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print(self.balance)
    def withdraw(self,amount):
        self.amount=amount
        self.balance=self.amount
        print(self.balance)


bank=bankaccount("694654",100)
bank.deposite(100)
bank.withdraw(100)


class Parent:
    def __init__(self):
        self.value = 10
    def display(self):
        print("Parent value:",self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = 20
    def show(self):
        print("Child value:",self.value)

obj = Child()
obj.display()
obj.show()    