
"""
PYTHON FUNDAMENTALS - 30 PRACTICE QUESTIONS WITH SOLUTIONS

Level: Beginner to Intermediate
Coverage: Python Lessons 1-30

Each section contains:
1. A practical programming question.
2. A working Python solution.

Topics:
Basics, Variables, Input, Operators, Conditions, Loops,
Strings, Lists, Tuples, Sets, Dictionaries, Functions,
Modules, Exceptions, File Handling, OOP, Inheritance,
Polymorphism, Encapsulation, Abstraction, Iterators,
Generators, Comprehensions, Lambda, Recursion, Scope,
Built-in Functions, JSON, CSV, Testing and Virtual Environments.

Use fictional/sample data only.
"""


# ============================================================
# Q1. PYTHON BASICS
# Question:
# Display a formatted profile card for a fictional student.
# ============================================================

print("\nQ1. PYTHON BASICS")

print("=" * 30)
print("       STUDENT PROFILE")
print("=" * 30)
print("Name       : Alex")
print("Age        : 20")
print("Course     : Computer Science")
print("Goal       : Become a Python Developer")
print("=" * 30)


# ============================================================
# Q2. VARIABLES AND DATA TYPES
# Question:
# Create variables of different data types and display them.
# ============================================================

print("\nQ2. VARIABLES AND DATA TYPES")

product_name = "Laptop"
price = 55000.50
quantity = 3
is_available = True

print("Product:", product_name, type(product_name))
print("Price:", price, type(price))
print("Quantity:", quantity, type(quantity))
print("Available:", is_available, type(is_available))


# ============================================================
# Q3. USER INPUT AND TYPE CONVERSION
# Question:
# Calculate the area and perimeter of a rectangle.
# ============================================================

print("\nQ3. USER INPUT AND TYPE CONVERSION")

length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print("Length:", length)
print("Width:", width)
print("Area:", area)
print("Perimeter:", perimeter)


# ============================================================
# Q4. OPERATORS
# Question:
# Calculate discount and final bill amount.
# ============================================================

print("\nQ4. OPERATORS")

bill_amount = 2000
discount_percentage = 10

discount = bill_amount * discount_percentage / 100
final_amount = bill_amount - discount

print("Original Bill:", bill_amount)
print("Discount:", discount)
print("Final Amount:", final_amount)


# ============================================================
# Q5. CONDITIONAL STATEMENTS
# Question:
# Assign a grade based on marks.
# ============================================================

print("\nQ5. CONDITIONAL STATEMENTS")

marks = 85

if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
elif 0 <= marks < 60:
    grade = "F"
else:
    grade = "Invalid Marks"

print("Marks:", marks)
print("Grade:", grade)


# ============================================================
# Q6. LOOPS
# Question:
# Print the multiplication table of a number.
# ============================================================

print("\nQ6. LOOPS")

number = 7

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ============================================================
# Q7. STRINGS
# Question:
# Count words and characters in a sentence.
# ============================================================

print("\nQ7. STRINGS")

sentence = "Python is useful for Data Science"

print("Original:", sentence)
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Characters:", len(sentence))
print("Words:", len(sentence.split()))


# ============================================================
# Q8. LISTS
# Question:
# Find average, maximum, minimum and sorted temperatures.
# ============================================================

print("\nQ8. LISTS")

temperatures = [32, 28, 35, 30, 27, 34]

average = sum(temperatures) / len(temperatures)

print("Temperatures:", temperatures)
print("Average:", average)
print("Maximum:", max(temperatures))
print("Minimum:", min(temperatures))
print("Sorted:", sorted(temperatures))


# ============================================================
# Q9. TUPLES
# Question:
# Store weekdays and access a day using its number.
# ============================================================

print("\nQ9. TUPLES")

weekdays = (
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
)

day_number = 3

if 1 <= day_number <= 7:
    print("Day:", weekdays[day_number - 1])
else:
    print("Invalid day number")


# ============================================================
# Q10. SETS
# Question:
# Find common and unique workshop participants.
# ============================================================

print("\nQ10. SETS")

workshop_a = {"Alex", "Jordan", "Taylor", "Morgan"}
workshop_b = {"Taylor", "Morgan", "Casey", "Riley"}

print("Common:", workshop_a & workshop_b)
print("Only Workshop A:", workshop_a - workshop_b)
print("All Participants:", workshop_a | workshop_b)


