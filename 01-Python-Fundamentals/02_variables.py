
"""
========================================================
TOPIC: VARIABLES AND DATA TYPES IN PYTHON
========================================================

1. VARIABLES
   - Variables are names used to store data.
   - Python does not require explicit variable declarations.
   - Use the assignment operator (=) to assign values.

2. NAMING RULES
   - Must start with a letter or underscore (_).
   - Cannot start with a number.
   - Cannot contain spaces.
   - Names are case-sensitive.
   - Cannot use Python keywords.
   - Use snake_case for variable names.

3. BASIC DATA TYPES
   - int       : Whole numbers (10, 25, -5)
   - float     : Decimal numbers (3.14, 8.5)
   - str       : Text ("Python", "Hello")
   - bool      : True or False
   - NoneType  : Represents no value (None)

4. TYPE CHECKING
   - type(variable) returns the data type.

5. TYPE CONVERSION
   - int()   : Converts to integer (where valid)
   - float() : Converts to float (where valid)
   - str()   : Converts to string
   - bool()  : Converts to boolean

6. IMPORTANT CONCEPTS
   - Python is dynamically typed.
   - A variable can be reassigned with a different data type.
   - Use meaningful variable names.
   - Python is case-sensitive.
   - Multiple variables can be assigned in one statement.
   - Multiple variables can share the same value.

========================================================
"""


# ------------------------------------------------------
# 1. CREATING VARIABLES AND ASSIGNING VALUES
# ------------------------------------------------------

# Integer
age = 21

# Float
price = 99.50

# String
course = "Python Programming"

# Boolean
is_learning = True

# None
result = None

print(age)
print(price)
print(course)
print(is_learning)
print(result)


# ------------------------------------------------------
# 2. CHECKING DATA TYPES
# ------------------------------------------------------

age = 21
price = 99.50
course = "Python"
is_learning = True

print(type(age))
print(type(price))
print(type(course))
print(type(is_learning))


# ------------------------------------------------------
# 3. TYPE CONVERSION
# ------------------------------------------------------

number = "100"

converted_number = int(number)

print(converted_number)
print(type(converted_number))

# Other examples
x = 10
print(float(x))

y = 25
print(str(y))

z = 0
print(bool(z))


# ------------------------------------------------------
# 4. DYNAMIC TYPING
# ------------------------------------------------------

value = 100
print(value, type(value))

value = "Hello"
print(value, type(value))


# ------------------------------------------------------
# 5. CASE-SENSITIVE VARIABLES
# ------------------------------------------------------

name = "Alex"
Name = "Sam"

print(name)
print(Name)


# ------------------------------------------------------
# 6. MULTIPLE ASSIGNMENT
# ------------------------------------------------------

a, b, c = 10, 20, 30

print(a, b, c)


# ------------------------------------------------------
# 7. ASSIGNING SAME VALUE TO MULTIPLE VARIABLES
# ------------------------------------------------------

x = y = z = 100

print(x, y, z)

