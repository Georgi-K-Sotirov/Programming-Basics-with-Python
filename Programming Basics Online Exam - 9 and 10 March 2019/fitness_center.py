qty_people = int(input())
back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
workout_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0
protein_counter = 0

for _ in range(qty_people):
    type_of_workout = input()
    if type_of_workout == "Back":
        back_counter += 1
        workout_counter += 1
    elif type_of_workout == "Chest":
        chest_counter += 1
        workout_counter += 1
    elif type_of_workout == "Legs":
        legs_counter += 1
        workout_counter += 1
    elif type_of_workout == "Abs":
        abs_counter += 1
        workout_counter += 1
    elif type_of_workout == "Protein shake":
        protein_shake_counter += 1
        protein_counter +=1
    elif type_of_workout == "Protein bar":
        protein_bar_counter += 1
        protein_counter +=1
percent_workout = workout_counter / qty_people * 100
percent_protein = protein_counter / qty_people * 100

print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{percent_workout:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")

