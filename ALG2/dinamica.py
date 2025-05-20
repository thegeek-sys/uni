'''
Si consideri una sequenza di interi X. La cancellazione da X di un certo numero
di elementi determina una sottosequenza. La sottosequenza `e crescente se il
valore dei suoi elementi `e crescente. La lunghezza della sottosequenza `e il numero
di elementi che la compongono. Il valore della sottosequenza `e dato dalla somma
dei valori degli elementi che la compongono.
Data la sequenza X = (x1, x2,...xn) a valori distinti si considerino i seguenti
tre problemi:
a. Trovare la sottosequenza crescente di X di lunghezza massima.
'''
def es1(X):
    T=[1]*len(X)
    for i in range(len(X)):
        for j in range(i):
            if X[j]<X[i]:
                T[i]=max(T[j]+1,T[i])

    return T


X=[50,4,100,2,48,3,1,34,30]
#print(es1(X))

'''
Data una matrice n ⇥ m di interi M = [mi,j ], una M -lista `e una sequenza
(m1,j1 , m2,j2 . . . mn,jm ) tale che 1  j1  . . . jm  m. Il valore di una M -lista `e
la somma degli elementi che la compongono.
Progettare un algoritmo che trova un M -lista di valore minimo in O(n · m).
'''
def es2(M):
    T=[[0]*len(M[0]) for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i==0:
                T[i][j]=M[i][j]
            else:
                T[i][j]=min(T[i-1][:j+1])+M[i][j]

    print(T)
    m=min(T[-1])
    k=T[-1].index(m)
    seq = [M[-1][k]]

    for i in range(len(T)-2,-1,-1):
        seq.append(min(M[i][:k+1]))
        k=M[i].index(seq[-1])
    return seq[::-1]


M=[[3,-1,5,2,-4],[0,2,-3,1,6],[-2,4,1,-5,0],[1,-6,2,3,-2]]
#print(es2(M))

'''
Dato un insieme di m stringhe binarie dette primitive ed una stringa di n bit X,
vogliamo sapere se la stringa X si può ottenere dalla concatenazione di stringhe
primitive.
Ad esempio: dato l’insieme di primitive {01, 10, 011, 101}, per la stringa X =
0111010101 la risposta è si (due possibili soluzioni sono 011  10  10  101 e
011  101  01  01) mentre per la stringa X = 0110001 la risposta è no.
a) Descrivere un algoritmo che, data la stringa X e le m primitive, risolve il
problema in O((m + n) · l) dove l è la lunghezza massima per le stringhe
primitive.
b) Modificare l’algoritmo proposto in modo che, nel caso X sia ottenibile
dalla concatenazione di primitive, vengano prodotti in output gli indici
delle primitive la cui concatenazione genera X.
Ad esempio: data la stringa X = 0111010101 e le primitive Y1 = 01, Y2 =
10, Y3 = 011 e Y4 = 101, l’algoritmo deve produrre in output la sequenza
3, 2, 2, 4 o la sequenza 3, 4, 1, 1
'''
def es3(X,A):
    T=[False]*len(X)
    T[0]=True
    l=max(len(x) for x in A)
    for i in range(len(T)):
        for j in range(max(0, i-l-1),i+1):
            if j>0:
                if T[j-1] and X[j:i+1] in A:
                    T[i]=True
                    break
            else:
                if T[0] and X[j:i+1] in A:
                    T[i]=True
                    break
    print(T)
    if T[-1]==False:
        return T[-1]

    s=[]
    f=-1
    k=len(T)-1
    while k>=0:
        for p in range(k,max(0,k-l)-1,-1):
            if p==0:
                if T[p] and X[p:k+1] in A:
                    f=-(k-p)
                    s.append(A.index(X[p:k+1]))
                    break
            else:
                if T[p-1] and X[p:k+1] in A:
                    f=-(k-p)-1
                    s.append(A.index(X[p:k+1]))
                    break
        k+=f
    s.reverse()
    return s

def es3_1(X,S):
    T=[0]*len(X)
    l=max(len(x) for x in S)
    for i in range(len(T)):
        if i<=l and X[:i+1] in S:
            T[i]=1
        elif i>l:
            for k in range(l):
                if X[i-k:i+1] in S and T[i-k-1]==1:
                    T[i]=1
                    break
    print(T)
    return T[-1]

X="0111010101"
A=["01", "10", "011", "101"]
print(es3_1(X,A))

'''
kermit sta cercando di attraversare un fiume
il cui percorso da una sponda all’altra `e descritto da n quadranti posiziona-
ti uno accanto all’altro. Ogni quadrante pu`o corrispondere ad una pietra,
rappresentata da un 1, oppure una zona d’acqua, rappresentata da uno 0.
Per poter attraversare, Kermit deve saltare da una pietra all’altra, senza mai
toccare una zona d’acqua, rispettando i seguenti vincoli:
• Quando Kermit effettua un salto di k quadranti, il salto successivo potr`a
essere solo di k − 1, k o k + 1 quadranti.
• Il primo salto dalla sponda iniziale al primo quadrante sar`a sempre
di ampiezza 1 (assumiamo quindi che il primo e l’ultimo quadrante
contengano sempre una pietra).
• Non `e possibile tornare su una pietra posizionata prima della pietra
attuale
Dato in input un array Q descrivente i quadranti del fiume:
1. Progettare un algoritmo che in O(n2) restituisca True se Kermit possa
raggiungere l’ultima pietra partendo dalla prima e False altrimenti
'''
def es4(Q):
    T=[[False]*len(Q) for _ in range(len(Q))]
    # T[i][j] se i è raggiungibile in j passi
    for i in range(len(Q)):
        for j in range(len(Q)):
            if j==0:
                T[i][j]=False
            elif j==1 and i==0:
                T[i][j]=True
            elif i==0:
                T[i][j]=False
            elif Q[i]==0:
                T[i][j]=False
            else:
                k = max(0, i-j)
                T[i][j] = T[k][j] or T[k][min(j+1, len(Q)-1)] or T[k][j-1]
    #print(T)
    for i in range(len(Q)):
        if T[-1][i]==True:
            return True, T
    return False, T

def es4_1(Q):
    f,T=es4(Q)
    if f==False:
        return False
    k=len(Q)-1
    p=T[-1].index(True)
    print(p)
    seq=[]
    while k>0:
        seq.append(p)
        k-=p
        for i in range(-1,2):
            if T[k][p+i]:
                p+=i
                break
    seq.append(1)
    return seq[::-1]

Q=[1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,1] # true
#Q=[1,1,1,1,0,0,0,1,1,0,1] # false
#print(es4_1(Q))

'''
Data una matrice di dimensione n×n le cui celle sono numerate con numeri
distinti che vanno da 1 a n2, vogliamo trovare la massima lunghezza possibile
per cammini che toccano celle con numerazione crescente e incremento di 1.
I cammini possono partire da una qualunque cella e, nel corso del cammino, dalla
generica cella (i, j) ci si pu`o spostare in una qualunque cella adiacente in orizzon-
tale o verticale (vale a dire in una delle celle (i, j +1), (i+1, j), (i, j 1), (i1, j)).
La lunghezza di un cammino `e data dal numero di nodi toccati dal cammino.
Progettare un algoritmo che risolve il problema in tempo O(n^2)
'''
def es5(M):
    n=len(M)
    pos=[[] for _ in range(n*n+1)]
    for i in range(n):
        for j in range(n):
            pos[M[i][j]]=[i,j]

    T=[[1]*len(M) for _ in range(len(M))]
    # T[i][j]=lunghezza massima fino alla casella M[i][j]

    for k in range(2,n*n):
        i,j=pos[k]
        if pos[k+1][0]==(i+1) and pos[k+1][1]==j:
            T[i+1][j]=T[i][j]+1
        elif pos[k+1][0]==(i-1) and pos[k+1][1]==j:
            T[i-1][j]=T[i][j]+1
        elif pos[k+1][1]==(j+1) and pos[k+1][0]==i:
            T[i][j+1]=T[i][j]+1
        elif pos[k+1][1]==(j-1) and pos[k+1][0]==i:
            T[i][j-1]=T[i][j]+1
    m=0
    print(T)
    for i in range(len(T)):
        for j in range(len(T)):
            m=max(m, T[i][j])
    return m

A=[[3,6,2],[7,1,9],[4,8,5]]
B=[[9,7,6],[8,2,5],[1,3,4]]
#print(es5(B))

'''
Data una sequenza di n interi positivi X e un intero positivo s vogliamo trovare
la pi`u lunga sottosequenza di X di somma s.
Ad esempio se X = (5, 2, 2, 6, 1, 7, 3, 5, 11, 3, 6) e s = 25, la pi`u lunga sottose-
quenza `e lunga 7 (5, 2, 2, , 1, 7, 3, 5, , , ); se X = (3, 3, 5, 13, 3, 5) e s = 28, non ci
sono sottosequenze di somma 28.
• Dare lo pseudo-codice di un algoritmo che dati X e s ritorna la lunghezza
massima di una sottosequenza di somma s di X in tempo O(ns) (se non
ci sono sottosequenze di somma s, ritorna 0).
• Dare poi lo pseudo-codice di un algoritmo che ritorna una sottosequenza
di lunghezza massima per X e s.
'''
def es6(X, s):
    T=[[0]*(s+1) for _ in range(len(X))]
    # T[i][j]=lunghezza massima della sottosequenza che termina in i la cui somma è j
    T[0][X[0]]=1
    for i in range(1, len(T)):
        for j in range(len(T[0])):
            if T[i-1][max(0, j-X[i])] != 0:
                T[i][j]=max(T[i-1][j], T[i-1][j-X[i]]+1)
            elif j==X[i]:
                T[i][j]=1
            elif T[i-1][j]!=0:
                T[i][j]=T[i-1][j]
    for x in T:
        print(x)
    return T[-1][-1]

def es6_1(X,s):
    T=[[0]*(s+1) for _ in range(len(X))]
    T[0][X[0]]=1
    for i in range(1, len(T)):
        for j in range(len(T[0])):
            if j==X[i]:
                T[i][j]=max(T[i-1][j],1)
            elif j>=X[i] and T[i-1][j-X[i]]!=0:
                T[i][j]=max(T[i-1][j-X[i]]+1, T[i-1][j])
            else:
                T[i][j]=T[i-1][j]

    for x in T:
        print(x)
    return T[-1][-1]


X=[5,2,2,6,1,7,3,5,11,3,6]
#print(es6(X,25))
print(es6_1(X,25))

'''
Abbiamo una sequenza S = (s1, s2, . . . , sn) di interi positivi.
Una sottosequenza S0 di S si definisce valida se per ogni coppia di elementi
consecutivi di S almeno un elemento della coppia compare in S0.
Il valore di una sottosequenza valida `e la somma dei suoi elementi.
Ad esempio: per S = (1, 2, 3, 5, 4, 6, 7), la sottosequenza S0 = (1, 3, 6) non `e
valida, mentre la sottosequenza S0 = (2, 5, 4, 7) `e valida ed ha valore valore 18 e
la sottosequenza S00 = (2, 3, 4, 6) `e valida ed ha valore 15.
• Descrivere un algoritmo che, data la sequenza S, calcola il valore minimo
di una sottosequenza valida in tempo O(n).
• Descrivere poi un algoritmo che trova una sottosequenza valida di valore
minimo.
'''
def es7(S):
    T=[0]*len(S)
    # T[i]=valore minmo della sottosequenza valida
    k=0
    i=0
    while i<len(S)-1:
        if S[i]<S[i+1]:
            k=i
        else:
            k=i+1

        if i-k<2:
            T[i]=min(S[i], S[i+1])
            i+=1
        elif i+2<len(S)-1:
            T[i-1]=min(S[i-1], S[i])
            i+=2

    print(T)

def es7_1(S):
    T=[0]*len(S)
    T[0]=S[0]
    T[1]=S[1]
    t=1
    for i in range(2,len(T)):
        if i-t>=2:
            t=i
            T[i]=min(T[i-2]+S[i], T[i-1]+S[i])
        else:
            if T[i-2]+S[i]<=T[i-1] or T[i-1]+S[i]<=T[i-1]:
                t=i
                T[i]=min(T[i-2]+S[i], T[i-1]+S[i])

            else:
                T[i]=T[i-1]
    print(T)
    return(T[-1])

S=(1,2,3,5,4,6,7)
print(es7(S))
print(es7_1(S))

'''
Dati in input i tre numeri
interi positivi x1, x2, x3 e un numero n, progettare un algoritmo di costo O(n)
che trovi il numero di sequenze
'''
def es8(x,y,z,n):
    A=[x,y,z]
    T=[0]*(n+1)
    T[0]=1
    for i in range(n+1):
        for x in A:
            if i-x>=0:
                T[i]+=T[i-x]
    return T[n]

#print(es8(2,4,8,10))


'''
Il Fantastico Mr. Fox è un ladro
professionista e sta progettando un grande furto in una nota strada in cui si
trovano n case adiacenti tra loro, poste in linea retta. Ogni casa del quartiere
ha una certa quantit`a mi di soldi al suo interno. Inoltre, ciascuna di esse `e
dotata di un sistema di sicurezza che contatter`a automaticamente la polizia se
sia essa che una delle case ad essere adiacenti vengono derubate. Ad esempio,
se la casa 4 e la casa 5 venissero derubate verrebbe allertato il sistema, mentre
ci`o non accadrebbe se venissero derubate le case 3 e 5.

Progettare un algoritmo che dato in input l’insieme m1, . . . , mn di soldi al-
l’interno delle case restituisca la quantit`a massima di soldi che Mr. Fox pu`o

rubare in una sola notte
'''
def es9(m):
    T=[0]*len(m)
    T[0]=m[0]
    T[1]=max(m[0],m[1])

    for i in range(2, len(m)):
        T[i]=max(T[i-1], T[i-2]+m[i])

    print(T)
    return T[-1]

m=[30,20,10,1,2,40,35]
#print(es9(m))

'''
Dato un intero n, con n ≥ 2, vogliamo contare il numero
di modi in cui e possibile ottenere n partendo dal numero 2 e potendo effettuare
le sole 3 operazioni di incremento di 1, prodotto per 2 e prodotto per 3.
'''
def es10(n):
    T=[0]*(n+1)
    T[2]=1
    T[3]=1
    for i in range(4,n+1):
        T[i]=T[i-1]
        if i%2==0:
            T[i]+=T[i//2]
        if i%3==0:
            T[i]+=T[i//3]
    print(T)
    return T[-1]

#print(es10(10))

'''
Data una sequenza S crescente di n interi, vogliamo trovare la lunghezza massima per le 
sottosequenze di S dove ciascun elemento è divisore del successivo. 
'''
def es11(S):
    T=[0]*len(S)
    T[0]=1
    for i in range(1,len(S)):
        k=0
        for j in range(i+1):
            if S[i]%S[j]==0:
                k+=1
        T[i]=max(T[i-1],k)
    print(T)
    return T[-1]

S=[3,5,10,6,18,36,40]
#print(es11(S))

'''
Data una sequenza S di n cifre decimali, vogliamo calcolare la lunghezza massima per  una sottosequenza non decrescente che contiene i tre simboli 0, 1 e 2
'''
def es12(S):
    T=[[0]*len(S) for _ in range(0,3)]
    # T[i][j]=lunghezza massima per una sottoseq non decr che termina con il simbolo i in pos fino a j
    if S[0]==0:
        T[0][0]=1
    for i in range(len(T)):
        for j in range(1,len(S)):
            if i==0 and S[j]==i:
                T[i][j]=T[i][j-1]+1
            elif S[j]==i:
                T[i][j]=max(T[i-1][j]+1,T[i][j-1]+1)
            else:
                T[i][j]=T[i][j-1]
    for x in T:
        print(x)
    return T[-1][-1]

S=[0,1,2,5,6,1,4,1,2,2,2,1,5,2]
#print(es12(S))

'''
Il display di un telefonino si presenta come di seguito indicato:123456789⇤0#Cerchiamo un particolare numero telefonico e sappiamo che:•il numero `e composto dancifre.•non contiene cifre uguali adiacenti•nel comporre il numero sul tastierino basta spostarsi solo tra tasti adiacentiin orizzontale o verticaleAd esempio, pern= 7, la combinazione 12108586996 non `e di certo il numerotelefonico che cerchiamo a causa della presenza delle seguenti tre coppie di cifreadiacenti 10 e 86 e 99.Progettare un algoritmo che, daton, restituisce il numero di combinazioni pos-sibili per il numero telefonico da ricercare.
'''
def es13(n):
    T=[[0]*10 for _ in range(n+1)]
    for i in range(10):
        T[1][i]=1

    for i in range(2, n+1):
        for j in range(10):
            if j==0:
                T[i][j]=T[i-1][8]
            elif j==1:
                T[i][j]=T[i-1][2]+T[i-1][4]
            elif j==2:
                T[i][j]=T[i-1][1]+T[i-1][3]+T[i-1][5]
            elif j==3:
                T[i][j]=T[i-1][2]+T[i-1][6]
            elif j==4:
                T[i][j]=T[i-1][1]+T[i-1][5]+T[i-1][7]
            elif j==5:
                T[i][j]=T[i-1][2]+T[i-1][4]+T[i-1][6]+T[i-1][8]
            elif j==6:
                T[i][j]=T[i-1][3]+T[i-1][5]+T[i-1][9]
            elif j==7:
                T[i][j]=T[i-1][4]+T[i-1][8]
            elif j==8:
                T[i][j]=T[i-1][5]+T[i-1][7]+T[i-1][9]+T[i-1][0]
            elif j==9:
                T[i][j]=T[i-1][6]+T[i-1][8]
    for x in T:
        print(x)
    return sum(T[-1])

#print(es13(3))

'''
Abbiamo una matrice M di interi di dimensione n×n con n>1. Una discesa su questa matrice `e una sequenza
di n celle della matrice con i seguenti vincoli
•le celle appartengono a righe diverse della matrice
•la prima cella appartiene alla prima riga della matrice
•ogni altra cella `e adiacente (in verticale o in diagonale) alla cella che laprecede.
Il valore di una discesa `e dato dalla somma dei valori delle sue n celle.
Progettare un algoritmo che, data la matrice M, trova il valore massimo tra i valori delle possibili discese di M.
'''
def es14(M):
    T=[[0]*len(M) for _ in range(len(M))]
    # T[i][j] = valore massimo fino alla cella i,j 
    for i in range(len(M)):
        for j in range(len(M)):
            if i==0:
                T[i][j]=M[i][j]
            elif j==0:
                T[i][j]=max(T[i-1][j], T[i-1][j+1])+M[i][j]
            elif j==len(M)-1:
                T[i][j]=max(T[i-1][j], T[i-1][j-1])+M[i][j]
            else:
                T[i][j]=max(T[i-1][j], T[i-1][j-1], T[i-1][j+1])+M[i][j]
    for x in T:
        print(x)
    return max(T[-1])

M=[
    [12,10,3,14,9],
    [0,1,13,15,13],
    [8,10,1,2,7],
    [7,11,10,5,7],
    [18,4,6,10,0]
   ]
#print(es14(M))

'''
Abbiamo due interi k ed n con 1<=k<=n. Vogliamo sapere quanti diversi modi ci sono di partizionare
l'insieme dei primi n interi in k sottoinsiemi.
Progettare un algoritmo che risolve il problema in tempo O(n*k)
'''
def es15(n,k):
    T=[[0]*(k+1) for _ in range(n+1)]
    # T[i][j] = modi per posizionare i elementi in j insiemi
    for i in range(len(T)):
        for j in range(1, k+1):
            if i==0 or j>i:
                T[i][j]=0
            elif j==1:
                T[i][j]=1
            else:
                T[i][j] = T[i-1][j-1]+j*T[i-1][j]
    for x in T:
        print(x)
    return T[-1][-1]

#print(es15(4,2))


'''
Abbiamo diversi tipi di stringhe binarie lunghe al più 2, concatenando
stringhe siffatte possiamo ottenere stringhe binarie di lunghezza arbitraria.
Progettare un algoritmo che prende in input l’insieme I coi tipi di stringhe
disponibili ed una stringa binaria S lunga n e, in tempo O(n), conta i diversi
modi con cui è possibile ottenereSconcatentando le stringhe dei tipi disponibili.
'''
def es16(I,S):
    T=[0]*len(S)
    for i in range(len(S)):
        if (S[i] not in I) and (S[i-1:i+1] not in I):
            T[i]=0
        else:
            for k in I:
                if S[i]==k:
                    T[i]+=T[i-1]
                elif S[i-1:i+1]==k:
                    T[i]+=T[i-2]
            if T[i]==0:
                T[i]=1
    print(T)
    return T[-1]

S='001010'
I=['0','01','10']
#print(es16(I,S))

'''
Data  una  stringa  binaria      vogliamo  contare  il  numero  di  diverse  coppie presenti nella sequenza.Ad esempio:•per  la risposte deve essere  (abbiamo infatti ). •p e r  la risposta deve essere 8 (abbiamo infatti ).Progettare un algoritmo che risolve il problema in tempo   .
'''
def es17(S):
    T=[[0]*len(S) for _ in range(0,2)]
    for i in range(len(T)):
        for j in range(len(T[0])):
            if i==j==0 and S[j]=='0':
                T[i][j]=1
            elif i==j==0:
                T[i][j]=0
            elif S[j]=='0' and i==0:
                T[i][j]=T[i][j-1]+1
            elif i==0:
                T[i][j]=T[i][j-1]
            elif i==1 and j==0:
                T[i][j]=0
            elif i==1 and S[j]=='1':
                T[i][j]=T[i-1][j]+T[i][j-1]
            else:
                T[i][j]=T[i][j-1]
    for x in T:
        print(x)
    return T[-1][-1]

S='010010'
#print(es17(S))

'''
Vogliamo il numero di sequenze decimali di lunghezzanin cuinon  appaiono  cifre  pari  adiacenti.   Progettare  un  algoritmo  che  prende  comeparametro l’interone, in tempoO(n), restituisce il numero delle sequenze cuisiamo interessati
'''
def es18(n):
    T=[[0]*2 for _ in range(n+1)]
    T[1][0]=5
    T[1][1]=5
    for i in range(2,n+1):
        T[i][0]=T[i-1][1]*5
        T[i][1]=(T[i-1][0]+T[i-1][1])*5
    print(T)
    return sum(T[-1])

#print(es18(3))

'''
Data una sequenza S di interi positivi si vuole trovare una sottosequenza di S
senza elementi in posizioni consecutive e la somma dei cui elementi sia massima.
'''
def es19(S):
    T=[0]*len(S)
    # T[i] = somma massima fino all'elemento i
    T[0]=S[0]
    T[1]=S[1]
    for i in range(2,len(S)):
        T[i]=max(T[i-1],T[i-2]+S[i])
    print(T)
    return T[-1]

S=[1,5,4,6,10,3,2,9]
#print(es19(S))

'''
 Dati due interi non negativi n e k vogliamo sapere
in quanti modi è possibile partizionare l’insieme dei numeri da
1 a n in � k sottoinsiemi non vuoti.
'''
def es20(n,k):
    T=[[0]*(k+1) for _ in range(n+1)]
    # T[i][j] = modi per distribuire i elementi in j insiemi
    T[1][1]=1
    for i in range(1,len(T)):
        for j in range(1,len(T[0])):
            if j==1:
                T[i][j]=1
            elif j<=i:
                T[i][j]=j*T[i-1][j]+T[i-1][j-1]
    for x in T:
        print(x)
    return T[-1][-1]

#print(es20(5,3))

'''
Si considerino 3 stringhe A, B e C, di lunghezza n, m ed n + m, rispettivamente.
Diciamo che C `e l’intreccio di A e B se contiene tutti i caratteri di A e tutti i
caratteri di B e l’ordine di tutti i caratteri delle stringhe individuali `e preservato.
'''
def es21(A,B,C):
    # TODO
    T=[[False]*len(B) for _ in range(len(A))]
    k=0
    L=[0]*len(C)
    for i in range(len(T)):
        for j in range(len(T[0])):
            if i==0 and (C[k]==B[j]):
                T[i][j]=True
                L[k]=1
                k+=1
            elif j==0 and (C[k]==A[i]):
                T[i][j]=True
                L[k]=1
                k+=1
            elif (T[i-1][j] or T[i][j-1]) and (C[i+j]==A[i] or C[i+j]==B[j]):
                T[i][j]=True
                L[i+j]=1
    for x in T:
        print(x)
    return L.count(1)==len(L)
A='aabxxz'
B='abxy'
C='abaaxbxyxz'
#print(es21(A,B,C))

'''
Data una lista con una serie di tagli di monete ed
un importo da raggiungere, trovare il numero minimo
di monete necessarie per ottenere tale importo. Se non
è possibile ottenere quell’importo restituire -1.
'''
def es22(A,r):
    T=[[float('inf')]*len(A) for _ in range(r+1)]
    for i in range(1,len(T)):
        for j in range(0, len(T[0])):
            if i==A[j]:
                T[i][j]=1
            elif j==0 and i>A[j]:
                T[i][j]=T[i-A[j]][0]+1
            else:
                T[i][j]=min(T[max(i-A[j],0)][j]+1, T[i][j-1])

    for x in T:
        print(x)
    if T[-1][-1]==float('inf'):
        return -1
    return T[-1][-1]

A=[5,7,10,25]
#print(es22(A,62))

'''
Una progressione aritmetica è una sequenza di numeri in
cui la differenza tra le coppie di numeri adiacenti è
costante. Questa differenza costante è chiamata "ragione".
Ad esempio, la sequenza 2, 5, 8, 11, 14, è una progressione
aritmetica di ragione 3. Una sequenza di un solo elemento è
una progressione aritmetica di qualunque ragione.
Dato un array di n interi positivi ed un intero c vogliamo
contare le progressioni aritmetiche di ragione c che
compaiono come sottosequenze dell’array.
'''
def es24(S):
    T=[0]*len(S)
    T[0]=S[0]
    for i in range(1,len(S)):
        T[i]=S[i]
        for j in range(0,i):
            if S[i-j]<S[i]:
                T[i]=max(T[i-j]+S[i],T[i])
    print(T)
    return max(T)

S=[22,3,9,4,1,5,20,6,7,2]
#S=[3,9,4,1,6]
#print(es24(S))

'''
Progettare un algoritmo che, dato l’intero positivo n, in tempo O(n)
conta il numero di stringhe ternarie lunghe n che non
contengono né la sottostringa 02 né la sottostringa 20 (vale a
dire: le cifre adiacenti presenti nella stringa differiscono al più
di 1).
'''
def es25(n):
    T=[[0]*3 for _ in range(n+1)]
    # T[i][j] = numero di stringhe valide lunghe i che terminano con j
    T[1][0],T[1][1],T[1][2] = 1,1,1

    for i in range(2, len(T)):
        for j in range(3):
            if j==0 or j==2:
                T[i][j]=T[i-1][0]+T[i-1][1]
            else:
                T[i][j]=sum(T[i-1])

    for x in T:
        print(x)
    return sum(T[-1])

#print(es25(4))

'''
Progettare un algoritmo che, dato un intero n, restituisce il
numero di stringhe lunghe n che è possibile ottenere con i 4
simboli 0, 1, 2 e 3 facendo in modo che nelle stringhe non
compaiano mai due cifre dispari adiacenti.
'''
def es26(n):
    T=[[0]*4 for _ in range(n+1)]
    # T[i][j] = numero di stringhe valide lunghe i che terminano con j
    for j in range(4):
        T[1][j]=1

    for i in range(2,n+1):
        for j in range(4):
            if j%2==0:
                T[i][j]=sum(T[i-1])
            else:
                T[i][j]=T[i-1][0]+T[i-1][2]
    for x in T:
        print(x)
    return sum(T[-1])

#print(es26(4))

'''
Una pedina è posizionata sulla casella (0,0) in alto a sinistra di una scacchiera n×n e 
mediante una sequenza di mosse tra caselle adiacenti deve raggiungere la casella
(n-1,n-1) in basso a destra. Una pedina posizionata sulla casella (i,j) ha al più 
due mosse possibili: spostarsi verso La sequenza di caselle toccate dalla pedina nello 
spostarsi da (0,0) a (n-1,n-1) determina un cammino. Ogni casella della scacchiera è 
labellata con 0 o 1. Un cammino è definito lecito se non contiene caselle adiacenti 
con la stessa label. 
'''
def es27(M):
    T=[[0]*len(M) for _ in range(len(M))]
    # T[i][j] = modi validi per raggiungere la casella i,j
    for i in range(len(T)):
        for j in range(len(T)):
            if j==i==0:
                T[i][j]=1
            elif i==0 and M[i][j-1]!=M[i][j]:
                T[i][j]=T[i][j-1]
            elif j==0 and M[i-1][j]!=M[i][j]:
                T[i][j]=T[i-1][j]
            elif M[i-1][j]!=M[i][j] and M[i][j-1]!=M[i][j]:
                T[i][j]=T[i-1][j]+T[i][j-1]
            elif M[i-1][j]!=M[i][j]:
                T[i][j]=T[i-1][j]
            elif M[i][j-1]!=M[i][j]:
                T[i][j]=T[i][j-1]
    for x in T:
        print(x)
    return T[-1][-1]

M=[
    [1,1,0],
    [0,0,0],
    [1,0,1]
]
#print(es27(M))

'''
Progettare un algoritmo di programmazione dinamica che, dato un intero n, in tempo O(n),
calcoli il numero di stringhe sull'alfabeto {0,1,2,3} in cui non compaiono mai due
cifre pari adiacenti. 
'''
def es28(n):
    T=[[0]*4 for _ in range(n+1)]
    # T[i][j] = numero di stringhe valide lunghe i che terminano con j

    T[1]=[1,1,1,1]
    for i in range(2,len(T)):
        T[i][0]=T[i][2]=T[i-1][1]+T[i-1][3]
        T[i][1]=T[i][3]=sum(T[i-1])
    
    for x in T:
        print(x)
    return sum(T[-1])

#print(es28(4))

'''
Progettare un algoritmo di programmazione dinamica che, data una sequenza A di n interi 
positivi ed un intero k, in tempo O(nk), calcoli il numero di sottosequenze di A la 
somma dei cui elementi sia k. 
'''

'''
Si hanno n attivit`a e per ogni attivit`a, 1  i  n, l’intervallo temporale [si, fi)
in cui l’attivit`a dovrebbe svolgersi e il guadagno vi che si ottiene dallo svolgi-
mento dell’attivit`a. Due attivit`a i e j sono compatibili se gli intervalli temporali
[si, fi) e[sj , fj ) sono disgiunti ed il valore di un sottoinsieme di attivit`a `e dato
dalla somma dei valori delle attivit`a del sottoinsieme. Vogliamo selezionare un
sottoinsieme S di valore massimo di attivit`a tra loro compatibili. Descrivere un
algoritmo che risolve il problema in O(n2).
'''
def es30(A,V):
    T=[0]*len(A)
    T[0]=V[0]
    for i in range(1,len(A)):
        s=V[i]
        t=A[i]
        for j in range(i):
            if A[j][1]<=t[0] and A[j][0]<=t[1]:
                s+=V[j]
                t[0]=min(A[j][0],T[0])
                t[0]=max(A[j][1],T[1])

        T[i]=max(T[i-1], s)
    print(T)
    return T[-1]

A=[[1,4],[1,4],[4,6],[6,8],[3,4],[0,1]]
V=[10,7,6,5,4,3]
print(es30(A,V))

'''
Lyon, principe dell’impero di Grado, ha catturato e imprigionato in una fortezza
la principessa Eirika, del regno di Renais. La fortezza `e rappresentata da una
griglia di n×m stanze. Partendo dall’inizio della fortezza, la stanza (0, 0), il 
principe Ephraim deve raggiungere la cella in cui `e tenuta prigioniera sua sorella,
la stanza (n, m). Durante la traversata, Ephraim pu`o procedere solo nelle stanze
direttamente a sud o ad est della precedente (dunque pu`o solo spostarsi dalla casella
(i, j) alla casella (i + 1, j) o (i, j + 1)).
Ephraim possiede dei punti salute iniziali, rappresentati da un numero intero.
Ogni stanza del dungeon, incluse quella iniziale e quella finale, pu`o contenere

degli sgherri all’interno (la cui quantit`a `e rappresentata da un intero nega-
tivo) o delle cure (la cui quantit`a `e rappresentata da un intero positivo).

Per ogni sgherro affrontato in una stanza, Ephraim perder`a un punto salu-
te, mentre ne guadagner`a uno per ogni cura consumata. Se in un qualsiasi

momento la salute di Ephraim raggiunge un numero minore o uguale a 0,
Ephraim morir`a immediatamente.
Progettare un algoritmo che data in input la matrice M, i cui valori indicano
gli interi rappresentanti gli elementi all’interno delle stanze del dungeon, trovi
la minima quantit`a di salute che Ephraim deve avere per salvare sua sorella.
'''
