destination = input()
saved_money = 0
while destination != "End":
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        saved_money += float(input())
        if saved_money >= budget:
            print(f"Going to {destination}!")
    destination = input()
