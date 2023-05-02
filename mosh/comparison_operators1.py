temperature = input("Enter the temperature: ")
temperature = int(temperature)

if temperature >= 30:
    print("It's a hot day.")
elif temperature <= 10:
    print("It's a cold day.")
else:
    print("It's neither hot nor cold")