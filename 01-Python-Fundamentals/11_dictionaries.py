
"""
LESSON 11: DICTIONARIES IN PYTHON

REVISION NOTES:

1. A dictionary stores data in KEY-VALUE pairs.

2. PROPERTIES:
   - Mutable (can be changed).
   - Keys must be unique.
   - Values can be duplicated.
   - Maintains insertion order.
   - Keys must be hashable (e.g. strings, numbers, tuples
     containing hashable elements).

3. CREATION:
   student = {"name": "Alex", "age": 21}

4. ACCESSING VALUES:
   dictionary["key"]
   dictionary.get("key")

5. IMPORTANT DICTIONARY METHODS:
   keys()       -> Returns all keys.
   values()     -> Returns all values.
   items()      -> Returns key-value pairs.
   get()        -> Safely retrieves a value.
   update()     -> Adds or updates entries.
   pop()        -> Removes a specified key.
   popitem()    -> Removes the last inserted pair.
   clear()      -> Removes all entries.
   setdefault() -> Returns a value, inserting a default
                   if the key does not exist.
   copy()       -> Creates a shallow copy.

6. LOOPING:
   for key in dictionary:
       print(key, dictionary[key])

7. NESTED DICTIONARY:
   A dictionary inside another dictionary.

8. DICTIONARY COMPREHENSION:
   Creates a dictionary using a concise expression.
"""


# --------------------------------------------------
# 1. CREATING A DICTIONARY
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "course": "Computer Science"
}

print(student)


# --------------------------------------------------
# 2. ACCESSING VALUES
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

print(student["name"])
print(student["age"])


# --------------------------------------------------
# 3. USING GET METHOD
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

print(student.get("name"))
print(student.get("marks"))
print(student.get("marks", 0))


# --------------------------------------------------
# 4. ADDING NEW KEY-VALUE PAIRS
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

student["city"] = "Delhi"

print(student)


# --------------------------------------------------
# 5. UPDATING VALUES
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

student["age"] = 22

print(student)


# --------------------------------------------------
# 6. UPDATE METHOD
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

student.update({
    "age": 22,
    "course": "Computer Science"
})

print(student)


# --------------------------------------------------
# 7. REMOVING ELEMENTS USING POP
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

removed = student.pop("age")

print("Removed value:", removed)
print(student)


# --------------------------------------------------
# 8. POPITEM METHOD
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

removed = student.popitem()

print("Removed pair:", removed)
print(student)


# --------------------------------------------------
# 9. CLEAR METHOD
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

student.clear()

print(student)


# --------------------------------------------------
# 10. GETTING ALL KEYS
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

print(student.keys())


# --------------------------------------------------
# 11. GETTING ALL VALUES
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

print(student.values())


# --------------------------------------------------
# 12. GETTING KEY-VALUE PAIRS
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

print(student.items())


# --------------------------------------------------
# 13. LOOPING THROUGH A DICTIONARY
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

for key in student:
    print(key, ":", student[key])


# --------------------------------------------------
# 14. LOOPING THROUGH ITEMS
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# --------------------------------------------------
# 15. CHECKING WHETHER A KEY EXISTS
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

print("name" in student)
print("marks" in student)


# --------------------------------------------------
# 16. DICTIONARY LENGTH
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "marks": 85
}

print("Number of entries:", len(student))


# --------------------------------------------------
# 17. SETDEFAULT METHOD
# --------------------------------------------------

student = {
    "name": "Alex",
    "age": 21
}

student.setdefault("city", "Delhi")
student.setdefault("age", 25)

print(student)


# --------------------------------------------------
# 18. COPYING A DICTIONARY
# --------------------------------------------------

original = {
    "name": "Alex",
    "age": 21
}

copied = original.copy()

copied["age"] = 22

print("Original:", original)
print("Copied:", copied)


# --------------------------------------------------
# 19. NESTED DICTIONARY
# --------------------------------------------------

students = {
    "student1": {
        "name": "Alex",
        "marks": 85
    },
    "student2": {
        "name": "Sam",
        "marks": 90
    }
}

print(students["student1"]["name"])
print(students["student2"]["marks"])


# --------------------------------------------------
# 20. DICTIONARY COMPREHENSION
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# --------------------------------------------------
# 21. DICTIONARY COMPREHENSION WITH CONDITION
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)


# --------------------------------------------------
# 22. PRACTICAL EXAMPLE: STUDENT RECORD
# --------------------------------------------------

student = {
    "name": "Alex",
    "marks": 88,
    "grade": "A"
}

print("Student:", student["name"])
print("Marks:", student["marks"])
print("Grade:", student["grade"])


# --------------------------------------------------
# END OF LESSON 11
# --------------------------------------------------
