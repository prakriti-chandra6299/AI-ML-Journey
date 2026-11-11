"""
LESSON 6: LOOPS IN PYTHON

REVISION NOTES:

1. Loops execute a block of code repeatedly.

2. FOR LOOP:
   Used to iterate over a sequence or range.

   Syntax:
   for variable in sequence:
       statements

3. WHILE LOOP:
   Repeats as long as a condition is True.

   Syntax:
   while condition:
       statements

4. range():
   Generates a sequence of numbers.
   range(start, stop, step)
   The stop value is excluded.

5. break:
   Immediately terminates the loop.

6. continue:
   Skips the current iteration and moves to the next one.

7. pass:
   Acts as a placeholder and does nothing.

8. Nested loops:
   A loop inside another loop.

9. IMPORTANT:
   - Maintain proper indentation.
   - Update the condition variable in while loops.
   - Otherwise, an infinite loop may occur.
"""


# --------------------------------------------------
# 1. BASIC FOR LOOP
# --------------------------------------------------

for i in range(5):
    print(i)


# --------------------------------------------------
# 2. FOR LOOP WITH START AND STOP
# --------------------------------------------------

for i in range(1, 6):
    print(i)


# --------------------------------------------------
# 3. FOR LOOP WITH STEP
# --------------------------------------------------

for i in range(2, 11, 2):
    print(i)


# --------------------------------------------------
# 4. LOOP THROUGH A STRING
# --------------------------------------------------

name = "Python"

for character in name:
    print(character)


# --------------------------------------------------
# 5. LOOP THROUGH A LIST
# --------------------------------------------------

languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)


# --------------------------------------------------
# 6. BASIC WHILE LOOP
# --------------------------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1


# --------------------------------------------------
# 7. BREAK STATEMENT
# --------------------------------------------------

for i in range(1, 11):
    if i == 5:
        break

    print(i)


# --------------------------------------------------
# 8. CONTINUE STATEMENT
# --------------------------------------------------

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# --------------------------------------------------
# 9. PASS STATEMENT
# --------------------------------------------------

for i in range(1, 6):
    if i == 3:
        pass

    print(i)


# --------------------------------------------------
# 10. NESTED FOR LOOP
# --------------------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# --------------------------------------------------
# 11. MULTIPLICATION TABLE
# --------------------------------------------------

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# --------------------------------------------------
# 12. SUM OF FIRST N NATURAL NUMBERS
# --------------------------------------------------

n = 10
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# --------------------------------------------------
# 13. REVERSE COUNTDOWN USING WHILE
# --------------------------------------------------

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Finished!")


# --------------------------------------------------
# 14. USING ELSE WITH A LOOP
# --------------------------------------------------

for i in range(1, 4):
    print(i)
else:
    print("Loop completed successfully.")


# --------------------------------------------------
# END OF LESSON 6
# --------------------------------------------------