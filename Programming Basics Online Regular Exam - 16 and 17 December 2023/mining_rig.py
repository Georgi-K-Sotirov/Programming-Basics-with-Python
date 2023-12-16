from math import ceil

video_card_price = int(input())
transition = int(input())
price_electricity = float(input())
profit_rom_one_card_in_one_day = float(input())

total_price_cards = video_card_price * 13
total_price_transitions = transition * 13
total_spend = total_price_cards + total_price_transitions + 1000
total_profit = 13 * (profit_rom_one_card_in_one_day - price_electricity)

days_for_profit = ceil(total_spend / total_profit)
print(total_spend)
print(f"{days_for_profit}")