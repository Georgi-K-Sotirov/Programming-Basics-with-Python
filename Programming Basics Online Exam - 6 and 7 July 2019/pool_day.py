from math import ceil
qty_people = int(input())
entry_fee = float(input())
price_for_lounger = float(input())
price_for_umbrella = float(input())

total_sum = (qty_people * entry_fee) + (ceil(qty_people / 2) * price_for_umbrella) + \
            (ceil(qty_people * 0.75) * price_for_lounger)
print(f"{total_sum:.2f} lv.")