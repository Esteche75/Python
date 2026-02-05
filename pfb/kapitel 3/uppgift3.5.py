längd = int(input('Ange längd på brevet: '))
bredd = int(input('Ange bredd på brevet: '))
tjock = int(input('Ange tjocklek på brevet: '))
if 140 <= längd <= 600 and bredd >= 90 and tjock <= 100 \
    and bredd+längd+tjock <=900:
    print('Brevet är ok.')
    
else:
    print('Brevet är inte tillåtet.')
    