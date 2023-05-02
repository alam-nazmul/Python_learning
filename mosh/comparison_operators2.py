name = input("Enter your name: ")

if len(name) < 3:
    print("The minimum characters will be 3")
elif len(name) > 50:
    print("The maximun characters will be 50")
else:
    print("Name looks good")