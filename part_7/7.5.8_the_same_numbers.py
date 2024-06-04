n = int(input())
a = b = n % 10
flag = "YES"

while n > 0:
    b = n % 10
    if a != b:
        flag = "NO"
    n //= 10

print(flag)