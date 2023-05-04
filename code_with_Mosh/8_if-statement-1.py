user_feedback = input("How about today? : ")

if user_feedback == "hot":
    print(f'Its a {user_feedback} day')
    print("Drink plenty of water")
elif user_feedback == "cold":
    print(f'Its a {user_feedback} day')
    print("Wear warm clothes")
else:
    print("It's a lovely day")