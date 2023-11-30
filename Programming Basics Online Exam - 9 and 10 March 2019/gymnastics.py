country = input()
category = input()
points = 0

if country == "Russia":
    if category == "ribbon":
        points = 9.1 + 9.4
    elif category == "hoop":
        points = 9.3 + 9.8
    elif category == "rope":
        points = 9.6 + 9
elif country == "Bulgaria":
    if category == "ribbon":
        points = 9.6 + 9.4
    elif category == "hoop":
        points = 9.55 + 9.75
    elif category == "rope":
        points = 9.5 + 9.4
elif country == "Italy":
    if category == "ribbon":
        points = 9.2 + 9.5
    elif category == "hoop":
        points = 9.25 + 9.35
    elif category == "rope":
        points = 9.7 + 9.15

percent = ((20 - points) / 20) * 100
print(f"The team of {country} get {points:.3f} on {category}.")
print(f"{percent:.2f}%")
