def nfak(n):
    x = 1
    if n >= 1:
        for i in range(1, n+1):
            x *= i
    return x
        
fak = int(input('Vilket heltal vill du räkna ut fakulteten på? '))
print(f'Fakulteten på {fak} är {nfak(fak)}.')
