ränta = float(input('Räntesats? '))
n = int(input('Antal år? '))
insättning = 12000
kapital = 0
for år in range(1, n+1, 1):
    kapital = (kapital + insättning) + (kapital * 0.01 * ränta)
    print(f'{år:3} {kapital:6.0f}')
    