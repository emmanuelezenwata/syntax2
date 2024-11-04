class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overload the + operator for vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # Overload the * operator for scalar multiplication
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Creating two Vector instances
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using the overloaded + operator
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# Using the overloaded * operator
v4 = v1 * 3
print(v4)  # Output: Vector(6 19)
# comment Variable Assignment
#In Python, variables are assigned using the = operator.
age = 25                 # integer
name = "Alice"           # string
is_student = True        # boolean
#Indentation
#Python uses indentation (usually 4 spaces) to define code blocks.
def greet():
    print("Hello, World!")
    
greet()
#Data Types
#Common Python data types include lists, tuples, and dictionaries.
#List: An ordered, mutable collection.
fruits = ["apple", "banana", "cherry"]
#Tuple: An ordered, immutable collection.
coordinates = (10.0, 20.5)
#Dictionary: A collection of key-value pairs.
person = {"name": "Alice", "age": 30}
#Operator Overloading in Custom Classes
#In Python, you can overload operators to customize their behavior for instances of a class. Below is an example with + (addition) and * (multiplication) operators.
#Example: Vector Class with Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overload the + operator for vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # Overload the * operator for scalar multiplication
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        # Provide a readable string representation for debugging
        return f"Vector({self.x}, {self.y})"

# Creating two Vector instances
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using the overloaded + operator
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# Using the overloaded * operator
v4 = v1 * 3
print(v4)  # Output: Vector(6, 9)
