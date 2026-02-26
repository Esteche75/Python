lista = ['banan', 'gurka', 'tomat', 'apelsin']

def rotera(x):
    z = x.pop()
    x.insert(0, z)
    return x

print(lista)
lista = rotera(lista)
print(lista)


