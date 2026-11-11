
"""
========================================================
TOPIC: USER INPUT AND TYPE CONVERSION IN PYTHON
========================================================

1. USER INPUT
   - input() is used to accept data from the user.
   - It pauses program execution until input is provided.
   - input() always returns data as a string (str).

2. INPUT WITH A MESSAGE
   - input("Enter your name: ") displays a prompt.
   - The entered value is stored in a variable.

3. TYPE CONVERSION
   - int()   : Converts input into an integer.
   - float() : Converts input into a decimal number.
   - str()   : Converts a value into a string.
   - bool()  : Converts a value into a boolean.

4. IMPORTANT
   - input() always returns a string.
   - Convert input before performing numerical calculations.
   - Invalid conversions can raise ValueError.
   - int("hello") is invalid.
   - int("25") is valid.

5. FORMATTED OUTPUT (F-STRINGS)
   - An f-string starts with the letter f before quotes.
   - Variables can be inserted using curly braces {}.
   - Example: f"Hello {name}"

6. USEFUL FUNCTIONS
   - print() : Displays output.
   - input() : Accepts user input.
   - type()  : Checks the data type.
   - int()   : Converts to integer.
   - float() : Converts to decimal.

========================================================
"""


# ------------------------------------------------------
# 1. BASIC USER INPUT
# ------------------------------------------------------

name = input("Enter your name: ")

print("Hello", name)


# ------------------------------------------------------
# 2. CHECKING THE INPUT DATA TYPE
# ------------------------------------------------------

value = input("Enter something: ")

print("Entered value:", value)
print("Data type:", type(value))


# ------------------------------------------------------
# 3. TAKING INTEGER INPUT
# ------------------------------------------------------

age = int(input("Enter your age: "))

print("Your age is:", age)
print("Data type:", type(age))


# ------------------------------------------------------
# 4. TAKING FLOAT INPUT
# ------------------------------------------------------

marks = float(input("Enter your marks: "))

print("Your marks are:", marks)
print("Data type:", type(marks))


# ------------------------------------------------------
# 5. TYPE CONVERSION
# ------------------------------------------------------

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

num1 = int(number1)
num2 = int(number2)

print("Sum:", num1 + num2)


# ------------------------------------------------------
# 6. FORMATTED OUTPUT USING F-STRINGS
# ------------------------------------------------------

student = input("Enter student name: ")
subject = input("Enter subject: ")
score = float(input("Enter marks: "))

print(f"{student} scored {score} marks in {subject}.")


# ------------------------------------------------------
# 7. MULTIPLE INPUTS IN ONE LINE
# ------------------------------------------------------

a, b = input("Enter two numbers separated by space: ").split()

a = int(a)
b = int(b)

print("First number:", a)
print("Second number:", b)
print("Product:", a * b)


# ------------------------------------------------------
# 8. HANDLING INVALID INPUT
# ------------------------------------------------------

try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a valid integer.")


# ------------------------------------------------------
# 9. SIMPLE CALCULATOR
# ------------------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division by zero is not allowed.")
