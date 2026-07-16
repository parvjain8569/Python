# error handeling 

# class balaanceError(Exception):
#     pass
# try:
#     balaance=5000
#     withdraw= int(input("enter the amount to withdraw "))

#     if withdraw>balaance:
#         raise balaanceError("insufficient balanace")
#     print("withdraw succesfuly ")

# except balaanceError as e:
#     print("custom error",e)

# except ValueError:
#     print("please enter a valid amount")

# finally:
#     print("thanks for using atm ")







class student:
    university="chitkara "
    def __init__(self,name,reg):
        self.name=name
        self.reg= reg
    def display(self):
        print(self.name,self.reg)


student1= student("parv",1319)  
print(student)
    