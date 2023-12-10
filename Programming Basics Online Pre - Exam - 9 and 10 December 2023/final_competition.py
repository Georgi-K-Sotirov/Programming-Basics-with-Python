dancers = int(input())
points = float(input())
season = input()
place = input()

sum_for_dancer = 0

if place == "Bulgaria":
    sum_for_dancer = points * dancers
    if season == "summer":
        sum_for_dancer *= 0.95
    elif season == "winter":
        sum_for_dancer *= 0.92
elif place == "Abroad":
    sum_for_dancer = points * dancers * 1.5
    if season == "summer":
        sum_for_dancer *= 0.90
    elif season == "winter":
        sum_for_dancer *= 0.85

donation = sum_for_dancer * 0.75
sum_for_one_dancer = (sum_for_dancer - donation) / dancers

print(f"Charity - {donation:.2f}")
print(f"Money per dancer - {sum_for_one_dancer:.2f}")