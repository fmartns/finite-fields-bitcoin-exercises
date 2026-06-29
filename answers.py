"""Reference answers for the exercises.

Look at these only after you have tried on your own. Copy a snippet into the
matching notebook cell, or read through to check your logic.
"""

# Exercise 1

def clock_add(hour, delta, modulo=12):
    return (hour + delta) % modulo


# Exercise 2

def __eq__(self, other):
    return self.num == other.num and self.prime == other.prime


def __ne__(self, other):
    return self.num != other.num or self.prime != other.prime


# Exercise 3 

def __init__(self, num, prime):
    if not (num >= 0 and num < prime):
        raise ValueError(f"Num {num} not in field range 0 to {prime - 1}")
    self.num = num
    self.prime = prime


# Exercise 4 

def __add__(self, other):
    return self.__class__((self.num + other.num) % self.prime, self.prime)


# Exercise 5 

def __sub__(self, other):
    return self.__class__((self.num - other.num) % self.prime, self.prime)


# Exercise 6 

def __mul__(self, other):
    return self.__class__((self.num * other.num) % self.prime, self.prime)


# Exercise 7 

def __pow__(self, exponent):
    return self.__class__(pow(self.num, exponent, self.prime), self.prime)


# Exercise 8 

def __truediv__(self, other):
    if other.num == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return self * (other ** (self.prime - 2))


# Exercise 9 

def multiplicative_inverse(n, prime):
    return pow(n, prime - 2, prime)


# Exercise 10 

def assert_fermat_holds(prime):
    for n in range(1, prime):
        assert pow(n, prime - 1, prime) == 1
