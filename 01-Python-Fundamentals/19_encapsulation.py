
"""
LESSON 19: ENCAPSULATION IN PYTHON

REVISION NOTES:

1. Encapsulation combines data and methods inside a class.
2. It controls how object data is accessed and modified.
3. Public members: Accessible from anywhere.
4. Protected members: Written with a single underscore (_).
5. Private members: Written with double underscores (__).
6. Getter: A method used to retrieve a value.
7. Setter: A method used to update a value.
8. @property provides controlled attribute access.

NAMING CONVENTIONS:

Public:     self.name
Protected:  self._salary
Private:    self.__balance

IMPORTANT:
Python uses naming conventions and name mangling.
A single or double underscore does not provide
absolute security or strict access restrictions.
"""

# --------------------------------------------------
# 1. Public members
# --------------------------------------------------

class Student:

    def __init__(self, name):
        self.name = name


student = Student("Alex")

print("Public Attribute:")
print(student.name)


# --------------------------------------------------
# 2. Protected members
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self._salary)


employee = Employee("Sam", 30000)

print("\nProtected Attribute:")
employee.display()

# Accessible, but intended for internal use.
print(employee._salary)


# --------------------------------------------------
# 3. Private members
# --------------------------------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def display_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

print("\nPrivate Attribute:")
account.display_balance()

# Direct access normally raises AttributeError.
# Uncomment the next line to see the error:
# print(account.__balance)


# --------------------------------------------------
# 4. Getter method
# --------------------------------------------------

class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


person = Person(21)

print("\nGetter:")
print("Age:", person.get_age())


# --------------------------------------------------
# 5. Setter method
# --------------------------------------------------

class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")


person = Person(20)

print("\nBefore updating:", person.get_age())

person.set_age(22)

print("After updating:", person.get_age())

person.set_age(-5)


# --------------------------------------------------
# 6. Using @property
# --------------------------------------------------

class StudentInfo:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")


student = StudentInfo(85)

print("\nUsing Property:")
print("Marks:", student.marks)

student.marks = 95

print("Updated Marks:", student.marks)

student.marks = 150


# --------------------------------------------------
# 7. Name mangling
# --------------------------------------------------

class Example:

    def __init__(self):
        self.__value = 100


obj = Example()

print("\nName Mangling:")

# Python internally changes __value to _Example__value.
# This is not recommended for normal access.
print(obj._Example__value)


# --------------------------------------------------
# 8. Practical example: Bank Account
# --------------------------------------------------

class SecureBankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > self.__balance:
            print("Insufficient balance.")

        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def get_balance(self):
        return self.__balance


account = SecureBankAccount("Alex", 5000)

print("\nSecure Bank Account:")

account.deposit(2000)
account.withdraw(1000)

print("Account Holder:", account.holder)
print("Current Balance:", account.get_balance())


# --------------------------------------------------
# END OF LESSON 19
# --------------------------------------------------