# ============================================================
# Q11. DICTIONARIES
# Question:
# Create and update product information.
# ============================================================

print("\nQ11. DICTIONARIES")

product = {
    "name": "Keyboard",
    "price": 1200,
    "category": "Electronics",
    "stock": 15
}

product["price"] = 1000
product["discount"] = 200

for key, value in product.items():
    print(key, ":", value)


# ============================================================
# Q12. FUNCTIONS
# Question:
# Create a function to calculate basic statistics.
# ============================================================

print("\nQ12. FUNCTIONS")

def calculate_statistics(numbers):

    return {
        "minimum": min(numbers),
        "maximum": max(numbers),
        "average": sum(numbers) / len(numbers)
    }


values = [10, 20, 30, 40, 50]

print(calculate_statistics(values))


# ============================================================
# Q13. MODULES AND PACKAGES
# Question:
# Use the math module for mathematical operations.
# ============================================================

print("\nQ13. MODULES AND PACKAGES")

import math

number = 25

print("Square Root:", math.sqrt(number))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Factorial:", math.factorial(5))


# ============================================================
# Q14. EXCEPTION HANDLING
# Question:
# Divide two numbers safely.
# ============================================================

print("\nQ14. EXCEPTION HANDLING")

try:
    first_number = 100
    second_number = 0

    result = first_number / second_number
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except TypeError:
    print("Invalid input type.")


# ============================================================
# Q15. FILE HANDLING
# Question:
# Write, read and append information to a text file.
# ============================================================

print("\nQ15. FILE HANDLING")

with open("practice_notes.txt", "w") as file:
    file.write("Python Practice\n")
    file.write("Learning File Handling\n")

with open("practice_notes.txt", "a") as file:
    file.write("Appending a new line\n")

with open("practice_notes.txt", "r") as file:
    print(file.read())


# ============================================================
# Q16. OOP BASICS
# Question:
# Create a Book class with attributes and a method.
# ============================================================

print("\nQ16. OOP BASICS")

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.title, self.author, self.price)


book1 = Book("Python Basics", "John Smith", 450)
book2 = Book("Learning Programming", "David Lee", 550)

book1.display()
book2.display()


# ============================================================
# Q17. INHERITANCE
# Question:
# Create Employee and Manager classes.
# ============================================================

print("\nQ17. INHERITANCE")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


manager = Manager("Alex", 50000, "IT")
manager.display()


# ============================================================
# Q18. POLYMORPHISM
# Question:
# Calculate areas using the same method name.
# ============================================================

print("\nQ18. POLYMORPHISM")

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def display_area(shape):
    print("Area:", round(shape.area(), 2))


display_area(Circle(5))
display_area(Rectangle(10, 5))


# ============================================================
# Q19. ENCAPSULATION
# Question:
# Create a BankAccount with controlled balance operations.
# ============================================================

print("\nQ19. ENCAPSULATION")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal.")

    def display_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)
account.display_balance()


# ============================================================
# Q20. ABSTRACTION
# Question:
# Create an abstract Shape class.
# ============================================================

print("\nQ20. ABSTRACTION")

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class CircleShape(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class RectangleShape(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = CircleShape(4)
rectangle = RectangleShape(5, 3)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())


# ============================================================
# Q21. ITERATORS AND ITERABLES
# Question:
# Use iter() and next() to access list elements.
# ============================================================

print("\nQ21. ITERATORS")

items = ["Pen", "Book", "Pencil", "Eraser", "Scale"]

iterator = iter(items)

try:
    while True:
        print(next(iterator))

except StopIteration:
    print("Iterator exhausted.")


# ============================================================
# Q22. GENERATORS
# Question:
# Generate the first n even numbers using yield.
# ============================================================

print("\nQ22. GENERATORS")

def even_numbers(n):

    for number in range(n):
        yield number * 2


for value in even_numbers(5):
    print(value)


# ============================================================
# Q23. COMPREHENSIONS
# Question:
# Generate squares and filter even numbers.
# ============================================================

print("\nQ23. COMPREHENSIONS")

numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]
even = [number for number in numbers if number % 2 == 0]

square_dictionary = {
    number: number ** 2 for number in numbers
}

print("Squares:", squares)
print("Even Numbers:", even)
print("Square Dictionary:", square_dictionary)


