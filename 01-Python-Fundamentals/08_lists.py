
"""
LESSON 8: LISTS IN PYTHON

REVISION NOTES:

1. A list stores multiple values in one variable.

2. Lists are:
   - Ordered: Elements maintain their positions.
   - Mutable: Elements can be changed.
   - Allow duplicates.
   - Can store different data types.

3. LIST CREATION:
   my_list = [10, 20, 30]

4. INDEXING:
   Positive indexing starts from 0.
   Negative indexing starts from -1.

5. SLICING:
   list[start:stop:step]

6. IMPORTANT LIST METHODS:
   append()  -> Adds one element at the end.
   extend()  -> Adds multiple elements.
   insert()  -> Adds an element at a position.
   remove()  -> Removes the first matching element.
   pop()     -> Removes an element by index.
   clear()   -> Removes all elements.
   sort()    -> Sorts the list.
   reverse() -> Reverses the list.
   index()   -> Finds the index of an element.
   count()   -> Counts occurrences.

7. OTHER FUNCTIONS:
   len()  -> Returns the number of elements.
   max()  -> Returns the largest value.
   min()  -> Returns the smallest value.
   sum()  -> Returns the total.

8. LIST COMPREHENSION:
   Creates a new list using a concise syntax.
"""


# --------------------------------------------------
# 1. CREATING LISTS
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

fruits = ["Apple", "Mango", "Banana"]

mixed = [10, "Python", 3.14, True]

print(numbers)
print(fruits)
print(mixed)


# --------------------------------------------------
# 2. ACCESSING LIST ELEMENTS
# --------------------------------------------------

fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])


# --------------------------------------------------
# 3. LIST SLICING
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:3])
print(numbers[2:])
print(numbers[:4])
print(numbers[::2])
print(numbers[::-1])


# --------------------------------------------------
# 4. CHANGING LIST ELEMENTS
# --------------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits[1] = "Orange"

print(fruits)


# --------------------------------------------------
# 5. APPEND METHOD
# --------------------------------------------------

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# --------------------------------------------------
# 6. EXTEND METHOD
# --------------------------------------------------

numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)


# --------------------------------------------------
# 7. INSERT METHOD
# --------------------------------------------------

fruits = ["Apple", "Banana"]

fruits.insert(1, "Mango")

print(fruits)


# --------------------------------------------------
# 8. REMOVE METHOD
# --------------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits.remove("Mango")

print(fruits)


# --------------------------------------------------
# 9. POP METHOD
# --------------------------------------------------

numbers = [10, 20, 30, 40]

removed = numbers.pop(2)

print("Removed:", removed)
print("Updated list:", numbers)


# --------------------------------------------------
# 10. CLEAR METHOD
# --------------------------------------------------

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


# --------------------------------------------------
# 11. SORTING A LIST
# --------------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# --------------------------------------------------
# 12. REVERSING A LIST
# --------------------------------------------------

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# --------------------------------------------------
# 13. COUNT AND INDEX
# --------------------------------------------------

numbers = [10, 20, 30, 20, 40, 20]

print("Count:", numbers.count(20))
print("Index:", numbers.index(30))


# --------------------------------------------------
# 14. USEFUL LIST FUNCTIONS
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# --------------------------------------------------
# 15. LOOPING THROUGH A LIST
# --------------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 16. CHECKING MEMBERSHIP
# --------------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

print("Mango" in fruits)
print("Orange" not in fruits)


# --------------------------------------------------
# 17. LIST COMPREHENSION
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# --------------------------------------------------
# 18. LIST COMPREHENSION WITH CONDITION
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# --------------------------------------------------
# 19. COPYING A LIST
# --------------------------------------------------

original = [10, 20, 30]

copied = original.copy()

copied.append(40)

print("Original:", original)
print("Copied:", copied)


# --------------------------------------------------
# 20. NESTED LISTS
# --------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])
print(matrix[2][1])


# --------------------------------------------------
# END OF LESSON 8
# --------------------------------------------------
