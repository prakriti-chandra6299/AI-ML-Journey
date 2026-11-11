
"""
LESSON 16: OBJECT-ORIENTED PROGRAMMING (OOP)

REVISION NOTES:

1. Class: A blueprint for creating objects.
2. Object: An instance of a class.
3. Attribute: A variable belonging to an object or class.
4. Method: A function defined inside a class.
5. __init__(): Constructor that initializes an object.
6. self: Refers to the current object.
7. Instance attributes: Belong to individual objects.
8. Class attributes: Shared by all instances unless overridden.

SYNTAX:

class ClassName:
    def __init__(self, parameters):
        self.attribute = parameters

    def method(self):
        # Method code

object_name = ClassName(arguments)

"""

# --------------------------------------------------
# 1. Creating a basic class
# --------------------------------------------------

class Student:
    name = "Alex"
    age = 20


# Creating an object
student1 = Student()

print("Name:", student1.name)
print("Age:", student1.age)


# --------------------------------------------------
# 2. Creating multiple objects
# --------------------------------------------------

class Car:
    brand = "Toyota"

car1 = Car()
car2 = Car()

print("\nCar 1:", car1.brand)
print("Car 2:", car2.brand)


# --------------------------------------------------
# 3. Using the constructor (__init__)
# --------------------------------------------------

class StudentInfo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


student1 = StudentInfo("Alex", 20)
student2 = StudentInfo("Sam", 21)

print("\nStudent Details:")

student1.display()
student2.display()


# --------------------------------------------------
# 4. Instance attributes
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("John", 30000)
employee2 = Employee("David", 40000)

print("\nEmployee 1:", employee1.name, employee1.salary)
print("Employee 2:", employee2.name, employee2.salary)


# --------------------------------------------------
# 5. Class attributes
# --------------------------------------------------

class College:

    college_name = "ABC Institute"

    def __init__(self, student_name):
        self.student_name = student_name


student1 = College("Alex")
student2 = College("Sam")

print("\nCollege:", student1.college_name)
print("Student 1:", student1.student_name)
print("Student 2:", student2.student_name)


# --------------------------------------------------
# 6. Instance methods
# --------------------------------------------------

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print("\nAddition:", calc.add(10, 20))
print("Multiplication:", calc.multiply(5, 4))


# --------------------------------------------------
# 7. Modifying object attributes
# --------------------------------------------------

class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


mobile1 = Mobile("Samsung", 25000)

print("\nOriginal Price:", mobile1.price)

mobile1.price = 30000

print("Updated Price:", mobile1.price)


# --------------------------------------------------
# 8. Practical example: Bank Account
# --------------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


account = BankAccount("Alex", 5000)

print("\nBank Account Details:")

account.deposit(2000)
account.withdraw(1000)
account.display_balance()


# --------------------------------------------------
# 9. Using type() and isinstance()
# --------------------------------------------------

print("\nObject Type:", type(student1))
print("Is student1 a College object?", isinstance(student1, College))


# --------------------------------------------------
# END OF LESSON 16
# --------------------------------------------------
