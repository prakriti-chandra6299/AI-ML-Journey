
"""
LESSON 12: FUNCTIONS IN PYTHON

REVISION NOTES:

1. A function is a reusable block of code.

2. FUNCTION DEFINITION:
   def function_name():
       statements

3. FUNCTION CALL:
   function_name()

4. PARAMETERS:
   Variables written inside the function definition.

5. ARGUMENTS:
   Actual values passed when calling a function.

6. RETURN:
   Sends a result back from a function.

7. TYPES OF ARGUMENTS:
   - Positional arguments
   - Keyword arguments
   - Default arguments
   - Variable-length positional arguments (*args)
   - Variable-length keyword arguments (**kwargs)

8. LAMBDA FUNCTION:
   A small anonymous function.
   Syntax: lambda arguments: expression

9. RECURSION:
   A function calling itself.

10. SCOPE:
    - Local variable: Defined inside a function.
    - Global variable: Defined outside a function.

11. IMPORTANT:
    print() displays a value.
    return sends a value back to the caller.
"""


# --------------------------------------------------
# 1. BASIC FUNCTION
# --------------------------------------------------

def greet():
    print("Hello, welcome to Python!")


greet()


# --------------------------------------------------
# 2. FUNCTION WITH PARAMETERS
# --------------------------------------------------

def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Alex")
greet_user("Sam")


# --------------------------------------------------
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# --------------------------------------------------

def add(a, b):
    print("Sum:", a + b)


add(10, 20)


# --------------------------------------------------
# 4. FUNCTION USING RETURN
# --------------------------------------------------

def multiply(a, b):
    return a * b


result = multiply(5, 4)

print("Product:", result)


# --------------------------------------------------
# 5. PRINT VS RETURN
# --------------------------------------------------

def function_one():
    print(10)


def function_two():
    return 10


result1 = function_one()
result2 = function_two()

print("Print function result:", result1)
print("Return function result:", result2)


# --------------------------------------------------
# 6. DEFAULT ARGUMENTS
# --------------------------------------------------

def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Alex")


# --------------------------------------------------
# 7. POSITIONAL ARGUMENTS
# --------------------------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Alex", 21)


# --------------------------------------------------
# 8. KEYWORD ARGUMENTS
# --------------------------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(age=22, name="Sam")


# --------------------------------------------------
# 9. VARIABLE-LENGTH ARGUMENTS (*args)
# --------------------------------------------------

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(10, 20, 30, 40))


# --------------------------------------------------
# 10. VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
# --------------------------------------------------

def display_details(**details):
    for key, value in details.items():
        print(key, ":", value)


display_details(
    name="Alex",
    age=21,
    course="Computer Science"
)


# --------------------------------------------------
# 11. FUNCTION WITH CONDITIONAL STATEMENT
# --------------------------------------------------

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))


# --------------------------------------------------
# 12. FUNCTION WITH A LOOP
# --------------------------------------------------

def multiplication_table(number):

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


multiplication_table(5)


# --------------------------------------------------
# 13. LAMBDA FUNCTION
# --------------------------------------------------

square = lambda number: number ** 2

print(square(5))


# --------------------------------------------------
# 14. LAMBDA WITH MULTIPLE ARGUMENTS
# --------------------------------------------------

add = lambda a, b: a + b

print(add(10, 20))


# --------------------------------------------------
# 15. RECURSION: FACTORIAL
# --------------------------------------------------

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))


# --------------------------------------------------
# 16. RECURSION: FIBONACCI
# --------------------------------------------------

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


for i in range(7):
    print(fibonacci(i), end=" ")

print()


# --------------------------------------------------
# 17. LOCAL VARIABLES
# --------------------------------------------------

def show_number():
    number = 100
    print("Inside function:", number)


show_number()


# --------------------------------------------------
# 18. GLOBAL VARIABLES
# --------------------------------------------------

number = 50


def show_global():
    print("Global number:", number)


show_global()


# --------------------------------------------------
# 19. USING GLOBAL KEYWORD
# --------------------------------------------------

counter = 0


def increase_counter():
    global counter
    counter += 1


increase_counter()
increase_counter()

print("Counter:", counter)


# --------------------------------------------------
# 20. PRACTICAL EXAMPLE: SIMPLE CALCULATOR
# --------------------------------------------------

def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"

        return a / b

    else:
        return "Invalid operator"


print(calculator(20, 10, "+"))
print(calculator(20, 10, "-"))
print(calculator(20, 10, "*"))
print(calculator(20, 10, "/"))


# --------------------------------------------------
# END OF LESSON 12
# --------------------------------------------------
 