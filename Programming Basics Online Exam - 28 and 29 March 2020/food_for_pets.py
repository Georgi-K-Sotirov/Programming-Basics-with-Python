days = int(input())
total_food = float(input())
dog_eaten_food = 0
cat_eaten_food = 0
total_eaten_food = 0
total_eaten_biscuits = 0

for num in range (1, days + 1):
    dog_eats_day = int(input())
    cat_eats_day = int(input())
    dog_eaten_food += dog_eats_day
    cat_eaten_food += cat_eats_day
    total_eaten_food += dog_eats_day + cat_eats_day
    if num % 3 == 0:
        total_eaten_biscuits += (dog_eats_day + cat_eats_day) * 0.1

percent_eaten = total_eaten_food / total_food * 100
percent_dog = dog_eaten_food / total_eaten_food * 100
percent_cat = cat_eaten_food / total_eaten_food * 100
print(f"Total eaten biscuits: {total_eaten_biscuits:.0f}gr.")
print(f"{percent_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")