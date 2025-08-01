# ===========================
# 🔰 BASIC SYNTAX & VARIABLES
# ===========================
print("\n🔰 BASIC SYNTAX")
x = 10
y = 3.14
name = "Python"
is_active = True
print(f"x: {x}, y: {y}, name: {name}, is_active: {is_active}")

# ===================
# 📋 IF...ELIF...ELSE
# ===================
print("\n📋 IF...ELIF...ELSE")
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")

# ============
# 🔁 WHILE LOOP
# ============
print("\n🔁 WHILE LOOP")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# ============
# 🔁 FOR LOOP
# ============
print("\n🔁 FOR LOOP")
for i in range(3):
    print(f"For loop index: {i}")

# ==========
# 🧮 OPERATORS
# ==========
print("\n🧮 OPERATORS")
print("Addition:", x + y)
print("Exponentiation:", x ** 2)
print("String in name:", "Py" in name)
print("Logical AND:", True and False)

# ===============
# 🧰 FUNCTIONS
# ===============
print("\n🧰 FUNCTIONS")
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# ===============
# 🧱 CLASSES & OOP
# ===============
print("\n🧱 CLASSES & OBJECTS (OOP)")
class Person:
    def __init__(self, name, age):
        self.name = name      # Attribute
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Alice", 28)
p1.greet()

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_id(self):
        print(f"My ID is {self.student_id}")

s1 = Student("Bob", 20, "S001")
s1.greet()
s1.show_id()

# ============
# 📦 LISTS
# ============
print("\n📦 LISTS")
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print("List Comprehension:", [x*2 for x in my_list])

# ============
# 📑 DICTIONARIES
# ============
print("\n📑 DICTIONARIES")
student = {"name": "John", "age": 18}
student["grade"] = "A"
for key, value in student.items():
    print(f"{key}: {value}")

# =========
# 🔣 SETS
# =========
print("\n🔣 SETS")
s = {1, 2, 2, 3}
print("Set:", s)

# =========
# 🧾 TUPLES
# =========
print("\n🧾 TUPLES")
t = (1, 2, 3)
print("Tuple:", t)

# ================
# 💾 FILE HANDLING
# ================
print("\n💾 FILE HANDLING")
with open("sample.txt", "w") as f:
    f.write("Learning Python!")

with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:", content)

# ======================
# 🚨 EXCEPTION HANDLING
# ======================
print("\n🚨 EXCEPTION HANDLING")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ======================
# 🔌 IMPORTING MODULES
# ======================
print("\n🔌 IMPORTING MODULES")
import math
print("Square root of 16:", math.sqrt(16))

# ==================
# 🧠 LAMBDA FUNCTION
# ==================
print("\n🧠 LAMBDA FUNCTION")
square = lambda x: x * x
print("Square of 4:", square(4))

# =======================
# 🧼 MAP & FILTER EXAMPLES
# =======================
print("\n🧼 MAP & FILTER")
nums = [1, 2, 3, 4]
print("Map x2:", list(map(lambda x: x * 2, nums)))
print("Filter evens:", list(filter(lambda x: x % 2 == 0, nums)))

# ==================
# 🧪 ENUMERATE & ZIP
# ==================
print("\n🧪 ENUMERATE & ZIP")
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(f"{i}: {color}")

names = ["Alice", "Bob"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# ===============================
# 💡 LIST, DICT & SET COMPREHENSION
# ===============================
print("\n💡 COMPREHENSIONS")
print("List:", [x for x in range(5)])
print("Dict:", {x: x**2 for x in range(3)})
print("Set:", {x for x in [1, 2, 2, 3]})

# ====================
# 🧩 DECORATORS (Basic)
# ====================
print("\n🧩 DECORATORS")
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# =================
# 🧬 GENERATORS
# =================
print("\n🧬 GENERATORS")
def count_up():
    for i in range(3):
        yield i

for num in count_up():
    print("Generated:", num)

# =====================
# 🧹 CLEANUP TEMP FILE
# =====================
import os
os.remove("sample.txt")
