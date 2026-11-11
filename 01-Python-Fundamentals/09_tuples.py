
"""
LESSON 9: TUPLES IN PYTHON

REVISION NOTES:

1. A tuple stores multiple values in one variable.

2. Tuples are:
   - Ordered
   - Immutable (cannot be modified)
   - Allow duplicate values
   - Can store different data types

3. TUPLE CREATION:
   numbers = (10, 20, 30)

4. SINGLE-ELEMENT TUPLE:
   single = (10,)
   The comma is important.

5. INDEXING:
   Positive indexing starts from 0.
   Negative indexing starts from -1.

6. SLICING:
   tuple[start:stop:step]

7. IMPORTANT TUPLE METHODS:
   count() -> Counts occurrences.
   index() -> Returns the index of an element.

8. USEFUL FUNCTIONS:
   len(), max(), min(), sum()

9. TUPLE UNPACKING:
   Assigns tuple elements to multiple variables.

10. IMMUTABILITY:
    You cannot directly add, remove or modify
    individual elements of a tuple.
"""


# --------------------------------------------------
# 1. CREATING TUPLES
# --------------------------------------------------

numbers = (10, 20, 30, 40)

fruits = ("Apple", "Mango", "Banana")

mixed = (10, "Python", 3.14, True)

print(numbers)
print(fruits)
print(mixed)


# --------------------------------------------------
# 2. CREATING A SINGLE-ELEMENT TUPLE
# --------------------------------------------------

single = (10,)

print(single)
print(type(single))


# --------------------------------------------------
# 3. TUPLE WITHOUT PARENTHESES
# --------------------------------------------------

numbers = 10, 20, 30

print(numbers)
print(type(numbers))


# --------------------------------------------------
# 4. ACCESSING TUPLE ELEMENTS
# --------------------------------------------------

fruits = ("Apple", "Mango", "Banana", "Orange")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])


# --------------------------------------------------
# 5. TUPLE SLICING
# --------------------------------------------------

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[0:3])
print(numbers[2:])
print(numbers[:4])
print(numbers[::2])
print(numbers[::-1])


# --------------------------------------------------
# 6. TUPLE LENGTH
# --------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))


# --------------------------------------------------
# 7. COUNT METHOD
# --------------------------------------------------

numbers = (10, 20, 30, 20, 40, 20)

print("Count:", numbers.count(20))


# --------------------------------------------------
# 8. INDEX METHOD
# --------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Index:", numbers.index(30))


# --------------------------------------------------
# 9. USEFUL TUPLE FUNCTIONS
# --------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# --------------------------------------------------
# 10. LOOPING THROUGH A TUPLE
# --------------------------------------------------

fruits = ("Apple", "Mango", "Banana")

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 11. CHECKING MEMBERSHIP
# --------------------------------------------------

fruits = ("Apple", "Mango", "Banana")

print("Mango" in fruits)
print("Orange" not in fruits)


# --------------------------------------------------
# 12. TUPLE UNPACKING
# --------------------------------------------------

person = ("Alex", 21, "Python Developer")

name, age, profession = person

print("Name:", name)
print("Age:", age)
print("Profession:", profession)


# --------------------------------------------------
# 13. USING THE ASTERISK (*) IN UNPACKING
# --------------------------------------------------

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# --------------------------------------------------
# 14. TUPLE CONCATENATION
# --------------------------------------------------

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

result = tuple1 + tuple2

print(result)


# --------------------------------------------------
# 15. TUPLE REPETITION
# --------------------------------------------------

numbers = (1, 2, 3)

result = numbers * 3

print(result)


# --------------------------------------------------
# 16. IMMUTABILITY OF TUPLES
# --------------------------------------------------

numbers = (10, 20, 30)

# The following statement would cause an error:
# numbers[0] = 100

print(numbers)


# --------------------------------------------------
# 17. CONVERTING LIST TO TUPLE
# --------------------------------------------------

my_list = [10, 20, 30, 40]

my_tuple = tuple(my_list)

print(my_tuple)


# --------------------------------------------------
# 18. CONVERTING TUPLE TO LIST
# --------------------------------------------------

my_tuple = (10, 20, 30, 40)

my_list = list(my_tuple)

my_list.append(50)

print(my_list)


# --------------------------------------------------
# 19. NESTED TUPLES
# --------------------------------------------------

students = (
    ("Alex", 85),
    ("Sam", 90),
    ("John", 78)
)

print(students[0])
print(students[1][1])
print(students[2][0])


# --------------------------------------------------
# END OF LESSON 9
# --------------------------------------------------
