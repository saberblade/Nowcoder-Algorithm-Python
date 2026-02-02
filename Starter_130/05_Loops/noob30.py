while True:
    line = input().split()
    if not line:
        break
    a,b = map(int, line)
    if a == 0 and b == 0:
        break
    print(a+b)