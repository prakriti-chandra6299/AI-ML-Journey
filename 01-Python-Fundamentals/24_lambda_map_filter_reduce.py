
"""
LESSON 24: LAMBDA FUNCTIONS, MAP(), FILTER() AND REDUCE()

REVISION NOTES
--------------
1. Lambda:
   - Small anonymous function.
   - Contains only one expression.
   - Syntax: lambda arguments: expression

2. map():
   - Applies a function to every item in an iterable.
   - Returns a map iterator.
   - Use list() to display all results.

3. filter():
   - Selects items based on a condition.
   - Keeps items for which the function returns True.
   - Returns a filter iterator.

4. reduce():
   - Combines iterable elements into one final value.
   - Available through the functools module.

5. map() transforms, filter() selects, reduce() combines.
"""

# ==================================================
# 1. LAMBDA FUNCTIONS
# ==================================================

# Normal function
def square(number):
    return number * number

print("Normal function:", square(5))

# Equivalent lambda function
square_lambda = lambda number: number * number

print("Lambda function:", square_lambda(5))


# Lambda with two arguments
add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Lambda with a condition
check_even = lambda number: number % 2 == 0

print("Is 8 even?", check_even(8))
print("Is 7 even?", check_even(7))


# ==================================================
# 2. MAP() FUNCTION
# ==================================================

# map(function, iterable)
# Applies the function to every element.

numbers = [1, 2, 3, 4, 5]

# Using a normal function
def double(number):
    return number * 2

result = map(double, numbers)

print("\nDoubled using map():", list(result))


# Using lambda with map()
result = map(lambda number: number * 2, numbers)

print("Doubled using lambda:", list(result))


# Square every number
squares = list(map(lambda number: number ** 2, numbers))

print("Squares:", squares)


# map() with two iterables
first = [10, 20, 30]
second = [1, 2, 3]

sums = list(map(lambda a, b: a + b, first, second))

print("Adding two lists:", sums)


# Convert names to uppercase
names = ["alex", "sam", "jordan"]

uppercase_names = list(map(lambda name: name.upper(), names))

print("Uppercase names:", uppercase_names)


# ==================================================
# 3. FILTER() FUNCTION
# ==================================================

# filter(function, iterable)
# Keeps elements for which the function returns True.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("\nEven numbers:", even_numbers)


# Filter odd numbers
odd_numbers = list(
    filter(lambda number: number % 2 != 0, numbers)
)

print("Odd numbers:", odd_numbers)


# Filter numbers greater than 5
greater_than_five = list(
    filter(lambda number: number > 5, numbers)
)

print("Numbers greater than 5:", greater_than_five)


# Filter names beginning with A
names = ["Alex", "Sam", "Anna", "Jordan", "Amy"]

a_names = list(
    filter(lambda name: name.startswith("A"), names)
)

print("Names beginning with A:", a_names)


# ==================================================
# 4. REDUCE() FUNCTION
# ==================================================

# reduce() combines all elements into one result.
# It must be imported from functools.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate the sum
total = reduce(lambda a, b: a + b, numbers)

print("\nSum using reduce():", total)


# Calculate the product
product = reduce(lambda a, b: a * b, numbers)

print("Product using reduce():", product)


# Find the largest number
values = [12, 45, 7, 89, 23]

largest = reduce(lambda a, b: a if a > b else b, values)

print("Largest number:", largest)


# ==================================================
# 5. COMBINING MAP() AND FILTER()
# ==================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# First select even numbers, then square them.
result = list(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, numbers)
    )
)

print("\nSquares of even numbers:", result)


# ==================================================
# 6. PRACTICAL EXAMPLE
# ==================================================

marks = [45, 78, 32, 90, 65, 25, 88]

# Select students' marks greater than or equal to 40.
passed_marks = list(
    filter(lambda mark: mark >= 40, marks)
)

print("\nPassed marks:", passed_marks)

# Add 5 grace marks to every passing score.
updated_marks = list(
    map(lambda mark: mark + 5, passed_marks)
)

print("Updated marks:", updated_marks)

# Calculate the total of updated marks.
total_marks = reduce(lambda a, b: a + b, updated_marks)

print("Total updated marks:", total_marks)


# ==================================================
# 7. IMPORTANT DIFFERENCES
# ==================================================

"""
LAMBDA:
    Creates a short anonymous function.

MAP:
    Transforms every element.

FILTER:
    Selects elements based on a condition.

REDUCE:
    Combines elements into one final result.

IMPORTANT:
    map() and filter() return iterators in Python 3.
    Use list() when you want to see all their results.
"""
