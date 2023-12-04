number = int(input())
counter = 1
for i in range(1, number + 1):
    end_condition = False
    for j in range(1, i + 1):
        print(counter, end = " ")
        counter += 1
        if counter > number:
            end_condition = True
            break
    print()
    if end_condition:
        break