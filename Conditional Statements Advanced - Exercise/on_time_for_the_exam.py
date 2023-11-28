hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())
total_minutes_exam = hour_exam * 60 + minutes_exam
total_minutes_arrive = hour_arrive * 60 + minutes_arrive
difference = abs(total_minutes_exam - total_minutes_arrive)
hours = difference // 60
minutes = difference % 60
if total_minutes_exam < total_minutes_arrive:
    print("Late")
    if difference < 60:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hours}:{minutes:02d} hours after the start")
elif total_minutes_exam - 30 <= total_minutes_arrive <= total_minutes_exam:
    print("On time")
    if difference != 0:
        print(f"{minutes} minutes before the start")
elif total_minutes_exam - 30 > total_minutes_arrive:
    print("Early")
    if difference < 60:
        print(f"{minutes} minutes before the start")
    else:
        print(f"{hours}:{minutes:02d} hours before the start")
