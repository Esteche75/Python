störst = 0
minst = 1.e300

while True:
    x = float(input('Tal: '))
    if x < 0:
        break
    if x > störst:
        störst = x
    elif x < minst:
        minst = x
print('Största tal = ', störst)
print('Minsta tal = ', minst)