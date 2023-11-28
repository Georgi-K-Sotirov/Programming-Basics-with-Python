name_of_actor = input()
point_from_academy = float(input())
number_of_grader = int(input())

for _ in range(number_of_grader):
    name_of_grader = input()
    point_from_grader = float(input())
    point_from_academy += len(name_of_grader) * point_from_grader / 2
    if point_from_academy > 1250.5:
        break
diff = 1250.5 - point_from_academy
if point_from_academy > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {point_from_academy:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")