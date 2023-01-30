# INPUT always return by str form

name = input("What is your name?: ")

print("Hello", name)

seconds = input("Please enter the number of seconds: ")
total_sec = int(seconds)

hours = total_sec // 3600
remain_sec = total_sec % 3600
minutes = remain_sec // 60
secs_finally_remain = remain_sec % 60

print("Hrs=", hours, "Mins=", minutes, "sec=", secs_finally_remain)