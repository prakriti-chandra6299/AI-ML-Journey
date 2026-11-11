
"""
LESSON 28: WORKING WITH JSON AND CSV FILES

REVISION NOTES
--------------
1. CSV (Comma-Separated Values):
   - Stores tabular data in rows and columns.
   - Commonly used for datasets and spreadsheets.
   - Python module: csv

2. JSON (JavaScript Object Notation):
   - Stores data using key-value pairs.
   - Supports objects, arrays, strings, numbers and booleans.
   - Python module: json

3. CSV FUNCTIONS:
   - csv.reader()       - Reads CSV rows.
   - csv.writer()       - Writes CSV rows.
   - csv.DictReader()   - Reads rows as dictionaries.
   - csv.DictWriter()   - Writes dictionaries to CSV.

4. JSON FUNCTIONS:
   - json.load()        - Reads JSON from a file.
   - json.dump()        - Writes JSON to a file.
   - json.loads()       - Converts JSON string to Python object.
   - json.dumps()       - Converts Python object to JSON string.

5. Always close files after working with them.
   The with statement handles this automatically.
"""

import csv
import json


# ==================================================
# 1. CREATING AND WRITING A CSV FILE
# ==================================================

students = [
    ["Name", "Age", "Marks"],
    ["Alex", 20, 85],
    ["Sam", 21, 92],
    ["Jordan", 19, 78]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully!")


# ==================================================
# 2. READING A CSV FILE
# ==================================================

print("\nReading CSV file:")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ==================================================
# 3. WRITING CSV USING DICTWRITER
# ==================================================

student_data = [
    {"Name": "Taylor", "Age": 22, "Marks": 88},
    {"Name": "Morgan", "Age": 20, "Marks": 95},
    {"Name": "Casey", "Age": 21, "Marks": 81}
]

fieldnames = ["Name", "Age", "Marks"]

with open("student_details.csv", "w", newline="") as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(student_data)

print("\nDictionary CSV file created!")


# ==================================================
# 4. READING CSV USING DICTREADER
# ==================================================

print("\nReading dictionary CSV:")

with open("student_details.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(dict(row))


# ==================================================
# 5. CREATING A PYTHON DICTIONARY
# ==================================================

student = {
    "name": "Alex",
    "age": 20,
    "marks": 85,
    "subjects": ["Python", "Math", "Statistics"],
    "passed": True
}

print("\nPython dictionary:")
print(student)


# ==================================================
# 6. CONVERTING PYTHON DATA INTO JSON
# ==================================================

# dumps() converts Python data into a JSON string.

json_string = json.dumps(student, indent=4)

print("\nJSON string:")
print(json_string)


# ==================================================
# 7. CONVERTING JSON STRING INTO PYTHON DATA
# ==================================================

python_data = json.loads(json_string)

print("\nConverted back to Python:")
print(python_data)

print("Student name:", python_data["name"])
print("Student subjects:", python_data["subjects"])


# ==================================================
# 8. WRITING JSON INTO A FILE
# ==================================================

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)

print("\nJSON file created successfully!")


# ==================================================
# 9. READING JSON FROM A FILE
# ==================================================

with open("student.json", "r") as file:

    loaded_student = json.load(file)

print("\nReading JSON file:")
print(loaded_student)

print("Name:", loaded_student["name"])
print("Marks:", loaded_student["marks"])


# ==================================================
# 10. WORKING WITH MULTIPLE STUDENTS IN JSON
# ==================================================

students = [
    {
        "name": "Alex",
        "marks": 85
    },
    {
        "name": "Sam",
        "marks": 92
    },
    {
        "name": "Jordan",
        "marks": 78
    }
]

with open("students.json", "w") as file:

    json.dump(students, file, indent=4)

with open("students.json", "r") as file:

    loaded_students = json.load(file)

print("\nStudent records:")

for student in loaded_students:
    print(student["name"], student["marks"])


# ==================================================
# 11. PRACTICAL CSV DATA PROCESSING
# ==================================================

print("\nProcessing student marks:")

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["Name"]
        marks = int(row["Marks"])

        if marks >= 40:
            status = "Pass"
        else:
            status = "Fail"

        print(name, "-", marks, "-", status)


# ==================================================
# 12. CSV VS JSON
# ==================================================

"""
CSV:
    Tabular data.
    Rows and columns.
    Suitable for spreadsheet-like datasets.

JSON:
    Key-value data.
    Supports nested structures.
    Suitable for structured data and APIs.

IMPORTANT:
    csv and json are built-in Python modules.
    No pip installation is required.
"""
