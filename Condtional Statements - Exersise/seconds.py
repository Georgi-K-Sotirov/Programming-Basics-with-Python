first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time_in_seconds = first_time + second_time + third_time
minutes = total_time_in_seconds // 60
seconds = total_time_in_seconds % 60

print(f'{minutes}:{seconds:02d}')