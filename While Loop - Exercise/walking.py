target_steps_a_day = 10000
steps = 0

while target_steps_a_day >= steps:
    user_input = input()
    if user_input == "Going home":
        trip_steps = int(input())
        steps += trip_steps
        break
    else:
        trip_steps = int(user_input)
        steps += trip_steps
diff = abs(steps - target_steps_a_day)
if target_steps_a_day <= steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")