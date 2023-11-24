first_player = input()
second_player = input()
first_player_points = 0
second_player_point = 0

for _ in range (18):
    first_player_card = input()
    if first_player_card == "End of game":
        print(f"{first_player} has {first_player_points} points")
        print(f"{second_player} has {second_player_point} points")
        break
    else:
        second_player_card = input()
        if second_player_card == "End of game":
            print(f"{first_player} has {first_player_points} points")
            print(f"{second_player} has {second_player_point} points")
            break
        else:
            first_player_card = int(first_player_card)
            second_player_card = int(second_player_card)
            if first_player_card > second_player_card:
                first_player_points += first_player_card - second_player_card
            elif first_player_card < second_player_card:
                second_player_point += second_player_card - first_player_card
            elif first_player_card == second_player_card:
                print("Number wars!")
                first_player_card_war = int(input())
                second_player_card_war = int(input())
                if first_player_card_war > second_player_card_war:
                    print(f"{first_player} is winner with {first_player_points} points")
                elif second_player_card_war > first_player_card_war:
                    print(f"{second_player} is winner with {second_player_point} points")
                break