age = input()

kids = 0
adults = 0


while age != "Christmas":
    age = int(age)
    if age <= 16:
        kids += 1
    else:
        adults += 1
    age = input()

money_toys = kids * 5
money_sweaters = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {money_sweaters}")