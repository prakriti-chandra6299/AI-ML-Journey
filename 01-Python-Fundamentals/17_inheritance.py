
"""
LESSON 17: INHERITANCE IN PYTHON

REVISION NOTES:

1. Inheritance allows one class to reuse another class's properties
   and methods.
2. Parent class: The class whose properties are inherited.
3. Child class: The class that inherits from another class.
4. super(): Used to access parent class methods and constructors.
5. Method overriding: Redefining a parent method in a child class.

TYPES OF INHERITANCE:

1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

SYNTAX:

class Parent:
    pass

class Child(Parent):
    pass
"""

# --------------------------------------------------
# 1. Single Inheritance
# --------------------------------------------------

class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()   # Inherited from Animal
dog.bark()  # Own method


# --------------------------------------------------
# 2. Multilevel Inheritance
# --------------------------------------------------

class Grandparent:

    def house(self):
        print("Grandparent owns a house.")


class Parent(Grandparent):

    def car(self):
        print("Parent owns a car.")


class Child(Parent):

    def bike(self):
        print("Child owns a bike.")


child = Child()

print("\nMultilevel Inheritance:")

child.house()
child.car()
child.bike()


# --------------------------------------------------
# 3. Multiple Inheritance
# --------------------------------------------------

class Father:

    def father_quality(self):
        print("Father is hardworking.")


class Mother:

    def mother_quality(self):
        print("Mother is caring.")


class Child(Father, Mother):

    def child_quality(self):
        print("Child is intelligent.")


child = Child()

print("\nMultiple Inheritance:")

child.father_quality()
child.mother_quality()
child.child_quality()


# --------------------------------------------------
# 4. Hierarchical Inheritance
# --------------------------------------------------

class Vehicle:

    def start(self):
        print("Vehicle starts.")


class Car(Vehicle):

    def drive(self):
        print("Car is driving.")


class Bike(Vehicle):

    def ride(self):
        print("Bike is riding.")


car = Car()
bike = Bike()

print("\nHierarchical Inheritance:")

car.start()
car.drive()

bike.start()
bike.ride()


# --------------------------------------------------
# 5. Using super()
# --------------------------------------------------

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_details(self):
        super().display()
        print("Marks:", self.marks)


student = Student("Alex", 90)

print("\nUsing super():")

student.show_details()


# --------------------------------------------------
# 6. Method Overriding
# --------------------------------------------------

class Parent:

    def show(self):
        print("This is the parent class.")


class Child(Parent):

    def show(self):
        print("This is the child class.")


obj = Child()

print("\nMethod Overriding:")

obj.show()


# --------------------------------------------------
# 7. Calling the Parent Method
# --------------------------------------------------

class Animal:

    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks.")


dog = Dog()

print("\nParent Method with super():")

dog.sound()


# --------------------------------------------------
# 8. Practical Example: Employee Management
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_manager(self):
        super().display()
        print("Department:", self.department)


manager = Manager("Sam", 50000, "IT")

print("\nEmployee Management:")

manager.display_manager()


# --------------------------------------------------
# 9. Checking Inheritance
# --------------------------------------------------

print("\nInheritance Checking:")

print(issubclass(Dog, Animal))
print(isinstance(dog, Animal))


# --------------------------------------------------
# END OF LESSON 17
# --------------------------------------------------
