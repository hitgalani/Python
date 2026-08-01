# Creating Variables
id = 10
name = "Hello"
price = 99.99
is_pass = True

print(id)
print(name)
print(price)
print(is_pass)

# Multiple Variable Assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Same Value to Multiple Variables
a = b = c = 100
print(a, b, c)

# Variable Reassignment
num = 10
print(num)

num = 20
print(num)

# Dynamic Typing
value = 100
print(type(value))

value = "Python"
print(type(value))

value = 10.5
print(type(value))

# Variable Naming Rules
student_name = "John"
studentAge = 20
_marks = 90
salary123 = 50000

print(student_name)
print(studentAge)
print(_marks)
print(salary123)

# Case Sensitive
name = "Alice"
Name = "Bob"

print(name)
print(Name)

# Swapping Variables
a = 10
b = 20

a, b = b, a

print(a, b)

# Delete Variable
x = 100
print(x)

del x
# print(x)   # Error

# Check Variable Type
num = 10
text = "Hello"
pi = 3.14

print(type(num))
print(type(text))
print(type(pi))

# Global Variable
x = 100

def show():
    print(x)

show()

# Local Variable
def demo():
    y = 50
    print(y)

demo()

# Global Keyword
x = 10

def change():
    global x
    x = 50

change()
print(x)

# Variable Unpacking
f_name = ["Rame", "Raje", "Romit"]

a, b, c = f_name

print(a)
print(b)
print(c)

# Print Multiple Variables
name = "Hello"
age = 20

print(name, age)

# Variable Arithmetic
a = 10
b = 5

sum = a + b
sub = a - b
mul = a * b
div = a / b

print(sum)
print(sub)
print(mul)
print(div)

# Variable Concatenation
first = "Hello"
second = "Python"

print(first + " " + second)

# Variable with f-string
name = "Hello"
age = 20

print(f"Name: {name}, Age: {age}")

# --Valid variable names
# name
# student_name
# _age
# marks123
# totalAmount

# --Invalid Variable Names
# 2name        # Starts with a digit
# student name # Contains a space
# class        # Python keyword
# my-name      # Hyphen is not allowed