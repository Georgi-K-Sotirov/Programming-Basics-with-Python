from math import inf

min_number = inf

while True:
    data_input = input()
    if data_input == "Stop":
        break
    data_input = int(data_input)
    if data_input < min_number:
        min_number = data_input

print(min_number)