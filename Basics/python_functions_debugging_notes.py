
"""
Python Functions & Debugging Notes by Simranjeet Kaur Sudan
Topics: Functions, Argument Types, *args, **kwargs, Scope, VS Code Debugging
"""

# ----------------------------
# 📌 1. Defining Functions
# ----------------------------

def greet():
    print("Hello, welcome to Python!")

greet()

# ----------------------------
# 📌 2. Function with Parameters
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Simran")

# ----------------------------
# 📌 3. Return Statement
# ----------------------------

def square(x):
    return x * x

result = square(5)
print(result)

# ----------------------------
# 📌 4. Argument Types
# ----------------------------

# Positional Arguments
def full_name(first, last):
    return f"{first} {last}"

print(full_name("Simran", "Kaur"))

# Default Arguments
def welcome(name="Guest"):
    print(f"Welcome, {name}")

welcome()
welcome("Simran")

# Keyword Arguments
def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=28, name="Simran")

# ----------------------------
# 📌 5. *args (Variable Positional Arguments)
# ----------------------------

def add_all(*numbers):
    total = sum(numbers)
    print(f"Total: {total}")

add_all(2, 4, 6, 8)

# ----------------------------
# 📌 6. **kwargs (Variable Keyword Arguments)
# ----------------------------

def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Simran", role="Cloud Engineer")

# ----------------------------
# 📌 7. Scope – Local vs Global
# ----------------------------

name = "Simran"  # Global variable

def change_name():
    name = "Kaur"  # Local variable
    print(f"Inside function: {name}")

change_name()
print(f"Outside function: {name}")

# ----------------------------
# 📌 8. Using 'global' Keyword
# ----------------------------

counter = 0

def increment():
    global counter
    counter += 1

increment()
print(f"Global counter: {counter}")

# ----------------------------
# 📌 9. Debugging in VS Code – Tips
# ----------------------------

# ✅ Add breakpoints by clicking left of line number
# ✅ Use F5 to start debugging
# ✅ Hover over variables to inspect values
# ✅ Use "Step Over (F10)", "Step Into (F11)", and "Continue (F5)"
# ✅ Use Watch panel to track specific variables
# ✅ Add print statements for quick tracing
# ✅ Use "Run and Debug" panel for configurations

# ----------------------------
# 📌 10. VS Code Tricks for Python
# ----------------------------

# ⚡ Shortcut: Ctrl + ` (open terminal)
# ⚡ Format code: Shift + Alt + F
# ⚡ Rename symbol: F2
# ⚡ Quick fix: Ctrl + .
# ⚡ Multi-cursor: Alt + Click

# ----------------------------
# End of Notes
# ----------------------------
