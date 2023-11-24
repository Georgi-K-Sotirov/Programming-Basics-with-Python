budget = float(input())
video_qty = int(input())
proccess_qty = int(input())
ram_qty = int(input())

video_price = 250 * video_qty
proccess_price = (video_price * 0.35) * proccess_qty
ram_price = (video_price * 0.1) * ram_qty

total_price = video_price + proccess_price + ram_price

if video_qty > proccess_qty:
    total_price *= 0.85

differense = abs(budget - total_price)

if budget > total_price:
    print(f'You have {differense:.2f} leva left')
else:
    print(f'Not enough money! You need {differense:.2f} leva more!')