import math

x = 1.0
y = 1
z = 0.00001
while True:
    print(x)
    f = 1/y
    a = 1/y+1
    x += 1/f - 1/a
    y += 1
    if abs(f) < z or abs(a) < z:
        break


    