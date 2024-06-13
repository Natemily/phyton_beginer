line, count, letter = input(), 0, ""
for i in range(len(line)):
    if line.count(str(line[i])) >= count:
        count = line.count(str(line[i]))
        letter = str(line[i])
print(letter)