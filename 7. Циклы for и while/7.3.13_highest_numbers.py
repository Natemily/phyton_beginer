n = int(input())
mx1 = mx2 = 0

for i in range(1, n+1):
    i = int(input())
    if i > mx1:
        mx2, mx1 = mx1, i
    elif mx2 < i < mx1:
        mx2 = i

print(mx1, mx2, sep='\n')