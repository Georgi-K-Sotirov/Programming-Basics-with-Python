screen_type = input()
row = int(input())
collum = int(input())
total_seats = row * collum
ticket_price_per_seat = 0

if screen_type == "Premiere":
    ticket_price_per_seat = 12
elif screen_type == "Normal":
    ticket_price_per_seat = 7.5
elif screen_type == "Discount":
    ticket_price_per_seat = 5

print(f"{ticket_price_per_seat * total_seats:.2f}")