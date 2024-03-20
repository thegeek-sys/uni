
def es45(parola1,parola2):
    '''
    progettare la funzione es45(parola1,parola2) che
    prende in input due  stringhe di caratteri parola1 e parola2, e restituisce 
    la lista delle sottostringhe che risultano in comune ad entrambe le parole.
    La lista delle sottostringhe comuni deve essere ordinata 
    lessicograficamente e non deve contenere duplicati.
    Si ricorda che una sottostringa e' quello che si ottiene da una stringa
    eliminando 0 o piu' caratteri all'inizio e 0 o piu' caratteri alla fine

    Ad esempio:
    con  parola1='aabbccdd' parola2='acccdzza' la funzione restituisce la lista [a,c,cc,ccd,cd,d]
    '''

    parola1, parola2 = sorted([parola1, parola2], key=len)
    rez = []
    for i in range(len(parola1)):
        for j in range(i+1, len(parola1)):
            if parola1[i:j] in parola2 and parola1[i:j] not in rez:
                rez.append(parola1[i:j])
    return sorted(rez)

print(es45('aabbccdd', 'acccdzza'))