import math

radie = float(input('Vad är cirkelns radie i cm: '))
omkrets = 2 * math.pi * radie
area = math.pi * radie ** 2
if radie == 0:
    print('Felaktig inmatning')
else:
    print(f'Omkretsen är {omkrets:.2f} ca och arean är {area:.2f} kvadratcm')