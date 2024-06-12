line, a = input(), 0
for i in range(1, len(line)):
    if line[i] == line[i-1]:
        a += 1
print(a)