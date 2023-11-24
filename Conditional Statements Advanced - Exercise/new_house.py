types_of_flower = input()
qty_of_flowers = int(input())
budget = int(input())
price_per_flower = 0

if types_of_flower == "Roses":
    price_per_flower = 5
    if qty_of_flowers > 80:
        price_per_flower *= 0.9
elif types_of_flower == "Dahlias":
    price_per_flower = 3.80
    if qty_of_flowers > 90:
        price_per_flower *= 0.85
elif types_of_flower == "Tulips":
    price_per_flower = 2.8
    if qty_of_flowers > 80:
        price_per_flower *= 0.85
elif types_of_flower == "Narcissus":
    price_per_flower = 3
    if qty_of_flowers < 120:
        price_per_flower *= 1.15
elif types_of_flower == "Gladiolus":
    price_per_flower = 2.5
    if qty_of_flowers < 80:
        price_per_flower *= 1.2

total_sum = price_per_flower * qty_of_flowers
difference = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {qty_of_flowers} {types_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
