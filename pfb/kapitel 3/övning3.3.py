import math

a = float(input('Skriv längd på sida a: '))
b = float(input('Skriv längd på sida b: '))
vinkel = float(input('Skriv vinkel mellan sidorna (grader): '))

# konvertera till radianer
vinkel = math.radians(vinkel)

# cosinussatsen
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(vinkel))

eps = 1e-10

ab = abs(a - b) < eps
bc = abs(b - c) < eps
ac = abs(a - c) < eps

if ab and bc:
    print('Triangeln är liksidig')
elif ab or bc or ac:
    print('Triangeln är likbent')
else:
    print('Triangeln är oliksidig')



