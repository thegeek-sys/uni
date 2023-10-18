




'''
    Homework 1 - opzionale

    Abbiamo una stringa S contenente una sequenza di interi non-negativi separati da virgole 
    ed un intero positivo m.  

    Progettare una funzione es1(S,m) che prende in input  la stringa S e l'intero m e 
    restituisce il numero di sottostringhe di S la somma dei cui valori e' m.
    
    Ad esempio, per S='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e m=9 la funzione deve restituire 7.
    
    Infatti:
    '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
     _'0,4,0,3,1,0,1,0'_____________
     _'0,4,0,3,1,0,1'_______________
     ___'4,0,3,1,0,1,0'_____________
    ____'4,0,3,1,0,1'_______________
    ____________________'0,0,5,0,4'_
    ______________________'0,5,0,4'_
     _______________________'5,0,4'_
    
    NOTA: il timeout previsto per questo esercizio è di 8 secondi per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)
'''

def ex1(S,m):
    "se un valore supera m posso spezzare la ricerca in due parti e buttare quel valore"
    numeri = list(map(int, S.split(",")))
    last   = 0
    somma  = 0
    N      = len(numeri)
    for i in range(N):
        if numeri[i] > m:
            somma += sottosoluzione(numeri[last:i], m, last)
            last = i+1
    if last < N:
        somma += sottosoluzione(numeri[last:], m, last)
    return somma

def sottosoluzione(numeri, m, offset):
    #print(f"sottosoluzione {offset} {offset+len(numeri)}")
    def minore():
        nonlocal i,j,compattati, somma, quante
        #print(f"i={i+offset} j={j+offset} somma={somma}<{m} quante={quante}")
        # aggiungo un valore positivo a destra
        j += 1
        if j<N:
            x = compattati[j]
            if x < 0:
                j += 1
                if j<N:
                    x = compattati[j]
                    somma += x
            else:
                somma += x
    def maggiore():
        nonlocal i,j,compattati, somma, quante
        #print(f"i={i+offset} j={j+offset} somma={somma}>{m} quante={quante}")
        # sottraggo il valore a sinistra e mi sposto al prox positivo
        x = compattati[i]
        somma -= x
        i += 1
        if i<N and compattati[i]<0:
            i += 1
    def uguale():
        nonlocal i,j,compattati, somma, quante
        #print(f"i={i+offset} j={j+offset} somma={somma}=={m} quante={quante}")
        # la somma vale 1
        addendo = 1
        # ma se seguita/preceduta da un valore negativo 
        if j < N - 1 and compattati[j + 1] < 0:
            addendo *= 1 - compattati[j+1]
        if i > 0 and compattati[i - 1] < 0:
            addendo *= 1 - compattati[i-1]
        quante += addendo
        # tolgo solo l'elemento a sinistra
        somma -= compattati[i]
        i += 1
        if i<N and compattati[i]<0:
            i += 1            
        # aggiungo quello a destra
        j += 1
        if j<N:
            x = compattati[j]
            if x < 0:
                j += 1
                if j<N:
                    x = compattati[j]
                    #assert x>0, "non ci possono essere due negativi in sequenza"
                    somma += x
            else:
                somma += x
    compattati = compatta(numeri, m)
    #print(compattati)
    N = len(compattati)
    if N == 0:
        return 0
    if N == 1:
        if compattati[0] == m:
            return 1
        else:
            return 0
    quante = 0
    if compattati[0] < 0:
        i = j = 1
    else:
        i = j = 0
    somma = compattati[i]
    while i < N and j < N:
        # invarianti: i e j indicano valori positivi
        #assert compattati[i]>0, f"valore negativo ({compattati[i]}) per i={i}" 
        #assert compattati[j]>0, f"valore negativo ({compattati[j]}) per j={j}"
        if somma < m:
            minore()
        elif somma > m:
            maggiore()
        else: # somma == m
            uguale()
    return quante


def compatta(numeri, m):
    """compatto le sottosequenze di k zeri e le sostituisco con -k"""
    compattati = []
    zeri = 0
    for x in numeri:
        if x:
            if zeri:
                compattati.append(-zeri)
                zeri = 0
            compattati.append(x)
        else:
            zeri +=1
    if zeri:
        compattati.append(-zeri)
    return compattati

def scompatta(compattati):
    scompattati = []
    for x in compattati:
        if x<0:
            scompattati.extend([0]*(-x))
        else:
            scompattati.append(x)
    return scompattati
