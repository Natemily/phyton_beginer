num = int(input())
mn, mx = 9, 0

while num > 0:
    a = num%10
    if a >= mx:
        mx = a
    if a <= mn:
        mn = a
    num //= 10

print("Максимальная цифра равна", mx)
print("Минимальная цифра равна", mn)