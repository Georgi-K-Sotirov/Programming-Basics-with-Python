capacity = float(input())
volume_suitcase = input()
total_suitcase = 0
counter = 1
while volume_suitcase != "End":
    volume_suitcase = float(volume_suitcase)
    if counter == 3:
        volume_suitcase *= 1.1
        counter = 1
    if capacity < volume_suitcase:
        break
    capacity -= volume_suitcase
    if capacity == 0:
        break
    counter += 1
    total_suitcase += 1
    volume_suitcase = input()
if volume_suitcase == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {total_suitcase} suitcases loaded.")