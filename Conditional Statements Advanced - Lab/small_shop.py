drink = input()
city = input()
qty = float(input())
price = 0

if city == 'Sofia':
    if drink == 'coffee':
        price = 0.5
    elif drink == 'water':
        price = 0.8
    elif drink == 'beer':
        price = 1.2
    elif drink == 'sweets':
        price = 1.45
    elif drink == 'peanuts':
        price = 1.6
elif city == 'Plovdiv':
    if drink == 'coffee':
        price = 0.4
    elif drink == 'water':
        price = 0.7
    elif drink == 'beer':
        price = 1.15
    elif drink == 'sweets':
        price = 1.30
    elif drink == 'peanuts':
        price = 1.5
elif city == 'Varna':
    if drink == 'coffee':
        price = 0.45
    elif drink == 'water':
        price = 0.7
    elif drink == 'beer':
        price = 1.1
    elif drink == 'sweets':
        price = 1.35
    elif drink == 'peanuts':
        price = 1.55

print(qty * price)

