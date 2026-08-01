age = input("Enter Your Age i can tell after 1 year after your age is?: ")

new_age = int(age) + 1

print(f"your age after 1 year will be: {new_age}")

# type casting 
print(1 + 1.1)
print(1 + int(1.1))
print(str(1) + str(1.1),"Hell" +" "+ "Love")


x = 1 + bool(1.1)   # bool(1.1) → True → 1 → 1 + 1 = 2
y = 1 + bool(0)     # bool(0) → False → 0 → 1 + 0 = 1

print(type(x), x)   # <class 'int'> 2
print(type(y), y)   # <class 'int'> 1


# ==============================
# PYTHON TYPE CASTING - ALL IN ONE PAGE
# ==============================

# 1. Implicit Type Casting
a = 10
b = 5.5
print(a + b, type(a + b))  # <class 'float'>

# 2. int()
print(int(10.9))
print(int("25"))
print(int(True))
print(int(False))

# 3. float()
print(float(10))
print(float("25"))
print(float(True))

# 4. str()
print(str(100))
print(str(10.5))
print(str(True))
print(str([1, 2, 3]))

# 5. bool()
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))

# 6. list()
print(list("Python"))
print(list((1, 2, 3)))
print(list({1, 2, 3}))
print(list({"a": 1, "b": 2}))
print(list(range(5)))

# 7. tuple()
print(tuple([1, 2, 3]))
print(tuple("Hello"))
print(tuple({1, 2, 3}))
print(tuple(range(5)))

# 8. set()
print(set([1, 2, 2, 3]))
print(set("banana"))
print(set((1, 2, 3)))
print(set(range(5)))

# 9. dict()
print(dict([("a", 1), ("b", 2)]))
print(dict(name="John", age=25))
print(dict(zip(["x", "y"], [10, 20])))

# 10. complex()
print(complex(5))
print(complex(2, 3))
print(complex("5+2j"))

# 11. bytes()
print(bytes(5))
print(bytes([65, 66, 67]))
print(bytes("Hello", "utf-8"))

# 12. bytearray()
print(bytearray(5))
print(bytearray([65, 66, 67]))
print(bytearray("Hello", "utf-8"))

# 13. memoryview()
b = bytes([65, 66, 67])
mv = memoryview(b)
print(mv)
print(mv[0])

# 14. frozenset()
print(frozenset([1, 2, 2, 3]))
print(frozenset("apple"))

# 15. chr()
print(chr(65))
print(chr(97))

# 16. ord()
print(ord("A"))
print(ord("a"))

# 17. bin()
print(bin(10))

# 18. oct()
print(oct(10))

# 19. hex()
print(hex(255))

# 20. ascii()
print(ascii("Python"))
print(ascii("你好"))

# 21. map()
numbers = ["1", "2", "3"]
print(list(map(int, numbers)))

# 22. zip() + dict()
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(dict(zip(keys, values)))

# 23. String → List
print(list("Python"))

# 24. List → String
letters = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(letters))

# 25. String → Integer
print(int("123"))

# 26. Integer → String
print(str(123))

# 27. String → Float
print(float("99.99"))

# 28. Float → Integer
print(int(19.99))

# 29. List → Tuple
print(tuple([1, 2, 3]))

# 30. Tuple → List
print(list((1, 2, 3)))

# 31. List → Set
print(set([1, 2, 2, 3]))

# 32. Set → List
print(list({1, 2, 3}))

# 33. Tuple → Set
print(set((1, 2, 2, 3)))

# 34. Set → Tuple
print(tuple({1, 2, 3}))

# 35. Range → List
print(list(range(5)))

# 36. Range → Tuple
print(tuple(range(5)))

# 37. Range → Set
print(set(range(5)))

# 38. Dictionary Keys → List
d = {"a": 1, "b": 2}
print(list(d.keys()))

# 39. Dictionary Values → List
print(list(d.values()))

# 40. Dictionary Items → List
print(list(d.items()))