  
    

'''
    Es 10: 3 punti
progettare la funzione es10(ftesto,k) che, presi in input 
l'indirizzo di un file di testo ed un intero k, restituisce una stringa di caratteri lunga k.
Il file di testo contiene stringhe di diversa lunghezza 
(una per riga ed ogni riga termina con '\n'), si guardi 
ad esempio il file f9.txt. 
I k caratteri della stringa restituita  dalla funzione si ottiengono
considerando le stringhe lunghe k presenti nel file di testo. 
L'i-mo carattere della stringa sara' il carattere che compare con maggior 
frequenza come i-mo carattere delle stringhe lunghe k nel file di testo (in caso 
di parita' di occorrenze viene scelto il carattere che precede 
gli altri lessicograficamente). 
Nel caso il file di testo non contenga parole lunghe k allora viene restituita 
la stringa vuota.  
Ad Esempio, per il file di testo f9.txt e k=3 la funzione restituisce  la stringa 'are' a 
seguito della presenza in f9.txt delle seguenti 4 stringhe lunghe 3:
tre
due
amo
ora 
'''
def es10(ftesto,k):
    rez = []
    with open(ftesto, mode='rt') as fr:
        for line in fr:
            if len(line.strip()) == k:
                rez.append(line.strip())
    
    if rez == []:
        return ''
    
    lfreq = []
    for i in range(k):
        dfreq = {}
        p = []
        for j in range(len(rez)):
            dfreq[rez[j][i]] = dfreq.get(rez[j][i], 0) + 1
        
        M = max(list(dfreq.values()))
        for k, v in dfreq.items():
            if v == M:
                p.append(k)
        
        lfreq.append(sorted(p, key=lambda x: x)[0])

            
        
    return ''.join(lfreq)
                
            
            

print(es10('ft9.txt', 3))