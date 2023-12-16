locations = int(input())

for current_location in range(locations):
    expected_average_yield = float(input())
    day_for_current_location = int(input())
    average_mined_gold = 0.0
    for current_day in range(day_for_current_location):
        gold_mined_a_day = float(input())
        average_mined_gold += gold_mined_a_day
    average_mined_gold_a_day = average_mined_gold / day_for_current_location
    if average_mined_gold_a_day >= expected_average_yield:
        print(f"Good job! Average gold per day: {average_mined_gold_a_day:.2f}.")
    else:
        print(f"You need {(expected_average_yield - average_mined_gold_a_day):.2f} gold.")