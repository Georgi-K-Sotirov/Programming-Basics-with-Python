minute_control = int(input())
seconds_control = int(input())
distance = float(input())
seconds_for_hundred_meters = int(input())
total_control = seconds_control + minute_control * 60
time_user = ((distance / 100) * seconds_for_hundred_meters) - ((distance / 120) * 2.5)
diff = time_user - total_control
if time_user <= total_control:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_user:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")