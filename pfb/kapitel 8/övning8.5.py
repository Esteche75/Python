def rel_prim(a, b):
    minsta = min(a, b)

    for i in range(2, minsta + 1):
        if a % i == 0 and b % i == 0:
            return False

    return True

# Test
a = int(input('Det första talet: '))
b = int(input('Det andra talet:  '))
if rel_prim(a, b):
    print('Relativa primtal')
else:
    print('Inte relativa primtal')

