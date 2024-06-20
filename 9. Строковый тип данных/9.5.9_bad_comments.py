n = int(input())
for i in range(1, n + 1):
    line = input()
    if line.isspace() or line == "":
        line = "COMMENT SHOULD BE DELETED"
    print(str(i)+": "+line)