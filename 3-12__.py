class vehicle:
    def start(self):
        print("engine is running")
    def stop(self):
        print("car stop running")
class Bike(vehicle):
    def bike_start(self):
         print("bike is started....")
class Car(vehicle):
    def car_start(self):
         print("car is started....")

hero = Bike()
hero.start()
hero.bike_start()
hero = Car()
hero.start()
hero.car_start()



class animal:
    def speak(self):
        return " some sound "
        
class cat(animal):
    def speak(self):   # overriding 
        return "meow"
c=cat()
print(c.speak())


