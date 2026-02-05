#Ett program som beräknar konstad för att ringa mobiltelefon

min = float(input('Hur många minuter ringer du i månaden? '))
avgift = float(input('Vad är minutkostnaden? '))
pris = min * avgift

if pris > 300:
    pris = pris * 0.9

print(f'Den totala kostnaden blir {pris:.2f}')