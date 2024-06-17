# объявление функции
def is_prime(num):
    for i in range(1, num + 1):
        if i == num or num != 1 or (i != num and num % i != 0):
            return True
        else:
            return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))