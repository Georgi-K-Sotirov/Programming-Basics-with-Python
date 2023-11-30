from math import  floor, ceil

price_for_racket = float(input())
qty_rackets = int(input())
qty_sneakers = int(input())
price_for_sneakers = price_for_racket / 6

total_price = ((price_for_sneakers * qty_sneakers) + (price_for_racket * qty_rackets)) * 1.2

price_for_tennis_player = floor(total_price / 8)
price_for_sponsors = ceil((total_price / 8) * 7 )

print(f"Price to be paid by Djokovic {price_for_tennis_player}")
print(f"Price to be paid by sponsors {price_for_sponsors}")