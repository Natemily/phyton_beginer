nkml = int(input())
l = nkml % 10
m = (nkml % 100) // 10
k = (nkml % 1000) // 100
n = (nkml % 10**4 ) // 1000
if l + n == k - m:
    print('ДА')
else:
    print('НЕТ')