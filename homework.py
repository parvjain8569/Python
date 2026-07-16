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



class Dog:
    def make_sound(self):
        print("bark")

class Cat:
    def make_sound(self):
        print("Meow")

class Cow:
    def make_sound(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()




class PrivateExample:
    def __init__(self):
        self.public_var = "I am public"
        self.__private_var = "I am private"

    def get_private(self):
        return self.__private_var

obj = PrivateExample()
print(obj.public_var)
print(obj.get_private())





class Car:
    wheels = 4  

    def __init__(self, color):
        self.color = color  

car1 = Car("Red")
car2 = Car("Blue")

Car.wheels = 5 

print(car1.wheels)
print(Car.wheels)






class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  
        return self.width * self.height

s = Shape()
r = Rectangle(5, 10)

print(s.area())
print(r.area())