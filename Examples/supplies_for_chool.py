pencils_packages = int(input())
markers_packages = int(input())
cleaner_liters = int(input())
discount = int(input())

pencils_price = pencils_packages * 5.80
markers_price = markers_packages * 7.20
cleaner_price = cleaner_liters * 1.20

total_price = pencils_price + markers_price + cleaner_price
final_price = total_price * (1 - (discount / 100))

print(final_price)