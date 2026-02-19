import math

while True:
    höjd = float(input('Ange höjd på bollen i meter: '))
    if höjd < 0:
        break
    studs = 0
    noll = 0.01
    while höjd > noll:
        höjd = höjd * 0.7
        studs += 1
    print(f'Bollen studsar {studs} gånger')
