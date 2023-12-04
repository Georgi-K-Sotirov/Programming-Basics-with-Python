record = float(input())
distance = float(input())
time_for_meter = float(input())
lost_time = distance // 50 * 30
total_time = distance * time_for_meter + lost_time
if total_time < record:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record:.2f} seconds slower.")