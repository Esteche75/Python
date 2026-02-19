import random

ej = []
while len(ej) < 5:
    s = int(random.randint(1, 50))
    if not s in ej:
        ej.append(s)
while len(ej) < 7:
    s = int(random.randint(1, 12))
    if not s in ej:
        ej.append(s)
print(ej)        


