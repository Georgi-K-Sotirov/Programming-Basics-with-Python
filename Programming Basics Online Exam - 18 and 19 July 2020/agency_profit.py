name_of_the_company = input()
qty_thickets_for_adults = int(input())
qty_thickets_for_children = int(input())
price_thickets_for_adults = float(input())
service_fee = float(input())
price_thickets_for_children = price_thickets_for_adults * 0.3

total_sum = (qty_thickets_for_children * price_thickets_for_children) \
            + (qty_thickets_for_adults * price_thickets_for_adults) \
            + ((qty_thickets_for_adults + qty_thickets_for_children) * service_fee)
profit = total_sum * 0.2

print(f"The profit of your agency from {name_of_the_company} tickets is {profit.2f} lv.")