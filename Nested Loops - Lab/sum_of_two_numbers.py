start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter = 0
condition_break = False

for i in range (start_number, end_number+1):
    for j in range (start_number, end_number+1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            condition_break = True
            break
    if condition_break:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")
