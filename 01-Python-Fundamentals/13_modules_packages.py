
"""
LESSON 13: MODULES AND PACKAGES IN PYTHON

REVISION NOTES:

1. MODULE:
   A Python file containing reusable code.
   Example: math, random, statistics.

2. PACKAGE:
   A directory containing related Python modules.

3. IMPORT:
   import math
   Imports the complete module.

4. FROM IMPORT:
   from math import sqrt
   Imports a specific function.

5. ALIAS:
   import math as m
   Gives a module a shorter name.

6. BUILT-IN MODULES:
   math      -> Mathematical operations.
   random    -> Random values.
   statistics -> Statistical calculations.
   datetime  -> Date and time operations.
   os        -> Operating system interaction.

7. PIP:
   Python's package installer.
   Example: python -m pip install package_name

8. __name__:
   When a Python file runs directly,
   __name__ becomes "__main__".

9. CUSTOM MODULE:
   A Python file created by you can be imported
   into another Python file.
"""


# --------------------------------------------------
# 1. IMPORTING A MODULE
# --------------------------------------------------

import math

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))


# --------------------------------------------------
# 2. IMPORTING SPECIFIC FUNCTIONS
# --------------------------------------------------

from math import sqrt, pow

print(sqrt(64))
print(pow(2, 3))


# --------------------------------------------------
# 3. USING ALIAS
# --------------------------------------------------

import math as m

print(m.sqrt(100))
print(m.pi)


# --------------------------------------------------
# 4. RANDOM MODULE
# --------------------------------------------------

import random

print(random.randint(1, 10))
print(random.random())

fruits = ["Apple", "Mango", "Banana"]

print(random.choice(fruits))


# --------------------------------------------------
# 5. SHUFFLING A LIST
# --------------------------------------------------

import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)


# --------------------------------------------------
# 6. STATISTICS MODULE
# --------------------------------------------------

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))


# --------------------------------------------------
# 7. DATETIME MODULE
# --------------------------------------------------

import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().time()

print("Date:", current_date)
print("Time:", current_time)


# --------------------------------------------------
# 8. WORKING WITH DATE
# --------------------------------------------------

import datetime

today = datetime.date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# --------------------------------------------------
# 9. OS MODULE
# --------------------------------------------------

import os

print("Current directory:", os.getcwd())
print("Operating system:", os.name)


# --------------------------------------------------
# 10. USING DIR()
# --------------------------------------------------

import math

print(dir(math))


# --------------------------------------------------
# 11. USING __NAME__
# --------------------------------------------------

print("Current module name:", __name__)

if __name__ == "__main__":
    print("This file is running directly.")


# --------------------------------------------------
# 12. CUSTOM MODULE EXAMPLE
# --------------------------------------------------

# We will create a separate custom module
# in the next section of this lesson.


# --------------------------------------------------
# END OF LESSON 13
# --------------------------------------------------
