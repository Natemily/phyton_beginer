cost = int(input())
sum = 0

while cost > 0:
    if cost >= 25:
        sum += 1
        cost -= 25
    elif cost >= 10:
        sum += 1
        cost -= 10
    elif cost >= 5:
        sum += 1
        cost -= 5
    elif cost >= 1:
        sum += 1
        cost -= 1

print(sum)