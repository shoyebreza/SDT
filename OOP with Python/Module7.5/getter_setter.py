class Person:
    def __init__(self, name, age):
        self._name = name    # Private-like attribute
        self._age = age      # Private-like attribute

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Name must contain only letters.")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value


# Using the class
person = Person("Alice", 25)

# Accessing attributes using getters
print(person.name)  # Output: Alice
print(person.age)   # Output: 25

# Modifying attributes using setters
person.name = "Bob"  # Works fine
print(person.name)   # Output: Bob

# method 2

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not value.isalpha():
            raise ValueError("Name must contain only letters.")
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value


# Using the class
person = Person("Alice", 25)
print(person.get_name())  # Output: Alice
person.set_name("Bob")    # Valid
print(person.get_name())  # Output: Bob
