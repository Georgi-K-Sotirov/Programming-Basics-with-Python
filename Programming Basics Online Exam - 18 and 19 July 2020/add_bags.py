price_for_20kg = float(input())
kilos_of_bags = float(input())
day_until = int(input())
qty_bags = int(input())
price_for_10_to_20kg = price_for_20kg * 0.5
price_for_up_to_10kg = price_for_20kg * 0.2
additional_fee = 0

if kilos_of_bags < 10:
    additional_fee = price_for_up_to_10kg
elif 10 <= kilos_of_bags <= 20:
    additional_fee = price_for_10_to_20kg
elif kilos_of_bags > 20:
    additional_fee = price_for_20kg

if day_until > 30:
    additional_fee *= 1.1
elif 7 <= day_until <= 30:
    additional_fee *= 1.15
elif day_until < 7:
    additional_fee *= 1.4

total_fee = qty_bags * additional_fee
print(f"The total price of bags is: {total_fee:.2f} lv. ")