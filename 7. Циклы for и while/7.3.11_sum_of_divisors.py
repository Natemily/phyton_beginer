tl, n = 0, int(input())
for i in range(1, n+1):
    if n % i == 0:
        tl += i
print(tl)