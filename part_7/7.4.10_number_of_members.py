line = input()
cnt = 0

while line != "стоп" and line != "хватит" and line != "достаточно":
    cnt += 1
    line = input()

print(cnt)