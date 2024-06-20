n, sum, k, pr = int(input()), 0, 0, 1
i = 1
fl = n%10
f1 = 0

while n > 0:
    a = n%10
    sum += a
    k += 1
    pr *= a
    f1=n
    n //= 10

print(sum, k, pr, sum/k, f1, fl+f1, sep="\n")