
"""
LESSON 22: GENERATORS IN PYTHON

REVISION NOTES:

1. Generator: A special function that produces values one at a time.
2. yield: Returns a value and pauses the function.
3. next(): Retrieves the next generated value.
4. A generator remembers its execution state.
5. Generators are memory-efficient.
6. Generators are iterators.
7. Once exhausted, a generator cannot be reused.

DIFFERENCE:

return:
- Returns a value.
- Terminates the function.

yield:
- Produces a value.
- Pauses the function.
- Continues from the same point when requested again.

SYNTAX:

def generator_function():
    yield value

generator = generator_function()
"""

# --------------------------------------------------
# 1. Creating a basic generator
# --------------------------------------------------

def simple_generator():
    yield 10
    yield 20
    yield 30


gen = simple_generator()

print("Basic Generator:")

print(next(gen))
print(next(gen))
print(next(gen))


# --------------------------------------------------
# 2. Generator using a loop
# --------------------------------------------------

def number_generator():
    for number in range(1, 6):
        yield number


print("\nGenerator with Loop:")

for number in number_generator():
    print(number)


# --------------------------------------------------
# 3. Understanding yield and execution
# --------------------------------------------------

def demo_generator():
    print("First execution")
    yield 1

    print("Second execution")
    yield 2

    print("Third execution")
    yield 3


gen = demo_generator()

print("\nExecution Flow:")

print(next(gen))
print(next(gen))
print(next(gen))


# --------------------------------------------------
# 4. Generator expression
# --------------------------------------------------

squares = (number ** 2 for number in range(1, 6))

print("\nGenerator Expression:")

for square in squares:
    print(square)


# --------------------------------------------------
# 5. Difference between list and generator
# --------------------------------------------------

numbers_list = [number for number in range(1, 6)]

numbers_generator = (
    number for number in range(1, 6)
)

print("\nList:", numbers_list)
print("Generator:", numbers_generator)

print("Generator values:", list(numbers_generator))


# --------------------------------------------------
# 6. Generator for even numbers
# --------------------------------------------------

def even_numbers(limit):

    for number in range(2, limit + 1, 2):
        yield number


print("\nEven Numbers:")

for number in even_numbers(20):
    print(number)


# --------------------------------------------------
# 7. Generator for Fibonacci sequence
# --------------------------------------------------

def fibonacci(limit):

    a, b = 0, 1

    for _ in range(limit):
        yield a
        a, b = b, a + b


print("\nFibonacci Sequence:")

for number in fibonacci(10):
    print(number)


# --------------------------------------------------
# 8. Handling StopIteration
# --------------------------------------------------

def small_generator():
    yield "Python"
    yield "Machine Learning"


gen = small_generator()

print("\nStopIteration Example:")

print(next(gen))
print(next(gen))

try:
    print(next(gen))

except StopIteration:
    print("Generator is exhausted.")


# --------------------------------------------------
# 9. Generator with conditional statements
# --------------------------------------------------

def positive_numbers(numbers):

    for number in numbers:

        if number > 0:
            yield number


values = [-5, 10, -2, 20, 0, 30]

print("\nPositive Numbers:")

for number in positive_numbers(values):
    print(number)


# --------------------------------------------------
# 10. Practical example: Processing large data
# --------------------------------------------------

def data_generator():

    for number in range(1, 6):
        print("Generating data:", number)
        yield number


print("\nProcessing Data:")

for data in data_generator():
    print("Processing:", data)


# --------------------------------------------------
# END OF LESSON 22
# --------------------------------------------------
