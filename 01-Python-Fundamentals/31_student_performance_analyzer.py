
"""
LESSON 31: STUDENT PERFORMANCE ANALYZER

REVISION NOTES:
1. Lists store multiple values.
2. Dictionaries store data in key-value pairs.
3. Functions organize reusable code.
4. Loops process multiple records.
5. Conditional statements make decisions.
6. Exception handling prevents program crashes.
7. Built-in functions: sum(), len(), max(), min(), sorted().
8. File handling saves results permanently.

PROJECT:
Analyze fictional student marks, calculate averages,
assign grades, and identify the top-performing student.
"""

import json
import csv


# --------------------------------------------------
# 1. STUDENT DATA
# --------------------------------------------------

students = [
    {"name": "Alex", "marks": [85, 90, 78]},
    {"name": "Jordan", "marks": [72, 80, 75]},
    {"name": "Taylor", "marks": [95, 92, 98]},
    {"name": "Morgan", "marks": [60, 68, 70]},
    {"name": "Casey", "marks": [88, 84, 91]}
]


# --------------------------------------------------
# 2. CALCULATE AVERAGE
# --------------------------------------------------

def calculate_average(marks):
    return sum(marks) / len(marks)


# --------------------------------------------------
# 3. ASSIGN GRADE
# --------------------------------------------------

def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


# --------------------------------------------------
# 4. ANALYZE STUDENTS
# --------------------------------------------------

def analyze_students(student_list):

    results = []

    for student in student_list:

        average = calculate_average(student["marks"])
        grade = calculate_grade(average)

        result = {
            "name": student["name"],
            "marks": student["marks"],
            "average": round(average, 2),
            "grade": grade
        }

        results.append(result)

    return results


# --------------------------------------------------
# 5. DISPLAY RESULTS
# --------------------------------------------------

def display_results(results):

    print("\nSTUDENT PERFORMANCE REPORT")
    print("-" * 55)

    for student in results:

        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {student['average']}")
        print(f"Grade: {student['grade']}")
        print("-" * 55)


# --------------------------------------------------
# 6. FIND TOP PERFORMER
# --------------------------------------------------

def find_top_student(results):

    top_student = max(
        results,
        key=lambda student: student["average"]
    )

    print("\nTOP PERFORMER")
    print(f"Name: {top_student['name']}")
    print(f"Average: {top_student['average']}")
    print(f"Grade: {top_student['grade']}")


# --------------------------------------------------
# 7. DISPLAY CLASS STATISTICS
# --------------------------------------------------

def display_statistics(results):

    averages = [
        student["average"] for student in results
    ]

    print("\nCLASS STATISTICS")
    print("-" * 30)

    print(f"Number of students: {len(results)}")
    print(f"Class average: {round(sum(averages) / len(averages), 2)}")
    print(f"Highest average: {max(averages)}")
    print(f"Lowest average: {min(averages)}")


# --------------------------------------------------
# 8. SAVE RESULTS TO JSON
# --------------------------------------------------

def save_to_json(results):

    try:
        with open("student_report.json", "w") as file:
            json.dump(results, file, indent=4)

        print("\nJSON report saved successfully.")

    except OSError as error:
        print(f"Error saving JSON: {error}")


# --------------------------------------------------
# 9. SAVE RESULTS TO CSV
# --------------------------------------------------

def save_to_csv(results):

    try:
        with open("student_report.csv", "w", newline="") as file:

            fieldnames = [
                "name", "marks", "average", "grade"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(results)

        print("CSV report saved successfully.")

    except OSError as error:
        print(f"Error saving CSV: {error}")


# --------------------------------------------------
# 10. MAIN PROGRAM
# --------------------------------------------------

def main():

    try:
        results = analyze_students(students)

        display_results(results)
        find_top_student(results)
        display_statistics(results)

        save_to_json(results)
        save_to_csv(results)

    except (ValueError, ZeroDivisionError) as error:
        print(f"Analysis error: {error}")


if __name__ == "__main__":
    main()


# --------------------------------------------------
# TIME COMPLEXITY
# --------------------------------------------------

"""
Let:
n = Number of students
m = Number of subjects per student

Analysis: O(n * m)
Sorting: Not used in this version.
Finding top student: O(n)
Displaying results: O(n)
Saving reports: O(n * m)
"""
