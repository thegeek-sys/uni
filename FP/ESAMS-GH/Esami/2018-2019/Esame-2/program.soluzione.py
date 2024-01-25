################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################

'''
Es 1: punti 3.

Si progetti la funzione es1(lista1) che, prende in input 
una lista di interi con eventuali ripetizioni e restituisce una lista di interi in cui 
ogni elemento della lista di input compare esattamente una volta. Gli elementi di questa 
nuova lista devono risultare ordinati per numero di occorrenze decrescenti nella prima 
lista. In caso di pari occorrenze il numero di valore minore ha la precedenza.
Al termine della funzione la lista di input non deve risultare modificata.  

Ad Esempio, per 
lista1=[1,10,3,3,2,10,3,8,2,3] verra' restituita la lista [3,2,10,1,8].
'''
def es1(lista1):
    # inserisci qui il tuo codice
    d={}
    for x in lista1:
        if x in d:d[x]+=1
        else:d[x]=1
    lista2=[]
    for x in d: 
        lista2.append((-d[x],x))
    lista2.sort()
    return [x[1] for x in lista2]
        


################################################################################

'''
Es 2: punti 3.

Si progetti la funzione es2(lista) che prende in input una lista di stringhe di 
caratteri alfabetici che vanno da  'a' a 'z'. La funzione deve restituire una nuova lista. 
La nuova lista contiene lo stesso numero di stringhe della prima. Ciascuna stringa della 
nuova lista si ottiene a partire dalla corrispondente stringa della prima lista sostituendo 
con il simbolo '*' tutte le occorrenze 
del primo e dell'ultimo carattere in ordine lessicografico che vi compaiono.

Esempio: se la lista e': ['lucio', 'anna', 'federico', 'roberto']
la lista restituita sara' ['l**io','****','fede*i*o','ro*er*o']
'''

def es2(lista):
    # inserisci qui il tuo codice
    lista1=[]
    for x in lista:
        s=set(x)
        s1=sorted(s)
        a=x.replace(s1[0],'*')
        a=a.replace(s1[-1],'*')
        lista1.append(a)
    return lista1
        


#####################################################################################

'''
Es 3:  punti 4.   

Un file contiene un insieme di operazioni aritmetiche binarie (cioe' con due operandi) 
fra numeri interi, ciascuna posta su di una singola linea del file, e rappresentate 
con la usuale notazione operando1 op operando2 (con op appartenente all'insieme  {+,−,∗}). 
Tra gli operandi e l’operatore e' presente un numero arbitrario di spazi.
Un esempio di file corrispondente al formato descritto e' il seguente registrato in f3a.txt: 
  
3+5 
2-4 
-5 * 12 
3 +2

Progettare la funzione es3(ftesto1) che prende come parametro l' indirizzo 
del file di testo che contine le operazioni aritmetiche e restituisce una lista contenente 
nell'ordine il risultato intero di ciascuna delle operazioni aritmetiche. 

es3('f3a.txt') deve restituire  la lista [ 8, −2, −60, 5].
'''

def es3(ftesto1):
    lista=[]
    with open(ftesto1, encoding='utf8') as f:
        for riga in f:
            if riga[-1]=='\n': 
                riga=riga[:-1]
            if '+' in riga:
                riga1=riga.split('+')
                a=int(riga1[0])+int(riga1[1])
            elif '*' in riga:
                riga1=riga.split('*')
                a=int(riga1[0])*int(riga1[1])
            else:
                riga=riga.replace(' ','')
                riga1=riga.split('-')
                if riga1[0]=='': 
                    x=-int(riga1[1])
                    riga1=riga1[2:]
                else:
                    x=int(riga1[0])
                    riga1=riga1[1:]
                if riga1[0]=='': 
                    y=-int(riga1[1])
                else:
                    y=int(riga1[0])
                a=x-y
            lista.append(a)
    return lista




######################################################################################

import immagini

