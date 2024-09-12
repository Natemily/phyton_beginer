n, a, b = int(input()), [], []
for i in range(n):
    a.append(input())
k = input()
for num in a:
    if k.lower() in num.lower():
        b.append(num)
print(*b, sep="\n")