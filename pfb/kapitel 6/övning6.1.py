list = []
while True:
    x = input('Skriv ett heltal som ska ingå i listan. Anvluta med ENTER: ')
    if x == '':
        break
    x = int(x)
    if not x in list:
        list.append(x)
print(list)