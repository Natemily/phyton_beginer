import sys

line = [s.strip() for s in sys.stdin]
max = max(line)
min = min(line)
print((ord(max[-1])*ord(min[-1]))**2)