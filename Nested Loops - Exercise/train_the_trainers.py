people_in_the_jury = int(input())
total_grades = 0
presentation_counter = 0
presentation_name = input()
while presentation_name != "Finish":
    total_presentation_grade = 0
    for grade in range(people_in_the_jury):
        current_grade = float(input())
        total_presentation_grade += current_grade
    average_presentation_grade = total_presentation_grade / people_in_the_jury
    total_grades += average_presentation_grade
    presentation_counter += 1
    print(f"{presentation_name} - {average_presentation_grade:.2f}.")
    presentation_name = input()
average_total_grade = total_grades / presentation_counter
print(f"Student's final assessment is {average_total_grade:.2f}.")