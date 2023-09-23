from math import ceil

t = int(input())
for _ in range(t):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    # a,b,c = map(int, input().split())  haría lo mimso

    d = abs(a-b)  # diferencia entre los recipientes
    print( ceil(d/(c*2)) )  # para que redondee hacia arriba
