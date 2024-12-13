class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    # Overriding the `sound` method
    def sound(self):
        return "Bark"

class Cat(Animal):
    # Overriding the `sound` method
    def sound(self):
        return "Meow"


# Using method overriding
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
