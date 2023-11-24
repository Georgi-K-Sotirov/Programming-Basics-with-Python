qty_joinery = int(input())
type_joinery = input()
type_of_delivery = input()
price_for_piece = 0
delivery_price = 0

if qty_joinery > 10:
    if type_joinery == "90X130":
        price_for_piece = 110
        if 60 >= qty_joinery > 30:
            price_for_piece *= 0.95
        elif qty_joinery > 60:
            price_for_piece *= 0.92
    elif type_joinery == "100X150":
        price_for_piece = 140
        if 80 >= qty_joinery > 40:
            price_for_piece *= 0.94
        elif qty_joinery > 80:
            price_for_piece *= 0.90
    elif type_joinery == "130X180":
        price_for_piece = 190
        if 50 >= qty_joinery > 20:
            price_for_piece *= 0.93
        elif qty_joinery > 50:
            price_for_piece *= 0.88
    elif type_joinery == "200X300":
        price_for_piece = 250
        if 50 >= qty_joinery > 25:
            price_for_piece *= 0.91
        elif qty_joinery > 50:
            price_for_piece *= 0.86
    if type_of_delivery == "With delivery":
        delivery_price = 60
    total_price = qty_joinery * price_for_piece + delivery_price
    if qty_joinery > 99:
        total_price *= 0.96
    print(f"{total_price:.2f} BGN")
else:
    print("Invalid order")
