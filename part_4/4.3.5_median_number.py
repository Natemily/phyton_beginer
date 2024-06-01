n, k, l = int(input()), int(input()), int(input())
if n < k < l or n > k > l:
    print(k)
elif k < n < l or l < n < k:
    print(n)
elif n > l > k or n < l < k:
    print(l)