def is_prime(x):
    if x < 2:
        return False

    for k in range(2, x):
        if x % k == 0:
            return False

    return True
        
talet = int(input('Ange att tal: '))
prim = bool(is_prime(talet))
if prim == True:
    print(f'{talet} är ett primtal.')
else:
    print(f'{talet} är inte ett primtal.')


