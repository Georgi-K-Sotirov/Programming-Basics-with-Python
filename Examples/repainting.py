needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours = int(input())

nylon_price = (needed_nylon + 2) * 1.50
paint_price = (needed_paint * 1.1) * 14.50
thinner_price = needed_thinner * 5
total_material_price = nylon_price + paint_price + thinner_price + 0.4
painter_price = (total_material_price * 0.3) * hours
final_price = total_material_price + painter_price

print(final_price)