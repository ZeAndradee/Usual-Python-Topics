# Write a program that asks the user for the number of students in the class,
# their grades, and prints the overall average, the highest, and the lowest grade.

highest_grade = 0
lowest_grade = 999
overall_average = 0

num_students = int(input("Enter the number of students in the class: "))
for i in range(1, num_students + 1):
    grade = int(input(f"Enter the grade for student {i}: "))
    if grade > highest_grade:
        highest_grade = grade
    elif grade < lowest_grade:
        lowest_grade = grade
    overall_average += grade

overall_average /= num_students

print(f'''Overall Average: {overall_average:.1f}
Highest Grade: {highest_grade}
Lowest Grade: {lowest_grade}''')
