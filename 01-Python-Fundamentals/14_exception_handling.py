
"""
LESSON 14: EXCEPTION HANDLING IN PYTHON

REVISION NOTES:
1. Exception: An error that occurs while a program is running.
2. try: Contains code that might cause an error.
3. except: Handles an error.
4. else: Executes when no exception occurs.
5. finally: Always executes, whether an error occurs or not.
6. raise: Used to raise an exception manually.

COMMON EXCEPTIONS:
- ZeroDivisionError: Dividing by zero.
- ValueError: Invalid value or conversion.
- TypeError: Invalid operation between data types.
- IndexError: Accessing an invalid list index.
- KeyError: Accessing a missing dictionary key.
- FileNotFoundError: Opening a file that does not exist.

SYNTAX:

try:
    risky_code
except ErrorType:
    handle_error
else:
    execute_if_no_error
finally:
    always_execute
"""

# --------------------------------------------------
# 1. Basic try and except
# --------------------------------------------------

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero!")


# --------------------------------------------------
# 2. Handling ValueError
# --------------------------------------------------

try:
    number = int("hello")
    print(number)

except ValueError:
    print("Please provide a valid integer.")


# --------------------------------------------------
# 3. Handling multiple exceptions
# --------------------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Invalid input! Enter an integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# --------------------------------------------------
# 4. Using else
# --------------------------------------------------

try:
    number = int("25")

except ValueError:
    print("Conversion failed.")

else:
    print("Conversion successful:", number)


# --------------------------------------------------
# 5. Using finally
# --------------------------------------------------

try:
    print("Program is running.")

except Exception:
    print("An error occurred.")

finally:
    print("This block always executes.")


# --------------------------------------------------
# 6. Using try, except, else and finally together
# --------------------------------------------------

try:
    number = int("50")
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Something went wrong.")

else:
    print("Final result:", result)

finally:
    print("Calculation completed.")


# --------------------------------------------------
# 7. Handling IndexError
# --------------------------------------------------

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("List index does not exist.")


# --------------------------------------------------
# 8. Handling KeyError
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 20
}

try:
    print(student["grade"])

except KeyError:
    print("The requested key does not exist.")


# --------------------------------------------------
# 9. Using raise
# --------------------------------------------------

age = 15

try:
    if age < 18:
        raise ValueError("Age must be at least 18.")

    print("Access granted.")

except ValueError as error:
    print("Error:", error)


# --------------------------------------------------
# 10. Catching the exception message
# --------------------------------------------------

try:
    result = 10 / 0

except Exception as error:
    print("Error occurred:", error)


# --------------------------------------------------
# 11. Practical example: Safe division function
# --------------------------------------------------

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(20, 5))
print(divide(20, 0))


# --------------------------------------------------
# END OF LESSON 14
# --------------------------------------------------
