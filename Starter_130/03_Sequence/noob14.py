import math
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
d_E = math.sqrt((x2-x1)**2 + (y2-y1)**2)
d_M = abs(x2-x1) + abs(y2-y1)
delta = abs(d_M - d_E)
print(delta)