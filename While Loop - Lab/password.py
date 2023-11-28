user_name = input()
password = input()

while True:
    user_password = input()

    if user_password == password:
        print(f"Welcome {user_name}!")
        break
