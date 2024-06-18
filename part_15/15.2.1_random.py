import random

def ugadaika():
    num = random.randint(1, 100)
    flag = True
    while flag == True:
        ch = int(input())
        if ch > num:
            print("Слишком много, попробуйте еще раз")
            flag = True
        elif ch < num:
            print("Слишком мало, попробуйте еще раз")
            flag = True
        else:
            print('Вы угадали, поздравляем!')
            flag = False

ugadaika()