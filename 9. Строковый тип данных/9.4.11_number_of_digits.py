line, count = input(), 0
for i in range(0, 10):
    count += line.count(str(i))
print(count)
