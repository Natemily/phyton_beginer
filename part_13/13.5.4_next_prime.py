def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num != 1 and num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def get_next_prime(num):
    k, a = num + 1, 0
    for i in range(k, k + 1000):
        if is_prime(i):
            a = i
            break
    return a


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
