n, c, flag = int(input()), 0, "YES"

while n > 0 and flag == "YES":
    a = n % 10
    if a >= c:
        c = a
    else:
        flag = "NO"
    n //= 10

print(flag)