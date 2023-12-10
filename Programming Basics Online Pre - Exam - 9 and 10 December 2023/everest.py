starting_meters = 5364
goal = 8848
diff = goal - starting_meters
days_counter = 1
sleeping = input()
while sleeping != "END":
    if sleeping == "Yes":
        days_counter += 1
    meters_per_day = int(input())
    if days_counter > 5:
        break
    diff -= meters_per_day
    if diff <= 0:
        break
    sleeping = input()

if diff <= 0:
    print(f"Goal reached for {days_counter} days!")
else:
    print("Failed!")
    print(f"{goal - diff}")