'''    
    Es 4: punti 4
    
    Abbiamo immagini che contengono su sfondo nero cammini di color bianco 
    che non si intrecciano ne' si toccano e sono formati da segmenti orizzontali 
    o verticali consecutivi.
    Si veda ad Esempio l'immagine f4a.png.
    Progettare la  funzione es4(fimm,w1,h1) che prende come parametri 
    l'indirizzo di un file .PNG siffatto e le coordinate (w1,h1) di un punto bianco 
    dell'immagine e restituisce un intero. 
    L'intero e' la lunghezza del segmento  rettilineo bianco su cui giace  il pixel 
    di coordinate (w1,h1). Nel caso in cui il pixel sia di giunzione 
    tra un segmento orizzontale ed un segmento verticale allora deve essere restituita 
    la lunghezza massima tra quella dei due segmenti.
    Ad esempio per il file f4.png:
    a) per il pixel (20,20) la funzione deve restituire 80
    a) per  il pixel (40,20) la funzione deve restituire 80
    b) per il pixel (60,40) deve restituire 61
    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''
    
def es4(fimm,w1,h1):
    img = immagini.load(fimm)
    lista=[]
    w,h=len(img[0]),len(img)
    if w1+1<w and  img[h1][w1+1]==(255,255,255):
            lista.append((1,0))
    if  h1+1<h  and img[h1+1][w1]==(255,255,255):
            lista.append((0,1))
    if  0<=w1-1 and img[h1][w1-1]==(255,255,255):
            lista.append((-1,0))
    if  0<=h1-1 and img[h1-1][w1]==(255,255,255):
            lista.append((0,-1))
    #print(lista)
    if len(lista)==1: 
        return conta(w1,h1,lista[0][0],lista[0][1], img)
    else:
        x,y=lista[0][0],lista[0][1]
        x1,y1=lista[1][0],lista[1][1]
        if x+x1==0 and y+y1==0:
            return conta(w1,h1,x,y, img) +conta(w1,h1,x1,y1, img)-1
        return max(conta(w1,h1,x,y, img) +conta(w1,h1,x1,y1, img))
            


def conta(x0,y0,x,y,img):
    #print('chiamo',x0,y0,x,y)
    tot=1
    while 0<=x0+x<len(img[0]) and 0<=y0+y<len(img) and img[y0+y][x0+x]==(255,255,255):
        x0+=x
        y0+=y
        tot+=1
        #print(x0,y0)
    return tot

############################################################################

import albero

'''
    Es 5: punti 6
    
    Dato un nodo di un albero, il grado del nodo e' il numero di figli che il nodo ha.

    Si definisca la funzione es5(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata e 
    torna come risultato un dizionario.
    Chiavi del dizionario sono i gradi dei nodi presenti nell'albero 
    e associato ad ogni chiave c'e' l'insieme di nodi dell'albero che hanno quella chiave.

    Esempio:  la funzione es5
    - sull'albero a sinistra restituisce  {0: {1, 2, 3, 4}, 2: {10, 3, 7}}
    - sull'albero a destra restituisce {0: {1, 2, 3, 4, 5, 6, 7, 8}, 2: {3, 26, 36, 7, 10, 11, 15}} .


                    10                                  36               
             _______|______                      _______|______         
            |              |                    |              |        
            3              7                   10             26        
         ___|___        ___|__               ___|___        ___|__      
        |       |      |      |             |       |      |      |     
        1       2      3      4             3       7     11     15     
                                           _|_     _|_    _|_    _|_    
                                          |   |   |   |  |   |  |   |   
                                          1   2   3   4  5   6  7   8   
                                                                   
    '''

def es5(tree):
    # inserisci qui il tuo codice
    d={}
    for x in tree.f:
        d1=es5(x)
        for x in d1:
            if x in d: 
                d[x]=d[x] | d1[x]
            else:
                d[x]=d1[x]
    y=len(tree.f)
    if y in d:
        d[y]=d[y]|  {tree.id}
    else: d[y]=  {tree.id}        
    return d 


###########################################################################

import os

'''
    Es 6: 6 punti


    Si definisca la funzione es6(pathDir, carname ) ricorsiva (o che fa uso di 
    funzioni o metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella ed il nome di una seconda cartella
    - cerca una occorrenza della seconda cartella   all'interno della cartella di partenza e 
      delle sottocartelle raggiungibili da questa. Se la cartella cercata  
      non viene trovata la funzione restituisce una stringa vuota, 
      in caso contrario restituisce la stringa con l'indirizzo 
      dell'occorrenza della seconda cartella.
      Nell'esplorazione delle sottocartelle quelle il cui nome comincia  col carattere '.' 
      non vanno considerate. 

      NOTA: È VIETATO USARE LA FUNZIONE DI LIBRERIA os.walk
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempi: 
    con es6('Informatica', 'RISC') la stringa restituita e' 'Informatica/Hardware/Architetture/Processori/RISC'
    con es6('Informatica', 'Basi') la stringa restituita e' ''
    con es6('Informatica/Software','ManualeMac') la stringa restituita e' 
    'Informatica/Software/SistemiOperativi/OSX/ManualeMac'

'''

def es6(pathDir,carname):
    # inserisci qui il tuo codice
    for x in os.listdir(pathDir):
        if x[0]=='.': 
            continue
        path1=pathDir + '/' + x
        if os.path.isfile(path1):
            continue
        if os.path.isdir(path1):
            if x==carname: return path1
            stringa=es6(path1,carname)
            if stringa: return stringa
    return ''

###########################################################################

'''
    Es. 7: punti 6

   Sia dato un albero realizzato da nodi della classe Nodo della libreria albero.py
   Si scriva la funzione es7(albero) che, facendo uso di funzioni ricorsive, e ricevendo un albero, 
   lo modifica distruttivamente in modo che
   - considerando la radice come il livello 0 dell'albero
   - tutti i nodi che si trovano in livelli dispari abbiano i loro sottoalberi ruotati di un posto a destra
   - tutti i nodi che si trovano in livelli pari o che hanno meno di 2 figli, invece restano invariati
   La funzione ritorna il numero di nodi che sono stati modificati.

    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate il test di ricorsione

    Esempio:

            1                0                   1                                           |
        /       \                            /       \                                       |
       2         3           1              2         3                                      |
    /  |  \      |                       /  |  \      |                                      |
   4   5   6     7           2          6   4   5     7                                      |
  / \  |       / |  \                      / \  |   / | \                                    |
 8  9  10    11  12  13      3            8   9 10 11 12 13                                  |

In questo caso la funzione ritorna il valore 1 (solo il nodo 2 ha avuto l'ordine dei figli modificato)

'''

def es7(tree):
    return ruota(tree, 0)

def ruota(tree, level):
    N = 0
    if len(tree.f) > 1 and level%2:
        tree.f = tree.f[1:] + tree.f[:1]
        N = 1

    for son in tree.f:
        N += ruota(son, level+1)
    return N

