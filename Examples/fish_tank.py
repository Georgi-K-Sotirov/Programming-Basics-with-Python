length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = length * width * height
water_volume = (tank_volume / 1000) * (1 - (percent/100))

print(water_volume)