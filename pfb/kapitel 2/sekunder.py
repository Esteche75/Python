tid = int(input ('Ange tid i sekunder: '))
tim = tid // 3600
min = tid % 3600 // 60
sek = tid % 3600 % 60 
print (f'{tim},{min},{sek}')
