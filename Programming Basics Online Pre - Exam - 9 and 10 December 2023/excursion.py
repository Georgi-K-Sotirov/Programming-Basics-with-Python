people = int(input())
nights = int(input())
transport_cards = int(input())
qty_tickets_museum = int(input())

nights_price = 20
transport_cards_price = 1.6
museum_price = 6

total_sum_one_person = (nights * nights_price) + (transport_cards_price * transport_cards) + museum_price * qty_tickets_museum
total_sum = (total_sum_one_person * people) * 1.25

print(f'{total_sum:.2f}')