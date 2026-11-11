
"""
LESSON 21: ITERATORS AND ITERABLES IN PYTHON

REVISION NOTES:

1. Iterable: An object whose elements can be accessed one by one.
2. Examples: List, tuple, string, set and dictionary.
3. Iterator: An object that produces elements one at a time.
4. iter(): Converts an iterable into an iterator.
5. next(): Retrieves the next element from an iterator.
6. StopIteration: Exception raised when an iterator is exhausted.
7. __iter__(): Returns an iterator.
8. __next__(): Returns the next element.

IMPORTANT DIFFERENCE:

Iterable = Can provide an iterator.
Iterator = Produces elements one at a time.

SYNTAX:

iterator = iter(iterable)
element = next(iterator)
"""

# --------------------------------------------------
# 1. Understanding an iterable
# --------------------------------------------------

numbers = [10, 20, 30, 40]

print("Iterable Example:")

for number in numbers:
    print(number)


# --------------------------------------------------
# 2. Using iter()
# --------------------------------------------------

numbers = [10, 20, 30]

iterator = iter(numbers)

print("\nUsing iter():")

print(next(iterator))
print(next(iterator))
print(next(iterator))


# --------------------------------------------------
# 3. Understanding StopIteration
# --------------------------------------------------

numbers = [1, 2]

iterator = iter(numbers)

print("\nStopIteration Example:")

print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))

except StopIteration:
    print("No more elements available.")


# --------------------------------------------------
# 4. Iterating through a string
# --------------------------------------------------

word = "PYTHON"

iterator = iter(word)

print("\nString Iterator:")

print(next(iterator))
print(next(iterator))
print(next(iterator))


# --------------------------------------------------
# 5. Iterating through a tuple
# --------------------------------------------------

colors = ("Red", "Green", "Blue")

iterator = iter(colors)

print("\nTuple Iterator:")

print(next(iterator))
print(next(iterator))
print(next(iterator))


# --------------------------------------------------
# 6. Iterating through a dictionary
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 20,
    "marks": 90
}

iterator = iter(student)

print("\nDictionary Iterator:")

print(next(iterator))
print(next(iterator))
print(next(iterator))


# --------------------------------------------------
# 7. Creating a custom iterator
# --------------------------------------------------

class Count:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Count(5)

print("\nCustom Iterator:")

for number in counter:
    print(number)


# --------------------------------------------------
# 8. Checking iterable and iterator
# --------------------------------------------------

numbers = [10, 20, 30]

iterator = iter(numbers)

print("\nChecking Types:")

print("List has __iter__:", hasattr(numbers, "__iter__"))
print("List has __next__:", hasattr(numbers, "__next__"))

print("Iterator has __iter__:", hasattr(iterator, "__iter__"))
print("Iterator has __next__:", hasattr(iterator, "__next__"))


# --------------------------------------------------
# 9. Using iter() with a sentinel value
# --------------------------------------------------

def get_number():
    return 5


print("\nSentinel Iterator:")

for value in iter(get_number, 0):
    print(value)
    break


# --------------------------------------------------
# 10. Practical example: Reading a list of tasks
# --------------------------------------------------

tasks = [
    "Study Python",
    "Practice coding",
    "Revise concepts",
    "Complete assignments"
]

task_iterator = iter(tasks)

print("\nStudy Tasks:")

while True:

    try:
        task = next(task_iterator)
        print(task)

    except StopIteration:
        print("All tasks completed.")
        break


# --------------------------------------------------
# END OF LESSON 21
# --------------------------------------------------
