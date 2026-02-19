lista = []
tupel_temp = []

print("Mata in värden till listan (ENTER för att avsluta):")

while True:
    värde = input("Värde: ")
    if värde == "":
        break
    lista.append(värde)

print("\nMata in värden till tupeln (ENTER för att avsluta):")

while True:
    värde = input("Värde: ")
    if värde == "":
        break
    tupel_temp.append(värde)

tupel = tuple(tupel_temp)

# Jämförelse
lika = True

if len(lista) != len(tupel):
    lika = False
else:
    for i in range(len(lista)):
        if lista[i] != tupel[i]:
            lika = False
            break

if lika:
    print("\nListan och tupeln är lika.")
else:
    print("\nListan och tupeln är inte lika.")