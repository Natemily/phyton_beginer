x, y = int(input()), int(input())
w = input()
if w == '+' or w == '-' or w == '/' or w == '*':
    if w == '+':
        print(x+y)
    elif w == '-':
        print(x-y)
    elif w == '/' and y != 0:
        print(x/y)
    elif w == '/' and y == 0:
        print("На ноль делить нельзя!")
    else:
        print(x*y)
else:
    print('Неверная операция')