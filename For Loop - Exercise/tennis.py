from math import  floor
number_of_tournaments = int(input())
points = int(input())

w_counter = 0
f_counter = 0
sf_counter = 0

for _ in range(number_of_tournaments):
    status_of_tournaments = input()
    if status_of_tournaments == "W":
        w_counter += 1
    elif status_of_tournaments == "F":
        f_counter += 1
    elif status_of_tournaments == "SF":
        sf_counter += 1

total_points = points + (w_counter * 2000) + (f_counter * 1200) + (sf_counter * 720)
average_points = floor((total_points - points)  / number_of_tournaments)
w_percent = w_counter / number_of_tournaments * 100

print(f"Final points: {total_points:.0f}")
print(f"Average points: {average_points:.0f}")
print(f"{w_percent:.2f}%")