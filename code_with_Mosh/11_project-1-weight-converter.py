weight = input("Enter your weight: ")
unit = input("Enter the unit (Kg / Lb): ")

weight = int(weight)
unit = unit.upper()

if unit == "KG":
    weight_in_pound = weight * 2.2
    print(f'Your weight is {int(weight_in_pound)} pounds')
elif unit == "LB":
    weight_in_kilograms = weight * 0.45
    print(f'Your weight is {int(weight_in_kilograms)} Kgs')