number_of_groups = int(input())
total_number_people = 0
group_musala =  0
group_monblan =  0
group_kilimandjaro =  0
group_k2 =  0
group_everest =  0
for group in range(number_of_groups):
    number_people = int(input())
    total_number_people += number_people
    if number_people <= 5:
        group_musala += number_people
    elif number_people <= 12:
        group_monblan += number_people
    elif number_people <= 25:
        group_kilimandjaro += number_people
    elif number_people <= 40:
        group_k2 += number_people
    else:
        group_everest += number_people

percent_musala = group_musala / total_number_people * 100
percent_monblan = group_monblan / total_number_people * 100
percent_kilimandjaro = group_kilimandjaro / total_number_people * 100
percent_k2 = group_k2 / total_number_people * 100
percent_everest = group_everest / total_number_people * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
