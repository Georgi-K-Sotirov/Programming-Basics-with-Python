from math import floor

record = float(input())
distance = int(input())
time_for_one_meter = float(input())

deley_time =( distance // 15 ) * 12.5

total_time = ( distance * time_for_one_meter ) + deley_time
differece = total_time - record

if total_time < record :
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {differece:.2f} seconds slower.')