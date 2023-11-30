stage_of_tournament = input()
type_of_ticket = input()
qty_tickets = int(input())
picture = input()
price = 0
if stage_of_tournament == "Quarter final":
    if type_of_ticket == "Standard":
        price = 55.5
    elif type_of_ticket == "Premium":
        price = 105.20
    elif type_of_ticket == "VIP":
        price = 118.90
elif stage_of_tournament == "Semi final":
    if type_of_ticket == "Standard":
        price = 75.88
    elif type_of_ticket == "Premium":
        price = 125.22
    elif type_of_ticket == "VIP":
        price = 300.40
elif stage_of_tournament == "Final":
    if type_of_ticket == "Standard":
        price = 110.10
    elif type_of_ticket == "Premium":
        price = 160.66
    elif type_of_ticket == "VIP":
        price = 400

total_price = qty_tickets * price
if total_price > 4000:
    total_price *= 0.75
elif total_price > 2000:
    total_price *= 0.9
    if picture == "Y":
        total_price += qty_tickets * 40
else:
    if picture == "Y":
        total_price += qty_tickets * 40

print(f"{total_price:.2f}")