# ============================================================
# Q24. LAMBDA, MAP, FILTER AND REDUCE
# Question:
# Increase prices by 10%, filter and calculate total.
# ============================================================

print("\nQ24. LAMBDA, MAP, FILTER AND REDUCE")

from functools import reduce

prices = [100, 200, 300, 400, 500]

increased_prices = list(
    map(lambda price: price * 1.10, prices)
)

filtered_prices = list(
    filter(lambda price: price > 300, increased_prices)
)

total = reduce(lambda x, y: x + y, increased_prices)

print("Updated Prices:", increased_prices)
print("Prices Above 300:", filtered_prices)
print("Total:", total)


# ============================================================
# Q25. RECURSION
# Question:
# Calculate factorial using recursion.
# ============================================================

print("\nQ25. RECURSION")

def factorial(number):

    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))


# ============================================================
# Q26. VARIABLE SCOPE
# Question:
# Demonstrate local, global and nonlocal variables.
# ============================================================

print("\nQ26. VARIABLE SCOPE")

message = "Global message"


def outer_function():

    count = 10

    def inner_function():

        nonlocal count
        count += 5
        print("Nonlocal count:", count)

    inner_function()


outer_function()

print("Global variable:", message)


# ============================================================
# Q27. BUILT-IN FUNCTIONS
# Question:
# Calculate statistics using built-in functions.
# ============================================================

print("\nQ27. BUILT-IN FUNCTIONS")

scores = [75, 90, 85, 60, 95, 80]

print("Total:", sum(scores))
print("Count:", len(scores))
print("Average:", sum(scores) / len(scores))
print("Minimum:", min(scores))
print("Maximum:", max(scores))
print("Sorted:", sorted(scores))


# ============================================================
# Q28. JSON AND CSV HANDLING
# Question:
# Save and read inventory data using JSON and CSV.
# ============================================================

print("\nQ28. JSON AND CSV HANDLING")

import json
import csv

inventory = [
    {"name": "Mouse", "price": 500, "quantity": 10},
    {"name": "Keyboard", "price": 1200, "quantity": 5},
    {"name": "Monitor", "price": 8000, "quantity": 3}
]

# JSON writing
with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# JSON reading
with open("inventory.json", "r") as file:
    json_data = json.load(file)

print("JSON Records:", json_data)

# CSV writing
with open("inventory.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["name", "price", "quantity"]
    )

    writer.writeheader()
    writer.writerows(inventory)

# CSV reading
with open("inventory.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print("CSV Record:", row)


# ============================================================
# Q29. DEBUGGING AND TESTING
# Question:
# Write a function and test it using unittest.
# ============================================================

print("\nQ29. DEBUGGING AND TESTING")

import unittest


def calculate_average(numbers):

    if not numbers:
        raise ValueError("List cannot be empty.")

    return sum(numbers) / len(numbers)


class TestAverage(unittest.TestCase):

    def test_normal_values(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_single_value(self):
        self.assertEqual(calculate_average([50]), 50)

    def test_decimal_values(self):
        self.assertEqual(calculate_average([2, 3]), 2.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])


suite = unittest.TestLoader().loadTestsFromTestCase(TestAverage)
unittest.TextTestRunner(verbosity=2).run(suite)


# ============================================================
# Q30. VIRTUAL ENVIRONMENTS AND PIP
# Question:
# Check the active Python environment and installed packages.
# ============================================================

print("\nQ30. VIRTUAL ENVIRONMENTS")

import sys
import importlib.util

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)

if sys.prefix != sys.base_prefix:
    print("Virtual Environment: ACTIVE")
else:
    print("Virtual Environment: NOT ACTIVE")

packages = ["numpy", "pandas", "matplotlib"]

for package in packages:

    if importlib.util.find_spec(package):
        print(package, "- Installed")
    else:
        print(package, "- Not Installed")


# ============================================================
# END OF PRACTICE QUESTIONS
# ============================================================

print("\n" + "=" * 45)
print("ALL 30 PRACTICE SECTIONS COMPLETED")
print("=" * 45)


# TIME COMPLEXITY:
# Each question has its own complexity depending on input size.
# Most basic examples take O(1) or O(n).
# Sorting takes O(n log n).
# Recursive factorial takes O(n) time and O(n) stack space.
