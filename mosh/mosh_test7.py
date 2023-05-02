command = ""
while command != "quit":
    command = input("Enter your cmd > ").lower()
    if command == "start":
        print("Car is started")
    elif command == "stop":
        print("Car is stopped")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - quit this")
    else:
        print("Sorry")