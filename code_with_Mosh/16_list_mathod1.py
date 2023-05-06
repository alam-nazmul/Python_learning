numbers = [5, 2, 3, 8, 10]

numbers.append(100)
print(numbers)

numbers.insert(0, 200)
print(numbers)

numbers.remove(200)
print(numbers)

#numbers.clear()
#print(numbers)

numbers.pop()
print(numbers)

print(numbers.count(3))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)