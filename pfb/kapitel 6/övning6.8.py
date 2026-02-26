resultat = []
namn = []
total = 0

while True:
    x = input('Elevens namn: ')
    if x == '':
        break

    namn.append(x)

    rad = input('Provresultat 5st (mellanslag mellan): ')
    poäng = [int(y) for y in rad.split()]

    resultat.append(poäng)

# Summering
for i in range(len(resultat)):
    summa = sum(resultat[i])
    total += summa
    print(namn[i], resultat[i], summa)

medel = total / len(resultat)
print(f'Medelvärde: {medel:.2f}')
    