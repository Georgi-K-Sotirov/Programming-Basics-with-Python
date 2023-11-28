limit = int(input())
total_sum = 0

while True:
    number = int(input())
    total_sum += number
    if total_sum >= limit:
        print(total_sum)
        break