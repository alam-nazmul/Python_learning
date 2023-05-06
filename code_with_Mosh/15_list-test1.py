numbers = [25, 78, 65, 89, 211, 784, 788]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)