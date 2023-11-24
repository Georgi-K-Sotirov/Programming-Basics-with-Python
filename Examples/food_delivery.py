chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegan_price = vegan_menu * 8.15
desert_price = (chicken_price + fish_price + vegan_price) * 0.2
delivery_price = 2.5

total_price = chicken_price + fish_price + vegan_price + desert_price + delivery_price
print(total_price)
