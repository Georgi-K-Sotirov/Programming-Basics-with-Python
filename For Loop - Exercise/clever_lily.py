age = int(input())
laundry_price = float(input())
price_per_toy = int(input())
total_toys = 0
total_money = 0
current_birthday_money = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1
total_money += total_toys * price_per_toy
diff = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")