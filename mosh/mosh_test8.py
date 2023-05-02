command = ""
started = False
while True:
    command = input("Enter your cmd > ").lower()
    if command == "start":
        if started:
            print("Car has already started")
        else:
        print("Car is started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
        print("Car is stopped")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - quit this")
    elif command == "quit":
        break
    else:
        print("Sorry")
