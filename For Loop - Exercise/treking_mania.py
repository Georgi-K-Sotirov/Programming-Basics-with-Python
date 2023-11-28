number_of_grups = int(input())
g1_counter = 0
g2_counter = 0
g3_counter = 0
g4_counter = 0
g5_counter = 0
people_counter = 0

for _ in range(number_of_grups):
    number_of_people = int(input())
    people_counter += number_of_people
    if number_of_people <= 5:
        g1_counter += number_of_people
    elif number_of_people <= 12:
        g2_counter += number_of_people
    elif number_of_people <= 25:
        g3_counter += number_of_people
    elif number_of_people <= 40:
        g4_counter += number_of_people
    elif number_of_people >= 41:
        g5_counter += number_of_people

g1_percent = g1_counter / people_counter * 100
g2_percent = g2_counter / people_counter * 100
g3_percent = g3_counter / people_counter * 100
g4_percent = g4_counter / people_counter * 100
g5_percent = g5_counter / people_counter * 100

print(f"{g1_percent:.2f}%")
print(f"{g2_percent:.2f}%")
print(f"{g3_percent:.2f}%")
print(f"{g4_percent:.2f}%")
print(f"{g5_percent:.2f}%")
