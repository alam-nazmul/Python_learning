command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Start")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stop")
    elif command == "help":
        print("Start - to start the car \nStop - to stop the car \nquit - to exit")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't get it...")