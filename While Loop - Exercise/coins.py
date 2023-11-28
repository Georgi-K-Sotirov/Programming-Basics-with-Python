inserted_money = float(input())
inserted_money = int(inserted_money * 100)
coins_counter = 0

while inserted_money > 0:
    if inserted_money >= 200:
        coins_counter += 1
        inserted_money -= 200
    elif inserted_money >= 100:
        coins_counter += 1
        inserted_money -= 100
    elif inserted_money >= 50:
        coins_counter += 1
        inserted_money -= 50
    elif inserted_money >= 20:
        coins_counter += 1
        inserted_money -= 20
    elif inserted_money >= 10:
        coins_counter += 1
        inserted_money -= 10
    elif inserted_money >= 5:
        coins_counter += 1
        inserted_money -= 5
    elif inserted_money >= 2:
        coins_counter += 1
        inserted_money -= 2
    elif inserted_money >= 1:
        coins_counter += 1
        inserted_money -= 1
        break

print(f"{coins_counter:.0f}")