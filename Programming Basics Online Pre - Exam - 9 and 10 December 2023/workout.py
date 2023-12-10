from math import ceil
days_running = int(input())
kilometers = float(input())
total_kilometers = kilometers
for _ in range(days_running):
    percent_more_for_a_day = int(input())
    kilometers += kilometers * percent_more_for_a_day  / 100
    total_kilometers += kilometers

diff = ceil(abs(1000 - total_kilometers))
if total_kilometers >= 1000:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")