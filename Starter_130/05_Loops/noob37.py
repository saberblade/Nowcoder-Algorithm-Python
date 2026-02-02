n = int(input())
n = abs(n)
s = str(n)
total = 0
for char in s:
    total += int(char)
print(total)