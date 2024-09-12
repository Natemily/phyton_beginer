line = input()
size = len(line)
half = size // 2
if size % 2 == 0:
    print(line[half:]+line[:size-half])
else:
    print(line[half + 1:]+line[:size-half])
