first_match = input()
second_match = input()
third_match = input()
wins = 0
draws = 0
lost = 0
first_team_goals = first_match[0]
first_team_goals = int(first_team_goals)
second_team_goals = first_match[2]
second_team_goals = int(second_team_goals)
if first_team_goals > second_team_goals:
    wins += 1
elif first_team_goals == second_team_goals:
    draws += 1
elif first_team_goals < second_team_goals:
    lost += 1


first_team_goals = second_match[0]
first_team_goals = int(first_team_goals)
second_team_goals = second_match[2]
second_team_goals = int(second_team_goals)
if first_team_goals > second_team_goals:
    wins += 1
elif first_team_goals == second_team_goals:
    draws += 1
elif first_team_goals < second_team_goals:
    lost += 1

first_team_goals = third_match[0]
first_team_goals = int(first_team_goals)
second_team_goals = third_match[2]
second_team_goals = int(second_team_goals)
if first_team_goals > second_team_goals:
    wins += 1
elif first_team_goals == second_team_goals:
    draws += 1
elif first_team_goals < second_team_goals:
    lost += 1

print(f"Team won {wins} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draws}")