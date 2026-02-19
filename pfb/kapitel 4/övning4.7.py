domare = 0

while domare < 3:
    domare = int(input('Hur många domare deltar? '))
    if domare < 3:
        print('Det måste vara minst 3 domare.')

s = 0
while s <= 0:
    s = int(input('Hur svårt är hoppet? '))
    if s <= 0:
        print('Svårighetsgraden måste vara positiv.')

total = 0.0
högst = 0.0
minst = 1e10

for x in range(domare):
    poäng = float(input('Ange poäng domare gav: '))
    
    if poäng > högst:
        högst = poäng
    if poäng < minst:
        minst = poäng
        
    total += poäng

total = total - högst - minst
total = total / (domare - 2)
total *= 3
total *= s

print(f'Poäng för hoppet = {total:.2f}')

        
        

    

            


    
    
        





