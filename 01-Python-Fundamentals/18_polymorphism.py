
"""
LESSON 18: POLYMORPHISM IN PYTHON

REVISION NOTES:

1. Polymorphism means one name with many forms.
2. The same method can behave differently for different objects.
3. Method overriding: Child class redefines a parent method.
4. Duck typing: Python focuses on available behavior, not exact type.
5. Operator overloading: Operators behave differently for different types.
6. Function polymorphism: One function works with different data types.

COMMON EXAMPLES:

- len() works with strings, lists and tuples.
- + adds numbers and joins strings.
- A method can have different implementations in different classes.
"""

# --------------------------------------------------
# 1. Built-in function polymorphism
# --------------------------------------------------

print("String length:", len("Python"))

numbers = [10, 20, 30, 40]
print("List length:", len(numbers))

items = (1, 2, 3)
print("Tuple length:", len(items))


# --------------------------------------------------
# 2. Operator polymorphism
# --------------------------------------------------

print("\nOperator Polymorphism:")

print(10 + 20)              # Addition
print("Hello " + "Python")  # String concatenation
print([1, 2] + [3, 4])      # List concatenation


# --------------------------------------------------
# 3. Method overriding
# --------------------------------------------------

class Animal:

    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def sound(self):
        print("Dog barks.")


class Cat(Animal):

    def sound(self):
        print("Cat meows.")


dog = Dog()
cat = Cat()

print("\nMethod Overriding:")

dog.sound()
cat.sound()


# --------------------------------------------------
# 4. Polymorphism with a common function
# --------------------------------------------------

class Dog:

    def sound(self):
        return "Bark"


class Cat:

    def sound(self):
        return "Meow"


class Cow:

    def sound(self):
        return "Moo"


def animal_sound(animal):
    print(animal.sound())


print("\nCommon Function:")

animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())


# --------------------------------------------------
# 5. Duck typing
# --------------------------------------------------

class Bird:

    def fly(self):
        print("Bird is flying.")


class Airplane:

    def fly(self):
        print("Airplane is flying.")


def start_flying(obj):
    obj.fly()


print("\nDuck Typing:")

start_flying(Bird())
start_flying(Airplane())


# --------------------------------------------------
# 6. Polymorphism with a loop
# --------------------------------------------------

class Circle:

    def area(self):
        return 3.14 * 5 * 5


class Rectangle:

    def area(self):
        return 10 * 5


class Square:

    def area(self):
        return 4 * 4


shapes = [Circle(), Rectangle(), Square()]

print("\nDifferent Shape Areas:")

for shape in shapes:
    print("Area:", shape.area())


# --------------------------------------------------
# 7. Operator overloading using __add__()
# --------------------------------------------------

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("\nOperator Overloading:")
print("Addition:", num1 + num2)


# --------------------------------------------------
# 8. Practical example: Payment System
# --------------------------------------------------

class UPI:

    def pay(self, amount):
        print("Paid", amount, "using UPI.")


class Card:

    def pay(self, amount):
        print("Paid", amount, "using Card.")


class Cash:

    def pay(self, amount):
        print("Paid", amount, "using Cash.")


def make_payment(payment_method, amount):
    payment_method.pay(amount)


print("\nPayment System:")

make_payment(UPI(), 500)
make_payment(Card(), 1000)
make_payment(Cash(), 200)


# --------------------------------------------------
# END OF LESSON 18
# --------------------------------------------------
