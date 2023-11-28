number_of_tabs = int(input())
salery = int(input())

for _ in range(number_of_tabs):
    open_tab = input()
    if open_tab == "Facebook":
        salery -= 150
    elif open_tab == "Instagram":
        salery -= 100
    elif open_tab == "Reddit":
        salery -= 50
    if salery <= 0:
        break
if salery <= 0:
    print("You have lost your salary.")
else:
    print(salery)