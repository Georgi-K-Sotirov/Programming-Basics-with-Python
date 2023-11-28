money_needed_for_vacation = float(input())
budget = float(input())
spend_counter = 0
days_counter = 0

while True:
    if spend_counter == 5:
        break
    type_of_action = input()
    deposit = float(input())
    if type_of_action == "spend":
        spend_counter += 1
        budget -= deposit
    elif type_of_action == "save":
        budget += deposit
        spend_counter = 0
    days_counter += 1
    if money_needed_for_vacation <= budget:
        break
    if budget < 0:
        budget =0

if money_needed_for_vacation <= budget:
    print(f"You saved the money for {days_counter} days.")
else:
    print(f"You can't save the money.")
    print(days_counter)