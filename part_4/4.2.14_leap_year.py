ago = int(input())
if ago % 4 == 0 and ago % 100 != 0 or ago % 400 == 0:
    print("YES")
else:
    print('NO')