# inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        return "Bark"

class Cat(Animal):  # Cat inherits from Animal
    def make_sound(self):
        return "Meow"


# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, dog.make_sound())  # Output: Buddy Bark
print(cat.name, cat.make_sound())  # Output: Whiskers Meow




# composition 

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started!"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Car "has-a" Engine

    def start_car(self):
        return f"{self.make} {self.model}: {self.engine.start()}"


# Using composition
engine = Engine(150)
car = Car("Toyota", "Corolla", engine)

print(car.start_car())  # Output: Toyota Corolla: Engine started!
