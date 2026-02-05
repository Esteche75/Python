tid = int(input('Hur många minuter ringer du i månaden? '))

if tid < 33:
    print('Använd Kontant.')
elif 33 <= tid <= 66:
    print('Använd Normal.')
else:
    print('Använd Plus')