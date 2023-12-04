movie_name = input()
student_counter = 0
standard_counter = 0
kid_counter = 0

while movie_name != "Finish":
    empty_seats = int(input())
    used_seats = 0
    for _ in range(empty_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_counter += 1
        elif current_ticket == "standard":
            standard_counter += 1
        elif current_ticket == "kid":
            kid_counter += 1
        used_seats += 1
    percent_current_film = used_seats / empty_seats * 100
    print(f"{movie_name} - {percent_current_film:.2f}% full.")
    movie_name = input()

total_tickets_sold = student_counter + standard_counter + kid_counter
percent_student = student_counter / total_tickets_sold * 100
percent_standard = standard_counter / total_tickets_sold * 100
percent_kid = kid_counter / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")