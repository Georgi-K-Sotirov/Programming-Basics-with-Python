price_tshirt = float(input())
price_for_bonus = float(input())

price_shorts = price_tshirt * 0.75
price_socks = price_shorts * 0.2
price_boots = (price_shorts + price_tshirt) * 2

total_sum = (price_boots + price_socks + price_shorts + price_tshirt) * 0.85
diff = abs(total_sum - price_for_bonus)
if total_sum >= price_for_bonus:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")