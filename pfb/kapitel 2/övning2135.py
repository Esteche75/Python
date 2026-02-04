import math

x1 = int(input('Ange x kordinat för första punkten: '))
y1 = int(input('Ange y kordinat för första punkten: '))
x2 = int(input('Ange x kordinat för andra punkten: '))
y2 = int(input('Ange y kordinat för andra punkten: '))
avstånd = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(f'avståndet mellan punkterna är {avstånd:.2f}')