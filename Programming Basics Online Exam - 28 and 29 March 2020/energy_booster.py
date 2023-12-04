fruit = input()
size_packet = input()
qty_buy = int(input())
price_per_piece = 0
if fruit == "Watermelon":
    if size_packet == "small":
        qty_buy *= 2
        price_per_piece = 56
    elif size_packet == "big":
        qty_buy *= 5
        price_per_piece = 28.70
elif fruit == 'Mango':
    if size_packet == "small":
        qty_buy *= 2
        price_per_piece = 36.66
    elif size_packet == "big":
        qty_buy *= 5
        price_per_piece = 19.60
elif fruit == "Pineapple":
    if size_packet == "small":
        qty_buy *= 2
        price_per_piece = 42.10
    elif size_packet == "big":
        qty_buy *= 5
        price_per_piece = 24.80
elif fruit == "Raspberry":
    if size_packet == "small":
        qty_buy *= 2
        price_per_piece = 20
    elif size_packet == "big":
        qty_buy *= 5
        price_per_piece = 15.20

total_price = qty_buy * price_per_piece
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price /= 2
print(f"{total_price:.2f} lv.")