
"""
LESSON 7: STRINGS IN PYTHON

REVISION NOTES:

1. A string is a sequence of characters.
   Strings can be written using single, double or triple quotes.

2. INDEXING:
   - Positive indexing starts from 0.
   - Negative indexing starts from -1 (last character).

3. SLICING:
   Syntax: string[start:stop:step]
   The stop index is excluded.

4. IMPORTANT STRING METHODS:
   upper()       -> Converts to uppercase.
   lower()       -> Converts to lowercase.
   title()       -> Capitalizes each word.
   capitalize()  -> Capitalizes the first character.
   strip()       -> Removes surrounding whitespace.
   replace()     -> Replaces part of a string.
   split()       -> Splits a string into a list.
   find()        -> Returns the position of a substring.
   count()       -> Counts occurrences.
   startswith()  -> Checks the beginning.
   endswith()    -> Checks the ending.

5. STRINGS ARE IMMUTABLE:
   Their original characters cannot be changed directly.

6. STRING FORMATTING:
   f-strings allow variables and expressions inside strings.

7. ESCAPE CHARACTERS:
   \\n -> New line
   \\t -> Tab
   \\\\ -> Backslash
   \\" -> Double quote
"""


# --------------------------------------------------
# 1. CREATING STRINGS
# --------------------------------------------------

single_quote = 'Hello Python'
double_quote = "Welcome to Python"
multi_line = """Python is easy to learn.
Python is powerful."""

print(single_quote)
print(double_quote)
print(multi_line)


# --------------------------------------------------
# 2. STRING LENGTH
# --------------------------------------------------

text = "Python Programming"

print("Length:", len(text))


# --------------------------------------------------
# 3. POSITIVE INDEXING
# --------------------------------------------------

language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[5])


# --------------------------------------------------
# 4. NEGATIVE INDEXING
# --------------------------------------------------

language = "Python"

print(language[-1])
print(language[-2])
print(language[-3])


# --------------------------------------------------
# 5. STRING SLICING
# --------------------------------------------------

text = "Python Programming"

print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
print(text[:])
print(text[::2])


# --------------------------------------------------
# 6. REVERSING A STRING
# --------------------------------------------------

word = "Python"

print(word[::-1])


# --------------------------------------------------
# 7. CHANGING CASE
# --------------------------------------------------

text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())


# --------------------------------------------------
# 8. REMOVING WHITESPACE
# --------------------------------------------------

text = "   Hello Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# --------------------------------------------------
# 9. REPLACING CHARACTERS OR WORDS
# --------------------------------------------------

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)


# --------------------------------------------------
# 10. FINDING AND COUNTING
# --------------------------------------------------

text = "Python is easy. Python is powerful."

print("Position:", text.find("easy"))
print("Count:", text.count("Python"))


# --------------------------------------------------
# 11. CHECKING START AND END
# --------------------------------------------------

text = "Python Programming"

print(text.startswith("Python"))
print(text.endswith("Programming"))


# --------------------------------------------------
# 12. SPLITTING A STRING
# --------------------------------------------------

text = "Python,Java,C++,JavaScript"

languages = text.split(",")

print(languages)


# --------------------------------------------------
# 13. JOINING STRINGS
# --------------------------------------------------

languages = ["Python", "Java", "C++"]

result = " | ".join(languages)

print(result)


# --------------------------------------------------
# 14. MEMBERSHIP OPERATORS
# --------------------------------------------------

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)


# --------------------------------------------------
# 15. STRING FORMATTING USING F-STRINGS
# --------------------------------------------------

name = "Alex"
age = 21

print(f"My name is {name} and I am {age} years old.")


# --------------------------------------------------
# 16. F-STRINGS WITH EXPRESSIONS
# --------------------------------------------------

a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Product = {a * b}")


# --------------------------------------------------
# 17. ESCAPE CHARACTERS
# --------------------------------------------------

print("Hello\nPython")
print("Hello\tPython")
print("This is a backslash: \\")
print("She said, \"Hello!\"")


# --------------------------------------------------
# 18. STRINGS ARE IMMUTABLE
# --------------------------------------------------

text = "Python"

# This creates a new string.
new_text = "J" + text[1:]

print("Original:", text)
print("Modified copy:", new_text)


# --------------------------------------------------
# 19. USER INPUT WITH STRINGS
# --------------------------------------------------

user_name = input("Enter a name: ")

print("Hello,", user_name)
print("Uppercase:", user_name.upper())
print("Name length:", len(user_name))


# --------------------------------------------------
# END OF LESSON 7
# --------------------------------------------------
