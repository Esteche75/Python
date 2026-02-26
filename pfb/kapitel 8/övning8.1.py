def plusmoms(p, m):
    return p + (p*(m/100))

pris = float(input('Vad är inköpspriset på varan? '))
moms = float(input('Vad är momsen på? '))

brutto = float(plusmoms(pris, moms))
print(f'Varan kostar {brutto:.2f} kr för kund')
