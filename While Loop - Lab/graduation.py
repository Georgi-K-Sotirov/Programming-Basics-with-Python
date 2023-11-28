student_name = input()
grade_counter = 0
year_counter = 1
fail_counter = 0
while True:
    if fail_counter >= 2:
        break
    if year_counter > 12:
        break
    grade = float(input())
    if grade >= 4.00:
        grade_counter += grade
        year_counter += 1
    else:
        fail_counter += 1
        continue
if fail_counter < 2:
    print(f"{student_name} graduated. Average grade: {grade_counter/12:.2f}")
else:
    print(f"{student_name} has been excluded at {year_counter} grade")

