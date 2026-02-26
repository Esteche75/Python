def nfak(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x

def ml(x, terms=10):
    s = 0
    for n in range(terms):
        s += (x ** n) / nfak(n)
    return s

e = int(input('Nu ska vi tydligen använda en Maclaurin-serie för att räkna ut värdet av : '))
u = int(input('Upphöjt med : '))
print(f'Det som kommer ut är tydligen : {ml(e, u):.2f}')