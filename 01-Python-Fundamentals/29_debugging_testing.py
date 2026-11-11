
"""
LESSON 29: PYTHON DEBUGGING AND TESTING BASICS

REVISION NOTES
--------------
1. Debugging:
   Finding and fixing errors in a program.

2. Three common types of errors:
   - Syntax Error: Incorrect Python syntax.
   - Runtime Error: Error occurring while executing.
   - Logical Error: Program runs but gives wrong output.

3. print():
   Helps inspect variable values.

4. breakpoint():
   Pauses execution and opens Python's debugger.

5. assert:
   Checks whether a condition is True.
   Raises AssertionError if False.

6. try-except:
   Handles runtime errors.

7. Unit Testing:
   Tests individual functions or small code units.

8. Python provides the built-in unittest module.
"""

# ==================================================
# 1. SYNTAX ERROR
# ==================================================

# Syntax errors occur when Python rules are violated.

# Incorrect example (kept as a comment):
# print("Hello"

# Correct example:
print("1. Syntax error example:")
print("Hello Python!")


# ==================================================
# 2. RUNTIME ERROR
# ==================================================

# Runtime errors occur while a program is running.

print("\n2. Runtime error example:")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# ==================================================
# 3. LOGICAL ERROR
# ==================================================

# The program runs, but the calculation is incorrect.

print("\n3. Logical error example:")

length = 10
width = 5

# Incorrect formula:
wrong_area = 2 * (length + width)
print("Incorrect area:", wrong_area)

# Correct formula:
correct_area = length * width
print("Correct area:", correct_area)


# ==================================================
# 4. DEBUGGING USING PRINT()
# ==================================================

print("\n4. Debugging using print():")

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:

    print("Current number:", number)

    total += number

    print("Current total:", total)

print("Final total:", total)


# ==================================================
# 5. DEBUGGING USING breakpoint()
# ==================================================

print("\n5. Debugging using breakpoint():")

def calculate_sum(a, b):

    result = a + b

    # Uncomment this line to pause execution
    # breakpoint()

    return result


answer = calculate_sum(10, 20)

print("Sum:", answer)

"""
When breakpoint() is active, Python pauses execution.

Useful debugger commands:
n = Next line
s = Step into function
c = Continue execution
p = Print a variable
q = Quit debugger

Remove or comment out breakpoint() after debugging.
"""


# ==================================================
# 6. ASSERT STATEMENTS
# ==================================================

print("\n6. Assert statements:")

age = 20

assert age >= 18, "Age must be at least 18"

print("Age verification successful!")


# Testing calculations using assert
assert 5 + 5 == 10
assert 10 * 2 == 20
assert 20 / 2 == 10

print("All assertions passed!")


# ==================================================
# 7. TESTING A FUNCTION
# ==================================================

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print("\n7. Testing functions:")

assert add(5, 3) == 8
assert add(-2, 2) == 0

assert multiply(4, 5) == 20
assert multiply(3, 0) == 0

print("Function tests passed!")


# ==================================================
# 8. HANDLING ERRORS DURING TESTING
# ==================================================

def divide(a, b):

    if b == 0:
        raise ValueError("Divisor cannot be zero")

    return a / b


print("\n8. Testing division:")

try:
    print("Division result:", divide(10, 2))
    print("Division result:", divide(10, 0))

except ValueError as error:
    print("Test detected an error:", error)


# ==================================================
# 9. UNIT TESTING USING unittest
# ==================================================

import unittest


def subtract(a, b):
    return a - b


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


# Run the unit tests when this file is executed directly.
if __name__ == "__main__":

    print("\n9. Running unit tests:")

    unittest.main(verbosity=2)


# ==================================================
# 10. IMPORTANT DIFFERENCES
# ==================================================

"""
DEBUGGING:
    Finding and fixing errors.

TESTING:
    Checking whether code works correctly.

ASSERT:
    Checks a condition during development.

UNIT TEST:
    Tests one function or small unit independently.

breakpoint():
    Pauses the program so you can inspect execution.

IMPORTANT:
    Python's unittest module is built in.
    No pip installation is required.
"""
