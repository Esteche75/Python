print('Bergdalens kommun hade 26 000 invånare år 2022')
år = int(input('Vilket år vill du beräkna framtida antal invånare?'))
invånare = 26000.0
födda = 0.07
döda = 0.06
inflyttade = 300.0
utflyttade = 325.0
x = år - 2022
for i in range(0,x):
    invånare *= 1.01 #födda - döda
    invånare -= 25.0 #inflyttade - utflyttade
print(f'Antal invånade år {år} = {invånare:.1f}.')


