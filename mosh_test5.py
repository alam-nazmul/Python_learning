weight = input("Enter your weight: ")
unit = input("Enter the unit (Kgs / Lbs): ")
weight = float(weight)
unit = unit.lower()

if unit == "kgs":
    weight = weight / 0.45
    print (f'Your weight is {weight} lbs')
elif unit == "lbs":
    weight = weight * 0.45
    print (f'Your weight is {weight} kgs')
else:
    print("Enter all information properly.")