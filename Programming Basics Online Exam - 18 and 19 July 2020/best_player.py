best_player = ""
goals = 0

player_name = input()
while player_name != "END":
    goals_player = int(input())
    if goals_player > goals:
        best_player = player_name
        goals = goals_player
    if goals >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if goals >= 3:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")
