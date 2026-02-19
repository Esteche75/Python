temp = []
medelvärde = float(0)
z = 0
while True:
    värde = input(f'Skriv in mätvärde i heltal för mätstation {len(temp)+1}: ')
    if värde == '':
        break
    värde = float(värde)
    temp.append(värde)
stationer = len(temp)
for x in temp:
    x = float(x)
    medelvärde += x
medelvärde /= stationer
print(f'Medeltemperaturen är: {medelvärde:.1f}')
for y in temp:
    z += 1
    if y > medelvärde:
        print(f'Mätstation {z} har uppmätt temperatur över medelvärde: {y:.1f}')





