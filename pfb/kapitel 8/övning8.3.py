#Övning8.3 = "Skriv en funktion som undersöker hur många små resp. stora bokstäver som finns i en text. Resultatet ska ges i en tuple."del

#Funkionen

#Läser in text
def stor_liten(x):
    stor = 0
    liten = 0
# tar bort mellanslag
#    t = "".join(x.split()) #Kanske inte behövs när vi ändå kör .isalpha()?
#Går igenom texten bokstav för bokstav och kollar om det är stor bokstav
    for i in x:
#Om det är en stor bokstav så + 1 till stor
        if i.isupper(): #tog bort and i.isalpha(). Det behövdes inte. Det kontrollerar .isupper()
            stor += 1
#Om inte + 1 till liten
        elif i.islower(): #tog bort and i.isalpha(). Det behövdes inte. Det kontrollerar .islower()
            liten += 1 
#När hela texten har bearbetats sparas både stor och liten till en tuple
#Returnera tuple
    return (stor, liten)
text = str('Hej baberiba. Korv ÄR GOTT.')
tlist = stor_liten(text)
print(f'Det finns {tlist[0]} stora bokstäver och {tlist[1]} små bokstäver i texten')


