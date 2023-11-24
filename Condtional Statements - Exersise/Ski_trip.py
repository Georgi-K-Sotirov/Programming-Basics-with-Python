days_of_stay = int(input())
type_of_room = input()
grade = input()
nights = days_of_stay - 1
price_per_night = 0

if type_of_room == "room for one person":
    price_per_night = 18
elif type_of_room == "apartment":
    price_per_night = 25
    if nights < 10:
        price_per_night *= 0.7
    elif 10 <= nights <= 15:
        price_per_night *= 0.65
    elif nights > 15:
        price_per_night *= 0.5
elif type_of_room == "president apartment":
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif 10 <= nights <= 15:
        price_per_night *= 0.85
    elif nights > 15:
        price_per_night *= 0.8
if grade == "positive":
    price_per_night *= 1.25
elif grade == "negative":
    price_per_night *= 0.9

print(f"{price_per_night*nights:.2f}")