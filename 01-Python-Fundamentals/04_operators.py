
"""
========================================================
TOPIC: OPERATORS IN PYTHON
========================================================

1. OPERATORS
   - Operators perform operations on variables and values.
   - Operands are the values on which operators work.

2. ARITHMETIC OPERATORS
   +   Addition
   -   Subtraction
   *   Multiplication
   /   Division (returns float)
   //  Floor division (quotient rounded down)
   %   Modulus (remainder)
   **  Exponentiation (power)

3. COMPARISON OPERATORS
   ==  Equal to
   !=  Not equal to
   >   Greater than
   <   Less than
   >=  Greater than or equal to
   <=  Less than or equal to
   - Returns True or False.

4. LOGICAL OPERATORS
   and : True if both conditions are True.
   or  : True if at least one condition is True.
   not : Reverses the Boolean result.

5. ASSIGNMENT OPERATORS
   =   Assign
   +=  Add and assign
   -=  Subtract and assign
   *=  Multiply and assign
   /=  Divide and assign
   //= Floor divide and assign
   %=  Modulus and assign
   **= Power and assign

6. MEMBERSHIP OPERATORS
   in     : Checks whether a value exists in a sequence.
   not in : Checks whether a value does not exist.

7. IDENTITY OPERATORS
   is     : Checks whether two references point to
            the same object.
   is not : Checks whether they point to different objects.
   - Do not confuse identity (is) with equality (==).

8. BITWISE OPERATORS
   &   AND
   |   OR
   ^   XOR
   ~   NOT
   <<  Left shift
   >>  Right shift

9. OPERATOR PRECEDENCE
   - Parentheses are evaluated first.
   - Exponentiation has high precedence.
   - Multiplication, division, floor division and
     modulus come before addition and subtraction.
   - Comparison operators are evaluated after arithmetic.
   - not, and, or follow in that order.
   - Use parentheses to make expressions clear.

========================================================
"""


# ------------------------------------------------------
# 1. ARITHMETIC OPERATORS
# ------------------------------------------------------

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# ------------------------------------------------------
# 2. COMPARISON OPERATORS
# ------------------------------------------------------

x = 15
y = 10

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# ------------------------------------------------------
# 3. LOGICAL OPERATORS
# ------------------------------------------------------

age = 22
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# ------------------------------------------------------
# 4. ASSIGNMENT OPERATORS
# ------------------------------------------------------

number = 10

number += 5
print("After += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 4
print("After /= :", number)

number = 10
number //= 3
print("After //= :", number)

number = 10
number %= 3
print("After %= :", number)

number = 2
number **= 3
print("After **= :", number)


# ------------------------------------------------------
# 5. MEMBERSHIP OPERATORS
# ------------------------------------------------------

languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("JavaScript" not in languages)


# ------------------------------------------------------
# 6. IDENTITY OPERATORS
# ------------------------------------------------------

list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

print(list1 == list2)  # Same values
print(list1 is list2)  # Different objects
print(list1 is list3)  # Same object


# ------------------------------------------------------
# 7. BITWISE OPERATORS
# ------------------------------------------------------

a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# ------------------------------------------------------
# 8. OPERATOR PRECEDENCE
# ------------------------------------------------------

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2
result3 = 2 ** 3 * 2

print(result1)
print(result2)
print(result3)


# ------------------------------------------------------
# 9. PRACTICAL EXAMPLE: SIMPLE BILL CALCULATOR
# ------------------------------------------------------

item_price = 250
quantity = 3
discount = 50

total = item_price * quantity
final_amount = total - discount

print("Total Amount:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
