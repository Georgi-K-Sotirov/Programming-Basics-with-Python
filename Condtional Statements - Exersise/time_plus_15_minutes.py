hour = int(input())
minutes = int(input())

time_in_seconds = hour * 60 + minutes + 15
hour_plus = time_in_seconds // 60
minutes_plus = time_in_seconds % 60

if hour_plus > 23:
    hour_plus -= 24
if minutes_plus > 59:
    minutes_plus -= 60

print(f'{hour_plus}:{minutes_plus:02d}')