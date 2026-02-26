matrix = []

print("Skriv en rad i taget (tal separerade med mellanslag).")
print("Tryck Enter på tom rad för att avsluta.")

while True:
    rad_input = input("Rad: ")
    if rad_input == "":
        break
    matrix.append([int(x) for x in rad_input.split()])

n = len(matrix)

# Kontrollera kvadratisk
if not all(len(rad) == n for rad in matrix):
    print("Matrisen är inte kvadratisk.")
else:
    sym = True
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                sym = False
                break

    if sym:
        print("Matrisen är symmetrisk")
    else:
        print("Matrisen är inte symmetrisk")
