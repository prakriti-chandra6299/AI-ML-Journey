
"""
LESSON 25: RECURSION IN PYTHON

REVISION NOTES
--------------
1. Recursion:
   A function calling itself is called recursion.

2. Base Case:
   The condition that stops recursion.

3. Recursive Case:
   The part where the function calls itself.

4. Without a proper base case, recursion may continue
   until Python raises RecursionError.

5. Each recursive call gets its own function call frame.

6. Recursion is useful for:
   - Factorial
   - Fibonacci series
   - Tree traversal
   - Searching and sorting
   - Backtracking problems
"""

# ==================================================
# 1. BASIC RECURSION
# ==================================================

def countdown(number):

    # Base case
    if number == 0:
        print("Done!")
        return

    # Print current number
    print(number)

    # Recursive call
    countdown(number - 1)


print("Countdown:")
countdown(5)


# ==================================================
# 2. FACTORIAL USING RECURSION
# ==================================================

# Factorial:
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(number):

    # Base case
    if number == 0 or number == 1:
        return 1

    # Recursive case
    return number * factorial(number - 1)


print("\nFactorial of 5:", factorial(5))
print("Factorial of 6:", factorial(6))


# ==================================================
# 3. SUM OF NATURAL NUMBERS
# ==================================================

# 1 + 2 + 3 + 4 + 5 = 15

def natural_sum(number):

    if number == 0:
        return 0

    return number + natural_sum(number - 1)


print("\nSum of first 5 natural numbers:", natural_sum(5))


# ==================================================
# 4. FIBONACCI USING RECURSION
# ==================================================

# Fibonacci:
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(number):

    # Base cases
    if number == 0:
        return 0

    if number == 1:
        return 1

    # Recursive case
    return fibonacci(number - 1) + fibonacci(number - 2)


print("\nFibonacci sequence:")

for i in range(7):
    print(fibonacci(i), end=" ")

print()


# ==================================================
# 5. POWER OF A NUMBER
# ==================================================

# 2^4 = 2 * 2 * 2 * 2 = 16

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print("\n2 raised to power 4:", power(2, 4))


# ==================================================
# 6. REVERSE A STRING
# ==================================================

def reverse_string(text):

    if len(text) == 0:
        return text

    return reverse_string(text[1:]) + text[0]


print("\nReversed string:", reverse_string("python"))


# ==================================================
# 7. GREATEST COMMON DIVISOR (GCD)
# ==================================================

# Euclidean algorithm:
# GCD(a, b) = GCD(b, a % b)

def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


print("\nGCD of 24 and 36:", gcd(24, 36))


# ==================================================
# 8. RECURSION WITH A LIST
# ==================================================

def list_sum(numbers):

    if len(numbers) == 0:
        return 0

    return numbers[0] + list_sum(numbers[1:])


values = [10, 20, 30, 40]

print("\nSum of list elements:", list_sum(values))


# ==================================================
# 9. UNDERSTANDING RECURSION FLOW
# ==================================================

"""
Example: factorial(4)

factorial(4)
    = 4 * factorial(3)
    = 4 * 3 * factorial(2)
    = 4 * 3 * 2 * factorial(1)
    = 4 * 3 * 2 * 1

Final answer = 24

The function calls itself until it reaches
the base case. Then the results return backward.
"""


# ==================================================
# 10. RECURSION VS ITERATION
# ==================================================

"""
RECURSION:
    A function calls itself.
    Uses the function call stack.
    Can make some problems easier to express.

ITERATION:
    Uses loops such as for and while.
    Usually uses less call-stack memory.
    Often preferable for simple repetition.

IMPORTANT:
    Python has a recursion depth limit.
    Avoid recursion when a simple loop is clearer.
"""
