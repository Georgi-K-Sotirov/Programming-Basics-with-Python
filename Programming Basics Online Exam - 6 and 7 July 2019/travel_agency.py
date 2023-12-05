city = input()
type_packet = input()
vip_user = input()
qty_days = int(input())
price = 0

if qty_days < 1:
    print("Days must be positive number!")
if city == "Bansko" or city == "Borovets":
    if type_packet == "noEquipment":
        price = 80
        if vip_user == "yes":
            price *= 0.95
    elif type_packet == "withEquipment":
        price = 100
        if vip_user == "yes":
            price *= 0.9
elif city == "Varna" or city == "Burgas":
    if type_packet == "noBreakfast":
        price = 100
        if vip_user == "yes":
            price *= 0.93
    elif type_packet == "withBreakfast":
        price = 130
        if vip_user == "yes":
            price *= 0.88
if price == 0:
    print("Invalid input!")
total_price = qty_days * price
if qty_days >= 7:
    total_price = (qty_days - 1) * price
if 0 < qty_days and price > 0:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
