
"""
LESSON 10: SETS IN PYTHON

REVISION NOTES:

1. A set stores unique elements.

2. SET PROPERTIES:
   - Unordered collection.
   - Does not allow duplicates.
   - Mutable.
   - Does not support indexing or slicing.
   - Can contain different immutable data types.

3. SET CREATION:
   numbers = {10, 20, 30}

4. EMPTY SET:
   empty_set = set()
   {} creates an empty dictionary, not a set.

5. IMPORTANT SET METHODS:
   add()          -> Adds one element.
   update()       -> Adds multiple elements.
   remove()       -> Removes an element; raises KeyError if absent.
   discard()      -> Removes an element if present.
   pop()          -> Removes and returns an arbitrary element.
   clear()        -> Removes all elements.

6. SET OPERATIONS:
   union()        -> Combines elements from both sets.
   intersection() -> Returns common elements.
   difference()   -> Returns elements in the first set only.
   symmetric_difference() -> Returns elements in either set,
                             but not in both.

7. OTHER OPERATIONS:
   issubset()     -> Checks whether a set is a subset.
   issuperset()   -> Checks whether a set is a superset.
   isdisjoint()   -> Checks whether sets have no common elements.

8. IMPORTANT:
   Sets are useful for removing duplicates and
   performing mathematical set operations.
"""


# --------------------------------------------------
# 1. CREATING SETS
# --------------------------------------------------

numbers = {10, 20, 30, 40}

fruits = {"Apple", "Mango", "Banana"}

mixed = {10, "Python", 3.14, True}

print(numbers)
print(fruits)
print(mixed)


# --------------------------------------------------
# 2. DUPLICATE ELEMENTS
# --------------------------------------------------

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)


# --------------------------------------------------
# 3. CREATING AN EMPTY SET
# --------------------------------------------------

empty_set = set()

print(empty_set)
print(type(empty_set))


# --------------------------------------------------
# 4. ADD METHOD
# --------------------------------------------------

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# --------------------------------------------------
# 5. UPDATE METHOD
# --------------------------------------------------

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)


# --------------------------------------------------
# 6. REMOVE METHOD
# --------------------------------------------------

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)


# --------------------------------------------------
# 7. DISCARD METHOD
# --------------------------------------------------

numbers = {10, 20, 30}

numbers.discard(50)  # No error if 50 is absent.

print(numbers)


# --------------------------------------------------
# 8. POP METHOD
# --------------------------------------------------

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed element:", removed)
print("Updated set:", numbers)


# --------------------------------------------------
# 9. CLEAR METHOD
# --------------------------------------------------

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# --------------------------------------------------
# 10. UNION
# --------------------------------------------------

set1 = {10, 20, 30}
set2 = {30, 40, 50}

print(set1.union(set2))

# Alternative:
print(set1 | set2)


# --------------------------------------------------
# 11. INTERSECTION
# --------------------------------------------------

set1 = {10, 20, 30}
set2 = {20, 30, 40}

print(set1.intersection(set2))

# Alternative:
print(set1 & set2)


# --------------------------------------------------
# 12. DIFFERENCE
# --------------------------------------------------

set1 = {10, 20, 30}
set2 = {20, 30, 40}

print(set1.difference(set2))

# Alternative:
print(set1 - set2)


# --------------------------------------------------
# 13. SYMMETRIC DIFFERENCE
# --------------------------------------------------

set1 = {10, 20, 30}
set2 = {20, 30, 40}

print(set1.symmetric_difference(set2))

# Alternative:
print(set1 ^ set2)


# --------------------------------------------------
# 14. SUBSET AND SUPERSET
# --------------------------------------------------

set1 = {10, 20}
set2 = {10, 20, 30, 40}

print(set1.issubset(set2))
print(set2.issuperset(set1))


# --------------------------------------------------
# 15. DISJOINT SETS
# --------------------------------------------------

set1 = {10, 20, 30}
set2 = {40, 50, 60}

print(set1.isdisjoint(set2))


# --------------------------------------------------
# 16. LOOPING THROUGH A SET
# --------------------------------------------------

fruits = {"Apple", "Mango", "Banana"}

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 17. CHECKING MEMBERSHIP
# --------------------------------------------------

fruits = {"Apple", "Mango", "Banana"}

print("Mango" in fruits)
print("Orange" not in fruits)


# --------------------------------------------------
# 18. REMOVING DUPLICATES FROM A LIST
# --------------------------------------------------

numbers = [10, 20, 20, 30, 30, 40, 40]

unique_numbers = set(numbers)

print(unique_numbers)


# --------------------------------------------------
# 19. CONVERTING SET INTO LIST
# --------------------------------------------------

numbers = {10, 20, 30, 40}

my_list = list(numbers)

print(my_list)


# --------------------------------------------------
# 20. SET LENGTH
# --------------------------------------------------

numbers = {10, 20, 30, 40, 50}

print("Number of elements:", len(numbers))


# --------------------------------------------------
# END OF LESSON 10
# --------------------------------------------------
