
"""
LESSON 23: COMPREHENSIONS IN PYTHON

REVISION NOTES:

1. Comprehensions provide a concise way to create collections.
2. List comprehension creates a list.
3. Set comprehension creates a set.
4. Dictionary comprehension creates a dictionary.
5. Conditional comprehensions allow filtering.
6. Nested comprehensions support multiple loops.

LIST COMPREHENSION SYNTAX:

[expression for item in iterable]

WITH CONDITION:

[expression for item in iterable if condition]

SET COMPREHENSION:

{expression for item in iterable}

DICTIONARY COMPREHENSION:

{key: value for item in iterable}

GENERATOR EXPRESSION:

(expression for item in iterable)
"""

# --------------------------------------------------
# 1. Normal way of creating a list
# --------------------------------------------------

squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print("Normal List:", squares)


# --------------------------------------------------
# 2. Basic list comprehension
# --------------------------------------------------

squares = [number ** 2 for number in range(1, 6)]

print("\nList Comprehension:", squares)


# --------------------------------------------------
# 3. List comprehension with conditions
# --------------------------------------------------

even_numbers = [
    number for number in range(1, 21)
    if number % 2 == 0
]

print("\nEven Numbers:", even_numbers)


# --------------------------------------------------
# 4. List comprehension with if-else
# --------------------------------------------------

results = [
    "Even" if number % 2 == 0 else "Odd"
    for number in range(1, 11)
]

print("\nEven or Odd:", results)


# --------------------------------------------------
# 5. Converting strings to uppercase
# --------------------------------------------------

names = ["alex", "sam", "john", "david"]

uppercase_names = [
    name.upper() for name in names
]

print("\nUppercase Names:", uppercase_names)


# --------------------------------------------------
# 6. Filtering positive numbers
# --------------------------------------------------

numbers = [-10, 5, -3, 20, 0, 15]

positive_numbers = [
    number for number in numbers
    if number > 0
]

print("\nPositive Numbers:", positive_numbers)


# --------------------------------------------------
# 7. Set comprehension
# --------------------------------------------------

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_squares = {
    number ** 2 for number in numbers
}

print("\nSet Comprehension:", unique_squares)


# --------------------------------------------------
# 8. Dictionary comprehension
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

square_dictionary = {
    number: number ** 2
    for number in numbers
}

print("\nDictionary Comprehension:", square_dictionary)


# --------------------------------------------------
# 9. Dictionary comprehension with condition
# --------------------------------------------------

marks = {
    "Alex": 85,
    "Sam": 45,
    "John": 90,
    "David": 35
}

passed_students = {
    name: score
    for name, score in marks.items()
    if score >= 50
}

print("\nPassed Students:", passed_students)


# --------------------------------------------------
# 10. Nested list comprehension
# --------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print("\nFlattened Matrix:", flattened)


# --------------------------------------------------
# 11. Extracting even numbers from a matrix
# --------------------------------------------------

even_values = [
    number
    for row in matrix
    for number in row
    if number % 2 == 0
]

print("\nEven Matrix Values:", even_values)


# --------------------------------------------------
# 12. Generator expression
# --------------------------------------------------

squares_generator = (
    number ** 2 for number in range(1, 6)
)

print("\nGenerator Expression:")

for value in squares_generator:
    print(value)


# --------------------------------------------------
# 13. Practical example: Data filtering
# --------------------------------------------------

student_marks = [45, 78, 90, 32, 65, 88, 40]

passed_marks = [
    mark for mark in student_marks
    if mark >= 50
]

print("\nPassed Marks:", passed_marks)


# Calculate percentage increase
updated_marks = [
    mark + 5 for mark in passed_marks
]

print("Updated Marks:", updated_marks)


# --------------------------------------------------
# END OF LESSON 23
# --------------------------------------------------
