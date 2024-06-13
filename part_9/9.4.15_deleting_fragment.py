line = input()
first = line.find("h")
last = line.rfind("h")
print(line[:first]+line[last + 1:])