'''Scenario 1:
Scenario: Student Grade Management System
You are tasked with creating a basic Student Grade Management System for a small class. The system should allow you to:

Add new students to the system. (done)
Record grades for each student in different subjects. (Done)
Calculate the average grade for each student.(Done)
Display the list of all students with their grades and averages. (Done)
Find and display the student with the highest average grade. '''
# Initialize an empty dictionary to store student data
sample_students = {}

# Collect student data
for i in range(2):
    name = input("Enter your name = ").strip()
    subject_grades = {}
    for y in range(2):
        subject = input("Enter a Subject name = ").strip().upper()
        marks = int(input("Enter the marks = "))
        subject_grades[subject] = marks
    sample_students[name] = subject_grades

print("Sample Students Data:", sample_students)

average_dict = {}

for key ,value in sample_students.items():
    total = sum(value.values())
    avg = total / len (value)
    average_dict[key] = avg

max_score = 0 
max_name = ''

for name ,score in average_dict.items():
    if score > max_score : 
        max_score = score
        max_name = name

print(f"Highest Average is of {max_name} with average of {max_score}")