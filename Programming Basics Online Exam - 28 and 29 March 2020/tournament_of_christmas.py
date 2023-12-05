days = int(input())
days_win = 0
days_lost = 0
money = 0
for games_for_a_day in range(days):
    name_of_game = input()
    wins_per_day = 0
    lost_per_day = 0
    money_per_day = 0
    while name_of_game != "Finish":
        win_lose = input()
        if win_lose == "win":
            wins_per_day += 1
            money_per_day += 20
        elif win_lose == "lose":
            lost_per_day += 1
        name_of_game = input()
    if wins_per_day > lost_per_day:
        days_win += 1
        money_per_day *= 1.1
    else:
        days_lost += 1
    money += money_per_day
if days_win > days_lost:
    money *= 1.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")