width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
box_counter = 0

while volume >= box_counter:
    moved_boxes = input()
    if moved_boxes == "Done":
        break
    moved_boxes = int(moved_boxes)
    box_counter += moved_boxes
diff = abs(volume - box_counter)
if volume >= box_counter:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")