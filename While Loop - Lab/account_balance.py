balanse = 0

while True:
    user_input = input()
    if user_input == "NoMoreMoney":
        break
    money_input = float(user_input)
    if money_input >= 0:
        print(f"Increase: {money_input:.2f}")
        balanse += money_input
    else:
        print("Invalid operation!")
        break
print(f"Total: {balanse:.2f}")