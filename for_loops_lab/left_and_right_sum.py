number = int(input())
left_sum = 0
right_sum = 0

for i in range(number):
    current_number = int(input())
    left_sum += current_number

for i in range(number):
    current_number = int(input())
    right_sum += current_number
diff = abs(right_sum - left_sum)
if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")