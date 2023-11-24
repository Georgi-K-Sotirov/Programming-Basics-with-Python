budget = float(input())
mute_qty = int(input())
price_for_mute = float(input())

decor_price = budget * 0.1
price_for_all_mute = 0

if mute_qty >150:
    price_for_all_mute = mute_qty * price_for_mute * 0.9
else:
    price_for_all_mute = mute_qty * price_for_mute

total_expences = decor_price + price_for_all_mute
difference = abs(total_expences - budget)

if budget > total_expences:
    print("Action!")
    print(f'Wingard starts filming with {difference:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')