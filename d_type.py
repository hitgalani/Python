name = "Hello"
age = 1
cgpe = 5.5
is_student = True
com = 1 + 5.5j


print(type(name))
print(type(age))
print(type(cgpe))
print(type(is_student))
print(type(com))

# ============================
# PYTHON DATA TYPES
# ============================

# 1. Numeric Data Types
a = 10                 # int
b = 10.5               # float
c = 3 + 4j             # complex

print(a, type(a))
print(b, type(b))
print(c, type(c))

# 2. String
name = "Python"

print(name, type(name))

# 3. Boolean
x = True
y = False

print(x, type(x))
print(y, type(y))

# 4. List (Ordered, Mutable)
numbers = [10, 20, 30]

print(numbers, type(numbers))

# 5. Tuple (Ordered, Immutable)
colors = ("Red", "Green", "Blue")

print(colors, type(colors))

# 6. Set (Unordered, No Duplicates)
fruits = {"Apple", "Banana", "Mango"}

print(fruits, type(fruits))

# 7. Dictionary (Key : Value)
student = {
    "name": "John",
    "age": 20
}

print(student, type(student))

# 8. NoneType
n = None

print(n, type(n))
