lista = []
print('Skriv in värde. Avsluta med ENTER.')

while True:

    värde = input('Värde: ')
    if värde == '':
        break
    lista.append(värde)

lista.sort()
n = len(lista)
if n % 2 == 1:
    median = lista[n // 2]
else:
    mitten1 = int(lista[n // 2 -1])
    mitten2 = int(lista[n // 2])
    median = (mitten1 + mitten2) / 2

print(f'Medianen är : {median}')

