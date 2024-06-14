line = input()
count = 0
index = -1
for i in range(len(line)):
    if line[i] == "f":
        count += 1
        if count == 2:
            index = i
if count >=2:
    print(index)
elif count == 1:
    print(-1)
else:
    print(-2)