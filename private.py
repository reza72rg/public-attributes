class Demo:
    def __init__(self):
        """
        Initialize a Demo object with attributes a, _b, and c.
        """
        self.a = 1  # Public attribute
        self._b = 2  # Protected attribute
        self.c = 3  # Public attribute (changed from __c to c)

obj = Demo()

# Access and print the values of the attributes
print(obj.a)  # Output: 1
print(obj._b)  # Output: 2
print(obj.c)  # Output: 3 (changed from __c to c)
