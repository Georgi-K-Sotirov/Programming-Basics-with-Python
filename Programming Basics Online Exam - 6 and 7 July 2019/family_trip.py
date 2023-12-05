budget = float(input())
nights = int(input())
price_for_night = float(input())
percent_additional_expenses = int(input())

total_nights = nights * price_for_night
if nights > 7:
    total_nights *= 0.95
additional_expenses = budget * percent_additional_expenses / 100
total_sum = total_nights + additional_expenses
diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")