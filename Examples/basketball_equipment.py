yearly_tax = int(input())

snickers_price = yearly_tax * 0.6
jersey_price = snickers_price * 0.8
ball_price = jersey_price / 4
accessories_price = ball_price / 5

final_price = yearly_tax + snickers_price + jersey_price + ball_price + accessories_price

print(final_price)