# Demonstrating polymorphism with different vehicle types
class Vehicle:
    def move(self):
        pass  # Base method, will be overridden by subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create instances
car = Car()
plane = Plane()
boat = Boat()

# Call move on each
car.move()    # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
boat.move()   # Output: Sailing 🚤
