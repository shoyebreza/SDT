""" Differences Between Class Methods and Static Methods
Aspect	Class Method	Static Method
Decorator Used	@classmethod	@staticmethod
Access to Class/Instance	Receives the cls parameter (class reference)	Does not receive self or cls; cannot access class/instance directly
Usage Purpose	Used when you need to work with the class itself (e.g., factory methods, modifying class state).	Used for utility or helper functions that do not depend on class/instance data.
Access to Class/Instance Variables	Can access and modify class variables via cls.	Cannot access or modify class/instance variables.
Examples
1. Class Method
 """
class MyClass:
    count = 0  # Class variable

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return f"Number of instances: {cls.count}"


# Creating instances
obj1 = MyClass()
obj2 = MyClass()

print(MyClass.get_count())  # Output: Number of instances: 2

""" Explanation:
    The get_count method is a class method that accesses and works with the class variable count.
    It uses the cls parameter to interact with class-level data.
2. Static Method """

class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Using the static method without creating an instance
print(MathUtils.add_numbers(5, 10))  # Output: 15

""" Explanation:
    The add_numbers method is a static method. It performs a utility task that doesn't require access to any class or instance data.
    It works independently of the class or its instances.
Combined Example """

class Example:
    class_variable = "Class Level Data"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def access_class_variable(cls):
        return f"Class Variable: {cls.class_variable}"

    @staticmethod
    def utility_function(a, b):
        return f"Sum: {a + b}"


# Using Class Method
print(Example.access_class_variable())  # Output: Class Variable: Class Level Data

# Using Static Method
print(Example.utility_function(10, 20))  # Output: Sum: 30

""" Key Notes:
    @classmethod works with class-level data (class_variable).
    @staticmethod works independently, purely as a utility function. """

