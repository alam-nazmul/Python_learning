try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invaild input")



try:
    age = int(input("Enter your age: "))
    income = 40000 / age
    print(income)
except ZeroDivisionError:
    print("Age can't be Zero")