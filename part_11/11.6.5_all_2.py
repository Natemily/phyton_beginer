numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.insert(10, 4)
numbers.insert(10, 5)
numbers.insert(10, 6)
del numbers[0]
numbers = numbers*2
numbers.insert(3, 25)
print(numbers)