name_of_the_book = input()
book_counter = 0

while True:
    book = input()
    if book == name_of_the_book:
        break
    if book == "No More Books":
        break
    book_counter += 1
if book == name_of_the_book:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
