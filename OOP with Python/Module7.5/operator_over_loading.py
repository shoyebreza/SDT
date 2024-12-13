class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the '+' operator
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Using the overloaded '+' operator
c1 = Complex(1.2, 3.4)
c2 = Complex(5.6, 7.8)

result = c1 + c2
print(result)  # Output: 6.8 + 11.2i
