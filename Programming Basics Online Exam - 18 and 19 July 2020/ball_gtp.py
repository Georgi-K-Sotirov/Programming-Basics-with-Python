number = int(input())
total_point = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_balls = 0

for i in range(number):
    ball_color = input()
    if ball_color == "red":
        total_point += 5
        red_balls += 1
    elif ball_color == "orange":
        total_point += 10
        orange_balls += 1
    elif ball_color == "yellow":
        total_point += 15
        yellow_balls += 1
    elif ball_color == "white":
        total_point += 20
        white_balls += 1
    elif ball_color == "black":
        total_point = int(total_point / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f"Total points: {int(total_point)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")