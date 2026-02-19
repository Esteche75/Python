v = int(input('Ange högsta multiplikation: '))
a = []

for i in range(0, v):
    a.append([])
    for j in range(0, v):
        value = (i+1) * (j+1)
        a[i].append(value)
        print(f'{value:4}', end=' ')
    print()