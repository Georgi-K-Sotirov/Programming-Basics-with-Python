number = int(input())

for current_number in range(1111, 9999 + 1):
    current_number = str(current_number)
    special_number = True
    for digit in current_number:
        if int(digit) == 0 or number % int(digit) != 0:
            special_number = False
            break
    if special_number:
        print(current_number, end=" ")
