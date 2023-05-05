command = ""

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stop")
    elif command == "help":
        print("start - to start the car \nstop - to stop the car \nquit - to exit")
    elif command == "quit":
        break
    else:
        print("I don't get you")