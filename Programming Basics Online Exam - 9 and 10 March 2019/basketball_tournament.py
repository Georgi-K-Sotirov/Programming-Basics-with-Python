total_games = 0
won_games = 0
lost_games = 0
tournament = input()

while tournament != "End of tournaments":

    number_game_per_tournament = int(input())
    total_games += number_game_per_tournament
    for game_number in range(1, number_game_per_tournament + 1):
        point_team_desy = int(input())
        points_rival_team = int(input())
        diff = abs(points_rival_team - point_team_desy)
        if point_team_desy > points_rival_team:
            won_games += 1
            print(f"Game {game_number} of tournament {tournament}:"
                  f" win with {diff} points.")
        else:
            lost_games += 1
            print(f"Game {game_number} of tournament {tournament}: "
                  f"lost with {diff} points.")
    tournament = input()

percent_win = won_games / total_games * 100
percent_lost = lost_games / total_games * 100

print(f"{percent_win:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")