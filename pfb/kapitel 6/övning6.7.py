matrix = [
    [16, 9, 2, 7],
    [6, 3, 12, 13],
    [11, 14, 5, 4],
    [1, 8, 15, 10]
]
n = 4
mål = 34
magisk = True

for rad in matrix:
    if sum(rad) != mål:
        magisk = False

for kol in range(n):
    if sum(matrix[rad][kol] for rad in range(n)) != mål:
        magisk = False

if sum(matrix[i][i] for i in range(n)) != mål:
    magisk = False

if sum(matrix[i][n-1-i] for i in range(n)) != mål:
    magisk = False

if magisk:
    print('Kvadraten är magisk')
else:
    print('Kvadraten är inte magisk')


