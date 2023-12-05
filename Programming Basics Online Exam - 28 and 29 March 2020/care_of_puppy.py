food_bayed = int(input())
food_bayed_in_grams = food_bayed * 1000
eating_a_day = input()
total_eaten = 0
while eating_a_day != "Adopted":
    eating_a_day_int = int(eating_a_day)
    total_eaten += eating_a_day_int
    eating_a_day = input()
diff = abs(total_eaten - food_bayed_in_grams)
if food_bayed_in_grams >= total_eaten:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")