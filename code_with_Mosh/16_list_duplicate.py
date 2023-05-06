numbers = [1, 3, 5, 7, 9, 7, 5, 3]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)