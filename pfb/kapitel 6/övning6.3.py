lista = []
temp = []

while True:
    värde = input('Skriv in värde för lista. Tryck ENTER när du är klar med inmatning. ')
    if värde == '':
        break
    lista.append(värde)

while True:
    värde = input('Skriv in värde för tuple. Tryck ENTER när du är klar med inmatning. ')
    if värde == '':
        break
    temp.append(värde)

tlist = tuple(temp)
lika = True


if len(lista) != len(tlist):
    print('Listorna är inte lika långa.')
    lika = False
    
for i in range(len(lista)):
    if lista[i] != tlist[i]:
        print('Listorna innehåller inte samma värde')
        lika = False
        break

if lika:
    print('Listorna är lika långa och har samma värde')


    