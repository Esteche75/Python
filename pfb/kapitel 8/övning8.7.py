def nfak(n):
    x = 1
    if n >= 1:
        for i in range(1, n+1):
            x *= i
    return x

def  bfak(n, k):
    if k > n or k < 0:
        return 0
    return nfak(n) // (nfak(k)* nfak(n -k))

print('Nu ska vi tydligen beräka binomialkoefficienter för värde n och k.')
n = int(input('Värde n: '))
k = int(input('Värde k: '))
bk = bfak(n, k)
print(f'Binomialkoefficenten för {n} och {k} är: {bk}')