tax_for_one_year = int(input())
sneakers = tax_for_one_year * 0.6
jersey = sneakers * 0.8
ball = jersey / 4
accessories = ball / 5

total_price = tax_for_one_year + sneakers +jersey + ball + accessories

print(f"{total_price:.2f}")