import math

name_of_the_series = input()
time_for_episode = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
time_for_relax = time_for_break / 4

free_time = time_for_break - time_for_lunch - time_for_relax
difference = math.ceil(abs(free_time - time_for_episode))

if free_time > time_for_episode:
    print(f'You have enough time to watch {name_of_the_series} and left with {difference:.0f} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_the_series}, you need {difference:.0f} more minutes.")