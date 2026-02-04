import math

radie = float(input('Vad är sfärens radie i cm? '))
volym = ((4 * math.pi * radie) ** 3) / 3
area = (4 * radie * math.pi) ** 2
print(f'Volymen på sfären är {volym:.2f} kubikcm och arean är {area:.2f} kvadratcm.')