player_name = input()
points = 301
valid_shots = 0
invalid_shots = 0
while points != 0:
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {invalid_shots} unsuccessful shots.")
        break
    points_in_trow = int(input())
    if field == "Single":
        if points < points_in_trow:
            invalid_shots += 1
            continue
        points -= points_in_trow
        valid_shots += 1
    elif field == "Double":
        if points < points_in_trow * 2:
            invalid_shots += 1
            continue
        points -= points_in_trow * 2
        valid_shots += 1
    elif field == "Triple":
        if points < points_in_trow * 3:
            invalid_shots += 1
            continue
        points -= points_in_trow * 3
        valid_shots += 1

if points == 0:
    print(f"{player_name} won the leg with {valid_shots} shots.")