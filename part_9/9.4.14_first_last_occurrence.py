line = input()
count = line.count("f")
if count == 1:
    print(line.find("f"))
elif count > 1:
    print(line.find("f"), line.rfind("f"))
else:
    print("NO")