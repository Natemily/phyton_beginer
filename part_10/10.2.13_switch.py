line = input()
first = line.find('h')
last = line.rfind('h')
new = line[:first+1]+line[last-1:first:-1]+line[last:]
print(new)