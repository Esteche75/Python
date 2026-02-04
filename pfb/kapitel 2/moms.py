pris = float (input('Vad är varans pris? '))
moms = float (input('Vilken är momssatsen? '))
total = float(pris + (pris * moms))
print(f'Priset på varan inklusive moms är {total:.2f}')
