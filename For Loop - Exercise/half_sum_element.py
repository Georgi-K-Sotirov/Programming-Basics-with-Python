from math import  inf
number = int(input())
max_number = - inf
total_sum = 0
for _ in range(number):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number
diff = abs(max_number - (total_sum - max_number))
if max_number == total_sum - max_number:
    print(f"Yes")
    print(f"Sum = {max_number}")
else:
    print(f"No")
    print(f"Diff = {diff}")