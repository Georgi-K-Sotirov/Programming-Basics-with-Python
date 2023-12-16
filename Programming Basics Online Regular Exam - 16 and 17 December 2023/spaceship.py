from math import floor

width_spaceship = float(input())
length_spaceship = float(input())
height_spaceship = float(input())
average_height_astronaut = float(input())

volume_spaceship = width_spaceship * length_spaceship * height_spaceship
volume_cabins = 2 * 2 * (average_height_astronaut + 0.40)

total_people = floor(volume_spaceship / volume_cabins)

if total_people < 3:
    print("The spacecraft is too small.")
elif total_people <= 10:
    print(f"The spacecraft holds {total_people} astronauts.")
else:
    print("The spacecraft is too big.")