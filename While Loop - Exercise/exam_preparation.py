failure_tasks = int(input())
last_task_name = ""
failed_tasks = 0
grade_counter = 0
tasks_counter = 0
total_grades = 0

while True:
    if failure_tasks == failed_tasks:
        break
    task_name = input()
    if task_name == "Enough":
        break
    grade = int(input())
    grade_counter += 1
    tasks_counter += 1
    total_grades += grade
    if grade <= 4:
        failed_tasks += 1
    last_task_name = task_name
if failure_tasks == failed_tasks:
    print(f"You need a break, {failed_tasks} poor grades.")
elif failed_tasks < failure_tasks:
    print(f"Average score: {total_grades/grade_counter:.2f}")
    print(f"Number of problems: {tasks_counter}")
    print(f"Last problem: {last_task_name}")