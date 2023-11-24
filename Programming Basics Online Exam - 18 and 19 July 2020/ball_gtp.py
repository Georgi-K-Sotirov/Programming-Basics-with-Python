n = int(input())

total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors = 0
divide_count = 0

# Въвеждане на цветовете и изчисляване на точките
for _ in range(n):
    color = input()
    if color == "black":  # Черна топка
        total_points //= 2
        divide_count += 1
    else:
        total_points += points
        if color == "red":
            red_balls += 1
        elif color == "orange":
            orange_balls += 1
        elif color == "yellow":
            yellow_balls += 1
        elif color == "white":
            white_balls += 1

# Изход
print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {divide_count}")
