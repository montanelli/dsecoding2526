"""object oriented programming"""

# A program is made up of one or more objects working together - objects make use of each other’s capabilities
# An Object is a bit of self-contained Data (properties) and Code (methods)
# A key aspect of the Object approach is to break the problem into smaller understandable parts
# We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects...
# Class - a template
# Method or Message - A defined capability of a class (portion of code, function)
# Field or attribute or property - A bit of data in a class
# Object or Instance - A particular instance of a class

import sys


class Vehicle:
    wheels = None
    brand = None
    model = None
    color = None
    engineSize = None
    registrationPlate = None
    fuel = None

    # initializer / instance attributes
    # When the object is constructed, the __init__ method is called to allocate and initialize the attributes that require to receive a value to create a proper instance of the class
    # the self parameter is specified to refer to the instance on which the method has to be applied.
    def __init__(self, brand, model, color, engineSize):
        self.brand = brand
        self.model = model
        self.color = color
        self.engineSize = engineSize

    # method 1: show description
    def showDescription(self):
        if self.registrationPlate is not None:
            print(
                f"the vehicle with plate {self.registrationPlate} is a",
                self.color,
                self.brand,
                self.model,
            )
        else:
            print("this vehicle is a", self.color, self.brand, self.model)

    # method 2: change the vehicle color
    def changeColor(self, newcolor):
        self.color = newcolor

    # method 3: set the plate
    def registerPlate(self, newPlate):
        self.registrationPlate = newPlate

    # method 4: specify the fuel
    def setFuel(self, newfuel):
        fuels = ["gas", "diesel", "petrol", "hybrid", "electric"]

        if newfuel in fuels:
            self.fuel = newfuel

    def printFuel(self):
        if self.registrationPlate is not None:
            print(f"the fuel of vehicle {self.registrationPlate} is", self.fuel)
        else:
            print("the fuel of the vehicle is", self.fuel)

    def printWheels(self):
        if self.wheels is None:
            print(f"I do not know how many wheels are set for this vehicle")
        elif self.registrationPlate is not None:
            print(f"the vehicle {self.registrationPlate} has {self.wheels} wheels")
        else:
            print(f"this vehicle has {self.wheels} wheels")

    # When the object is destroyed, the __del__ method is called to de-allocate the memory assigned to the object
    def __del__(self):
        if self.registrationPlate is None:
            print("I destroyed", self.color, self.brand, self.model)
        else:
            print(
                f"I destroyed the {self.color} {self.brand} {self.model} with plate {self.registrationPlate}"
            )


# inheritance
# When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
# Write once - reuse many times
# The new class (child) has all the capabilities of the old class (parent) - and then some more
# ‘Subclasses’ are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.
class Car(Vehicle):

    # class attribute
    wheels = 4
    parkAssist = None

    def hasParkAssist(self, parkAssist):
        if parkAssist:
            self.parkAssist = True
        else:
            self.parkAssist = False


class Truck(Vehicle):
    wheels = 6
    fuel = "diesel"


class Motorcycle(Vehicle):
    wheels = 2


# main code

mycar = Vehicle("Volkswagen", "Golf", "Black", 2000)
mycar.registerPlate("GH 463 DD")

mycar.showDescription()

mycar.changeColor("Red")
mycar.setFuel("electric")

mycar.showDescription()
mycar.printFuel()

mycar.setFuel("water")
mycar.printFuel()

# mycar = "I'm a bike"
print(isinstance(mycar, Vehicle))

mycar.printWheels()

mycar2 = Car("BMW", "X5", "Purple", 2500)
mycar2.printWheels()

mycar2.hasParkAssist(True)

# the method hasParkAssist (defined in the Car class) is not available on object of the superclass Vehicle
# mycar.hasParkAssist(True)

print(isinstance(mycar2, Vehicle))
print(isinstance(mycar, Car))

sys.exit()
