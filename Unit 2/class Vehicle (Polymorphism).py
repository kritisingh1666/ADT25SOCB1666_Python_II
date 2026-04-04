# Create a base class Vehicle and a method move() and two subclasses Car and Bicycle
# Override the move() method in both subclasses. 
# The Car should print "Driving on the road" and the Bicycle should print "Pedaling on the road"
# Demonstrate polymorphism by calling the move() method on both objects

class Vehicle:
    def Move(self):
          return "The vehicle is moving"
    
class Car(Vehicle):
    def Move(self):
         return "Driving on the road"

class Bicycle(Vehicle):
    def Move(self):
         return "Pedaling on the road" 

c = Car()
b = Bicycle()

print("The car is", c.Move())
print("The bicycle is", b.Move())

     
    
    
