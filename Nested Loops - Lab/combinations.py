number = int(input())
counter = 0
for x1 in range(number+1):
    for x2 in range(number+1):
        for x3 in range(number+1):
            result = x1 + x2 + x3
            if result == number:
                counter += 1
print(counter)