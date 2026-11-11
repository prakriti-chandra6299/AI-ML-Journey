
"""
LESSON 15: FILE HANDLING IN PYTHON

REVISION NOTES:

1. File handling allows programs to store and retrieve data.
2. open() is used to open a file.
3. close() is used to close a file.
4. read() reads the entire file.
5. readline() reads one line.
6. readlines() reads all lines into a list.
7. write() writes data into a file.
8. append mode adds data without deleting existing content.
9. with open() automatically closes the file.

FILE MODES:

'r'  = Read
'w'  = Write (overwrites existing content)
'a'  = Append (adds content)
'x'  = Create a new file
'r+' = Read and write

SYNTAX:

with open("filename.txt", "mode") as file:
    # Perform file operations
"""

# --------------------------------------------------
# 1. Creating and writing to a file
# --------------------------------------------------

file = open("sample.txt", "w")

file.write("Hello Python!\n")
file.write("Learning file handling.")

file.close()

print("File created successfully.")


# --------------------------------------------------
# 2. Reading an entire file
# --------------------------------------------------

file = open("sample.txt", "r")

content = file.read()

print("\nFile content:")
print(content)

file.close()


# --------------------------------------------------
# 3. Reading one line
# --------------------------------------------------

file = open("sample.txt", "r")

first_line = file.readline()

print("\nFirst line:")
print(first_line)

file.close()


# --------------------------------------------------
# 4. Reading all lines into a list
# --------------------------------------------------

file = open("sample.txt", "r")

lines = file.readlines()

print("\nAll lines:")
print(lines)

file.close()


# --------------------------------------------------
# 5. Using append mode
# --------------------------------------------------

file = open("sample.txt", "a")

file.write("\nLearning Python is interesting.")

file.close()

print("\nNew content appended.")


# --------------------------------------------------
# 6. Reading the updated file
# --------------------------------------------------

file = open("sample.txt", "r")

print("\nUpdated file content:")
print(file.read())

file.close()


# --------------------------------------------------
# 7. Using with open()
# --------------------------------------------------

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nReading using with open():")
    print(content)

# File automatically closes after the with block.


# --------------------------------------------------
# 8. Creating a new file using x mode
# --------------------------------------------------

try:
    with open("new_file.txt", "x") as file:
        file.write("This is a newly created file.")

    print("\nNew file created.")

except FileExistsError:
    print("\nFile already exists.")


# --------------------------------------------------
# 9. Handling FileNotFoundError
# --------------------------------------------------

try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("\nThe requested file was not found.")


# --------------------------------------------------
# 10. Writing multiple lines
# --------------------------------------------------

subjects = ["Python\n", "Machine Learning\n", "Data Science\n"]

with open("subjects.txt", "w") as file:
    file.writelines(subjects)

print("\nMultiple lines written successfully.")


# --------------------------------------------------
# 11. Counting lines in a file
# --------------------------------------------------

with open("subjects.txt", "r") as file:
    lines = file.readlines()

    print("\nTotal number of lines:", len(lines))


# --------------------------------------------------
# END OF LESSON 15
# --------------------------------------------------
