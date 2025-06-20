
"""
Python Control Flow Notes by Simranjeet Kaur Sudan
Topics: Comparison Operators, Conditional Statements, Logical Operators,
Ternary Operators, Short-Circuiting, Chaining Comparisons, Loops
"""

# ----------------------------
# 📌 1. Comparison Operators
# ----------------------------

a = 10
b = 20

print(a == b)  # False (Equal)
print(a != b)  # True  (Not equal)
print(a > b)   # False (Greater than)
print(a < b)   # True  (Less than)
print(a >= b)  # False (Greater than or equal)
print(a <= b)  # True  (Less than or equal)

# ----------------------------
# 📌 2. Conditional Statements (if/elif/else)
# ----------------------------

age = 22

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# ----------------------------
# 📌 3. Ternary Operator (Conditional Expression)
# ----------------------------

score = 85
result = "Pass" if score >= 50 else "Fail"
print(result)

# ----------------------------
# 📌 4. Logical Operators
# ----------------------------

x = 5

print(x > 3 and x < 10)  # True
print(x < 3 or x > 2)    # True
print(not (x > 3))       # False

# ----------------------------
# 📌 5. Short-Circuit Evaluation
# ----------------------------

def check():
    print("Function called")
    return True

print(False and check())  # Function won't be called (short-circuited)
print(True or check())    # Function won't be called (short-circuited)

# ----------------------------
# 📌 6. Chaining Comparison Operators
# ----------------------------

num = 15

# Equivalent to (10 < num) and (num < 20)
if 10 < num < 20:
    print("Number is between 10 and 20")

# ----------------------------
# 📌 7. For Loop
# ----------------------------

for i in range(5):
    print(f"Iteration: {i}")

# ----------------------------
# 📌 8. For-Else Loop
# ----------------------------

for i in range(3):
    print(i)
else:
    print("Loop completed without break.")

# With break
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This won't print because loop was broken.")

# ----------------------------
# 📌 9. Nested Loops
# ----------------------------

for i in range(1, 3):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# ----------------------------
# 📌 10. Iterables and For Loops
# ----------------------------

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Strings are iterable
for ch in "Python":
    print(ch)

# ----------------------------
# 📌 11. While Loop
# ----------------------------

counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# ----------------------------
# 📌 12. Infinite Loop with Break
# ----------------------------

while True:
    answer = input("Type 'exit' to quit: ")
    if answer == 'exit':
        break
