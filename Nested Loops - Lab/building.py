floor_number = int(input())
room_number = int(input())

for floor in reversed(range(1, floor_number + 1)):
    for room in range(room_number):
        room_type = "A" if floor % 2 else "O"
        if floor == floor_number:
            room_type = "L"
        print(f"{room_type}{floor}{room}", end=" ")
    print()
