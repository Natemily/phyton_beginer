line, count = input(), 0
for i in range(len(line)):
    if line[i] == line[i].lower() and line[i].lower() in ("qwertyuiopasdfghjklzxcvbnm"):
        count += 1
print(count)