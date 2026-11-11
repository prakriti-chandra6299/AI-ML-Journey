
"""
LESSON 27: IMPORTANT PYTHON BUILT-IN FUNCTIONS

REVISION NOTES
--------------
1. len()       - Returns the length of an object.
2. type()      - Returns the data type.
3. range()     - Generates a sequence of numbers.
4. enumerate() - Provides index and value together.
5. zip()       - Combines multiple iterables.
6. sorted()    - Returns a new sorted list.
7. reversed()  - Returns elements in reverse order.
8. sum()       - Calculates the sum.
9. min()       - Returns the smallest value.
10. max()      - Returns the largest value.
11. any()      - True if at least one element is true.
12. all()      - True if every element is true.
13. abs()      - Returns absolute value.
14. round()    - Rounds a number.
15. isinstance()- Checks an object's data type.
"""

# ==================================================
# 1. len() AND type()
# ==================================================

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Data type:", type(numbers))

name = "Python"

print("String length:", len(name))
print("String type:", type(name))


# ==================================================
# 2. range()
# ==================================================

print("\nRange from 0 to 4:")

for number in range(5):
    print(number, end=" ")

print()

print("Range from 2 to 8:")

for number in range(2, 9):
    print(number, end=" ")

print()

print("Range with step 2:")

for number in range(2, 11, 2):
    print(number, end=" ")

print()


# ==================================================
# 3. enumerate()
# ==================================================

subjects = ["Python", "Mathematics", "Statistics"]

print("\nUsing enumerate():")

for index, subject in enumerate(subjects):
    print(index, subject)


# Starting index from 1
print("\nStarting index from 1:")

for index, subject in enumerate(subjects, start=1):
    print(index, subject)


# ==================================================
# 4. zip()
# ==================================================

names = ["Alex", "Sam", "Jordan"]
marks = [85, 92, 78]

print("\nUsing zip():")

for name, mark in zip(names, marks):
    print(name, "scored", mark)


# zip() stops at the shortest iterable by default.
numbers = [1, 2, 3]
letters = ["A", "B"]

print("Unequal lists:", list(zip(numbers, letters)))


# ==================================================
# 5. sorted()
# ==================================================

numbers = [50, 10, 40, 20, 30]

print("\nOriginal list:", numbers)

print("Ascending:", sorted(numbers))

print("Descending:", sorted(numbers, reverse=True))

# sorted() returns a new sorted list.
# Original list remains unchanged.
print("Original after sorted():", numbers)


# ==================================================
# 6. sorted() WITH key
# ==================================================

words = ["banana", "kiwi", "apple", "watermelon"]

# Sort according to word length
result = sorted(words, key=len)

print("\nSorted by length:", result)


# ==================================================
# 7. reversed()
# ==================================================

numbers = [1, 2, 3, 4, 5]

print("\nReversed list:", list(reversed(numbers)))

word = "PYTHON"

print("Reversed string:", "".join(reversed(word)))


# ==================================================
# 8. sum(), min() AND max()
# ==================================================

marks = [75, 85, 90, 65, 80]

print("\nTotal marks:", sum(marks))
print("Minimum marks:", min(marks))
print("Maximum marks:", max(marks))


# ==================================================
# 9. any() AND all()
# ==================================================

numbers = [2, 4, 6, 8, 9]

# any(): At least one element satisfies the condition.
print("\nAny odd number?", any(number % 2 != 0 for number in numbers))

# all(): Every element satisfies the condition.
print("Are all numbers positive?", all(number > 0 for number in numbers))

values = [True, True, False]

print("any(values):", any(values))
print("all(values):", all(values))


# ==================================================
# 10. abs() AND round()
# ==================================================

print("\nAbsolute value:", abs(-25))
print("Rounded value:", round(3.14159, 2))
print("Rounded number:", round(8.7))


# ==================================================
# 11. isinstance()
# ==================================================

number = 100
text = "Python"
values = [1, 2, 3]

print("\nIs number an integer?", isinstance(number, int))
print("Is text a string?", isinstance(text, str))
print("Is values a list?", isinstance(values, list))


# ==================================================
# 12. PRACTICAL EXAMPLE
# ==================================================

student_names = ["Alex", "Sam", "Jordan", "Taylor"]

student_marks = [85, 45, 92, 30]

print("\nStudent report:")

for index, (name, mark) in enumerate(
    zip(student_names, student_marks),
    start=1
):
    status = "Pass" if mark >= 40 else "Fail"
    print(index, name, mark, status)

print("Highest mark:", max(student_marks))
print("Lowest mark:", min(student_marks))
print("Average mark:", round(sum(student_marks) / len(student_marks), 2))

print("At least one student passed:",
      any(mark >= 40 for mark in student_marks))

print("All students passed:",
      all(mark >= 40 for mark in student_marks))


# ==================================================
# 13. IMPORTANT DIFFERENCES
# ==================================================

"""
enumerate():
    Gives index and value.

zip():
    Combines corresponding elements.

sorted():
    Returns a new sorted list.

reversed():
    Returns a reverse iterator.

any():
    Checks whether at least one condition is True.

all():
    Checks whether every condition is True.

IMPORTANT:
    list(), tuple() and set() can convert iterables
    into different collection types.
"""
