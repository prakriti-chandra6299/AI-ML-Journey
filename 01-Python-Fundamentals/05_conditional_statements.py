"""
LESSON 5: CONDITIONAL STATEMENTS

REVISION NOTES:

1. Conditional statements are used to make decisions.

2. if:
   Executes a block when the condition is True.

3. elif:
   Checks another condition if the previous condition was False.
   You can use multiple elif blocks.

4. else:
   Executes when all previous conditions are False.

5. Nested if:
   An if statement inside another if statement.

6. Conditional Expression:
   Short form of if-else.
   Syntax: value_if_true if condition else value_if_false

7. Important:
   - Use a colon (:) after if, elif and else.
   - Maintain proper indentation.
   - Python uses indentation to define code blocks.
"""


# --------------------------------------------------
# 1. BASIC IF STATEMENT
# --------------------------------------------------

age = 20

if age >= 18:
    print("You are eligible to vote.")


# --------------------------------------------------
# 2. IF-ELSE STATEMENT
# --------------------------------------------------

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# --------------------------------------------------
# 3. IF-ELIF-ELSE STATEMENT
# --------------------------------------------------

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")


# --------------------------------------------------
# 4. CHECK POSITIVE, NEGATIVE OR ZERO
# --------------------------------------------------

number = -5

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# --------------------------------------------------
# 5. FIND THE GREATER NUMBER
# --------------------------------------------------

a = 25
b = 40

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both numbers are equal")


# --------------------------------------------------
# 6. NESTED IF STATEMENT
# --------------------------------------------------

age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Entry not allowed")


# --------------------------------------------------
# 7. USING LOGICAL OPERATORS IN CONDITIONS
# --------------------------------------------------

age = 21
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")
else:
    print("You cannot enter.")


# --------------------------------------------------
# 8. CONDITIONAL EXPRESSION (SHORT-HAND IF-ELSE)
# --------------------------------------------------

number = 10

result = "Even" if number % 2 == 0 else "Odd"

print("Result:", result)


# --------------------------------------------------
# 9. CHECK VOTING ELIGIBILITY USING USER INPUT
# --------------------------------------------------

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# --------------------------------------------------
# 10. SIMPLE LOGIN CHECK
# --------------------------------------------------

correct_password = "python123"

entered_password = input("Enter password: ")

if entered_password == correct_password:
    print("Login successful")
else:
    print("Incorrect password")


# --------------------------------------------------
# END OF LESSON 5
# --------------------------------------------------