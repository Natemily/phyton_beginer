n, a = int(input()), []
for i in range(n):
    a.append(input())
k, b = int(input()), []
for i in range(k):
    b.append(input())

for i in range(len(a)):
    count = 0
    for j in range(len(b)):
        if b[j].lower() in a[i].lower():
            count += 1
            if count == len(b) - 1:
                print(a[i])
                break