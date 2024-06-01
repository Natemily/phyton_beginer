n, k, l = int(input()), int(input()), int(input())
if n == k == l:
    print("Равносторонний")
elif n == k or n == l or k == l:
    print('Равнобедренный')
else:
    print('Разносторонний')