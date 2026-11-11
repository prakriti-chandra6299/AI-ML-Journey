
"""
LESSON 20: ABSTRACTION IN PYTHON

REVISION NOTES:

1. Abstraction hides implementation details.
2. It shows only essential features to the user.
3. Abstract class: A class that contains one or more abstract methods.
4. Abstract method: A method declared without its implementation.
5. abc: Python's Abstract Base Class module.
6. ABC: Base class used to create abstract classes.
7. @abstractmethod: Decorator used to declare abstract methods.
8. Abstract classes cannot be instantiated directly.
9. Child classes must implement inherited abstract methods.

IMPORTANT IMPORTS:

from abc import ABC, abstractmethod

SYNTAX:

class Parent(ABC):

    @abstractmethod
    def method(self):
        pass
"""

from abc import ABC, abstractmethod


# --------------------------------------------------
# 1. Creating an abstract class
# --------------------------------------------------

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# --------------------------------------------------
# 2. Implementing an abstract method
# --------------------------------------------------

class Dog(Animal):

    def sound(self):
        print("Dog barks.")


class Cat(Animal):

    def sound(self):
        print("Cat meows.")


dog = Dog()
cat = Cat()

print("Abstract Method Implementation:")

dog.sound()
cat.sound()


# --------------------------------------------------
# 3. Abstract class with multiple abstract methods
# --------------------------------------------------

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle(10, 5)

print("\nRectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


# --------------------------------------------------
# 4. Abstract class cannot be instantiated
# --------------------------------------------------

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Uncomment to see the error:
# vehicle = Vehicle()

# Error: Cannot instantiate an abstract class
# with abstract methods.


# --------------------------------------------------
# 5. Practical example: Payment System
# --------------------------------------------------

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI.")


class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card.")


class Cash(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Cash.")


print("\nPayment System:")

payment1 = UPI()
payment2 = Card()
payment3 = Cash()

payment1.pay(500)
payment2.pay(1000)
payment3.pay(200)


# --------------------------------------------------
# 6. Abstraction with inheritance
# --------------------------------------------------

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_name(self):
        print("Employee Name:", self.name)


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        return 40000


class PartTimeEmployee(Employee):

    def calculate_salary(self):
        return 15000


print("\nEmployee Salary:")

employee1 = FullTimeEmployee("Alex")
employee2 = PartTimeEmployee("Sam")

employee1.display_name()
print("Salary:", employee1.calculate_salary())

employee2.display_name()
print("Salary:", employee2.calculate_salary())


# --------------------------------------------------
# 7. Checking abstract class inheritance
# --------------------------------------------------

print("\nInheritance Checking:")

print(issubclass(Dog, Animal))
print(issubclass(Rectangle, Shape))


# --------------------------------------------------
# END OF LESSON 20
# --------------------------------------------------
