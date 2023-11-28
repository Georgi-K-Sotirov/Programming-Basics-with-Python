from math import inf

max_number = -inf

while True:
    data_input = input()
    if data_input == "Stop":
        break
    data_input = int(data_input)
    if data_input > max_number:
        max_number = data_input

print(max_number)