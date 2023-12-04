minutes_walk = int(input())
times_per_day_walk = int(input())
calories_per_day = int(input())

calories_per_day_burn = minutes_walk * times_per_day_walk * 5
half_calories_needed = calories_per_day / 2
if calories_per_day_burn >= half_calories_needed:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_per_day_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_per_day_burn}.")