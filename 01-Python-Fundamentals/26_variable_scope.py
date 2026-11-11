
"""
LESSON 26: VARIABLE SCOPE IN PYTHON

REVISION NOTES
--------------
1. Scope determines where a variable can be accessed.

2. Local Variable:
   Created inside a function.
   Accessible only inside that function.

3. Global Variable:
   Created outside all functions.
   Accessible throughout the module.

4. global Keyword:
   Allows a function to modify a global variable.

5. nonlocal Keyword:
   Allows an inner function to modify a variable
   belonging to its enclosing function.

6. LEGB Rule:
   Python searches for variables in this order:
   L - Local
   E - Enclosing
   G - Global
   B - Built-in
"""

# ==================================================
# 1. LOCAL VARIABLES
# ==================================================

def show_number():
    number = 10
    print("Local variable:", number)


show_number()

# number cannot be accessed outside show_number().
# Uncommenting the next line causes NameError.
# print(number)


# ==================================================
# 2. GLOBAL VARIABLES
# ==================================================

message = "Welcome to Python"


def display_message():
    print("Global variable:", message)


display_message()
print("Accessing global variable outside:", message)


# ==================================================
# 3. LOCAL AND GLOBAL VARIABLES WITH SAME NAME
# ==================================================

value = 100


def show_value():
    value = 50
    print("Inside function:", value)


show_value()
print("Outside function:", value)


# ==================================================
# 4. MODIFYING GLOBAL VARIABLES
# ==================================================

counter = 0


def increase_counter():
    global counter
    counter += 1


increase_counter()
increase_counter()
increase_counter()

print("\nGlobal counter:", counter)


# ==================================================
# 5. ENCLOSING SCOPE
# ==================================================

def outer_function():

    message = "Hello from outer function"

    def inner_function():
        print("Enclosing variable:", message)

    inner_function()


outer_function()


# ==================================================
# 6. NONLOCAL KEYWORD
# ==================================================

def outer_counter():

    count = 0

    def inner_counter():
        nonlocal count
        count += 1

    inner_counter()
    inner_counter()
    inner_counter()

    print("\nNonlocal counter:", count)


outer_counter()


# ==================================================
# 7. LEGB RULE
# ==================================================

name = "Global Name"


def outer_function():

    name = "Enclosing Name"

    def inner_function():

        name = "Local Name"

        print("LEGB example:", name)

    inner_function()


outer_function()


# ==================================================
# 8. BUILT-IN SCOPE
# ==================================================

# print(), len(), sum(), max() are built-in functions.

numbers = [10, 20, 30, 40]

print("\nBuilt-in len():", len(numbers))
print("Built-in sum():", sum(numbers))
print("Built-in max():", max(numbers))


# ==================================================
# 9. VARIABLE SCOPE IN LOOPS
# ==================================================

for number in range(1, 4):
    result = number * 2

print("\nVariable created in loop:", result)

# In Python, a for loop does not create a separate
# local scope. The variable remains accessible here.


# ==================================================
# 10. IMPORTANT DIFFERENCES
# ==================================================

"""
LOCAL:
    Defined inside a function.

GLOBAL:
    Defined at module level.

ENCLOSING:
    Defined in an outer function containing
    another inner function.

BUILT-IN:
    Names provided by Python, such as print and len.

global:
    Modify a module-level variable.

nonlocal:
    Modify a variable in an enclosing function.

LEGB:
    Local -> Enclosing -> Global -> Built-in.
"""
