n, sum, sum2 = int(input()), 0,  0

for i in range(1, n+1):
    if i == 1:
        print(1, end=' ')
        sum = i
    else:
        print(sum+sum2, end=' ')
        sum2, sum = sum, sum+sum2
       