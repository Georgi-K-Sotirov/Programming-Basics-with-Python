budget_for_trip = float(input())
puzzels_qty = int(input())
dolls_qty = int(input())
bears_qty = int(input())
minions_qty = int(input())
trucks_qty = int(input())

puzzels_price = 2.6
dolls_price = 3.0
bears_price = 4.1
minions_price = 8.2
trucks_price = 2.0

total_revenu = puzzels_price * puzzels_qty + dolls_price * dolls_qty \
               +bears_price * bears_qty + minions_price * minions_qty \
               + trucks_price * trucks_qty

total_toys_qty = puzzels_qty + dolls_qty + bears_qty + minions_qty + trucks_qty

if total_toys_qty >= 50:
    total_revenu *= 0.75
total_revenu *= 0.9

differens = abs(total_revenu - budget_for_trip)

if budget_for_trip > total_revenu:
    print(f'Not enough money! {differens:.2f} lv needed.')
else:
    print(f'Yes! {differens:.2f} lv left.')