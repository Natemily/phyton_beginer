import random

print("Добро пожаловать в числовую угадайку")

num1 = random.randint(1, 100)

def is_valid(n):
    if n.isdigit() and int(n) in range(1, 100):
        return True
    else:
        return False

flag = True    

while flag == True:
    print("Напишите число от 1 до 100")
    num = input()
    if is_valid(num):
        num = int(num)
        if num < num1:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > num1:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif num == num1:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            flag = False
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
