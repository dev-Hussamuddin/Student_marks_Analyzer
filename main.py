import csv
import os

name = input("Enter student's fullname: ")
subjects = ["Python", "Database", "Math", "English", "Computer"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

# CGPA Calculation
cgpa = average / 9.5

# Grade
if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B+'
elif average >= 60:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'D'

result = "PASS" if average >= 40 else "FAIL"

# Display Result
print(f"\nStudent Name:   {name}")
print(f"Total Marks:    {total}")
print(f"Average Marks:  {average:.2f}")
print(f"CGPA:           {cgpa:.2f}")
print(f"Grade:          {grade}")
print(f"Result:         {result}")

# Save to CSV
file_name = "student_results.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, 'a', newline='') as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Name",
            "Total Marks",
            "Average Marks",
            "CGPA",
            "Grade",
            "Result"
        ])

    writer.writerow([
        name,
        total,
        round(average, 2),
        round(cgpa, 2),
        grade,
        result
    ])

print("\nResults saved to student_results.csv")