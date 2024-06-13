line = input()
a = "YES"

for i in range(0, len(line)):
    if line[i] != line[len(line) - 1 - i]:
        a = "NO"
        break

print(a)