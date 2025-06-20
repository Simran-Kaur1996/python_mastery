
"""
Python Learning Notes by Simranjeet Kaur Sudan
Topics: Variables, Strings, Numbers, Type Conversion
"""

# ----------------------------
# 📌 1. Variables
# ----------------------------

x = 10
name = "Simran"
price = 19.99

# Variables store data values. Python uses dynamic typing.

# ----------------------------
# 📌 2. Variable Naming Rules
# ----------------------------

# Valid variable names
user_name = "Simran"
age1 = 28

# Invalid examples (uncomment to test)
# 1name = "Simran"   # Cannot start with a number
# my-name = "Simran" # Hyphens are not allowed

# Best practice: use lowercase with underscores (snake_case)

# ----------------------------
# 📌 3. Strings
# ----------------------------

greeting = 'Hello'
intro = "Welcome to Python!"
multiline = '''This is a
multi-line string.'''

# Strings are sequences of characters. They can be enclosed in single, double, or triple quotes.

# ----------------------------
# 📌 4. Escape Sequences
# ----------------------------

quote = "She said, \"Python is awesome!\"\nNew line here."

# Common escape sequences:
# \'  → single quote
# \"  → double quote
# \\  → backslash
# \n  → new line
# \t  → tab

# ----------------------------
# 📌 5. Formatted Strings
# ----------------------------

name = "Simran"
age = 28

formatted = f"My name is {name} and I am {age} years old."

# f-strings provide a clean way to embed expressions inside string literals.

# ----------------------------
# 📌 6. String Methods
# ----------------------------

text = "  Hello, Python!  "

print(text.lower())        # '  hello, python!  '
print(text.upper())        # '  HELLO, PYTHON!  '
print(text.strip())        # 'Hello, Python!'
print(text.replace("Python", "World"))  # '  Hello, World!  '
print("Python" in text)    # True

# Other useful methods:
# .find(), .split(), .startswith(), .endswith()

# ----------------------------
# 📌 7. Numbers
# ----------------------------

integer_num = 42
float_num = 3.14
is_valid = True

# Integer, float, and boolean types.

# ----------------------------
# 📌 8. Working with Numbers
# ----------------------------

a = 15
b = 4

print(a + b)     # Addition
print(a - b)     # Subtraction
print(a * b)     # Multiplication
print(a / b)     # Division (float)
print(a // b)    # Floor division
print(a % b)     # Modulo (remainder)
print(a ** b)    # Exponentiation

# ----------------------------
# 📌 9. Type Conversion
# ----------------------------

str_num = "100"
converted_int = int(str_num)   # str to int

num = 45.67
converted_str = str(num)       # float to str

non_empty = "Python"
bool_val = bool(non_empty)     # Non-empty → True

# int(), float(), str(), bool() are commonly used type conversion functions.
