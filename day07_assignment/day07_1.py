'''
Structured CSV & JSON Data Processor
Scenario
An academic registrar stores student course registrations in a CSV file. You need to read this file, 
compute overall statistics, and export a summarized JSON report.

Problem Description
Create a function process_student_records(input_csv_path, output_json_path):
Reads an input_csv_path containing columns: student_id, name, course, score.
Uses csv.DictReader inside a context manager to parse all rows.
Computes:
total_students: Total number of students processed.
average_score: Arithmetic mean of all student scores (rounded to 2 decimal places).
top_scorer: The dictionary {"name": <name>, "score": <score>} of the highest scoring student.
course_counts: A dictionary mapping each course name to the count of enrolled students.
Writes the summary dictionary into output_json_path formatted with an indentation of 4 spaces using json.dump().
Example Walkthrough
# Given input CSV:
# student_id,name,course,score
# 101,Arham,AI,88.5
# 102,Lisa,BDA,94.0
# 103,Vinod,AI,96.5

process_student_records("students.csv", "summary.json")

# Expected summary.json output:
# {
#     "total_students": 3,
#     "average_score": 93.0,
#     "top_scorer": {
#         "name": "Vinod",
#         "score": 96.5
#     },
#     "course_counts": {
#         "AI": 2,
#         "BDA": 1
#     }
# }
'''
import csv
import json


def process_student_records(input_csv_path, output_json_path):

    students = []

    # Read CSV file
    with open(input_csv_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["score"] = float(row["score"])
            students.append(row)

    # Total students
    total_students = len(students)

    # Calculate average score
    total_score = 0

    for student in students:
        total_score += student["score"]

    average_score = round(total_score / total_students, 2)

    # Find top scorer
    top_student = students[0]

    for student in students:
        if student["score"] > top_student["score"]:
            top_student = student

    top_scorer = {
        "name": top_student["name"],
        "score": top_student["score"]
    }

    # Count students in each course
    course_counts = {}

    for student in students:
        course = student["course"]

        if course in course_counts:
            course_counts[course] += 1
        else:
            course_counts[course] = 1

    # Create summary
    summary = {
        "total_students": total_students,
        "average_score": average_score,
        "top_scorer": top_scorer,
        "course_counts": course_counts
    }

    # Write JSON file
    with open(output_json_path, mode="w") as file:
        json.dump(summary, file, indent=4)

    return summary

summary = process_student_records(
    "students.csv",
    "summary.json"
)

print(summary)