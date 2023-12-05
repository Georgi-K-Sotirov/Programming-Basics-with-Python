drink = input()
sugar = input()
qty = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.9 * 0.65
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
    if qty >= 5:
        price *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1 * 0.65
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = 0.5 * 0.65
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

total_sum = qty * price
if total_sum > 15:
    total_sum *= 0.8
print(f"You bought {qty} cups of {drink} for {total_sum:.2f} lv.")