class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override eat method
    def eat(self):
        print('vegetables')

    # Implement exercise method
    def exercise(self):
        print('gym e poisa diya hudai gham jorai')

    # Overload '+' operator
    def __add__(self, other):
        return self.age + other.age
    
    # Overload '*' operator
    def __mul__(self, other):
        return self.weight * other.weight
    
    # Overload 'len()' function
    def __len__(self):
        return self.height
    
    # Overload '>' operator
    def __gt__(self, other):
        return self.age > other.age
    
    # Overload '<' operator (optional for clarity)
    def __lt__(self, other):
        return self.age < other.age


# Create instances
sakib = Cricketer('sakib', 38, 68, 91, 'BD')
mushi = Cricketer('mushi', 36, 65, 78, 'BD')
tamim = Cricketer('tamim', 34, 70, 85, 'BD')

# Using max with overloaded operators
players = [sakib, mushi, tamim]
oldest_player = max(players)  # Works because we overloaded '>' operator

print(f"The oldest player is {oldest_player.name}, aged {oldest_player.age}.")
