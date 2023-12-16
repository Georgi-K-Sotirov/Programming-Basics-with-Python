team = input()
stock = input()
qty_souvenirs = int(input())

stock_price = 0
if team == "Argentina":
    if stock == "flags":
        stock_price = 3.25
    elif stock == "caps":
        stock_price = 7.20
    elif stock == "posters":
        stock_price = 5.1
    elif stock == "stickers":
        stock_price = 1.25
    else:
        print("Invalid stock!")
elif team == "Brazil":
    if stock == "flags":
        stock_price = 4.20
    elif stock == "caps":
        stock_price = 8.50
    elif stock == "posters":
        stock_price = 5.35
    elif stock == "stickers":
        stock_price = 1.2
    else:
        print("Invalid stock!")
elif team == "Croatia":
    if stock == "flags":
        stock_price = 2.75
    elif stock == "caps":
        stock_price = 6.90
    elif stock == "posters":
        stock_price = 4.95
    elif stock == "stickers":
        stock_price = 1.1
    else:
        print("Invalid stock!")
elif team == "Denmark":
    if stock == "flags":
        stock_price = 3.1
    elif stock == "caps":
        stock_price = 6.5
    elif stock == "posters":
        stock_price = 4.8
    elif stock == "stickers":
        stock_price = 0.9
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")

total_price = stock_price * qty_souvenirs

if total_price > 0:
    print(f"Pepi bought {qty_souvenirs} {stock} of {team} for {total_price:.2f} lv.")