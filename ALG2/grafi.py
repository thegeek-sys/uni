from math import sqrt

def sortTop(G):
    gradoEnt = [0]*len(G)
    for i in range(len(G)):
        for v in G[i]:
            gradoEnt[v]+=1
    sorgenti = [ i for i in range(len(G)) if gradoEnt[i] == 0 ]
    ST = []
    while sorgenti:
        u = sorgenti.pop()
        ST.append(u)
        for v in G[u]:
            gradoEnt[v]-=1
            if gradoEnt[v] == 0:
                sorgenti.append(v)
    if len(ST) == len(G):
        return ST
    return []

'''
Progettare un algoritmo che prende come parametro un intero n e in tempo O(sqrt(n)) verifica se il numero n `e semiprimo.
Un numero si dice semiprimo se `e il prodotto di due numeri primi (non necessariamente diversi).
'''
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0: return False
    return True


def es1(n):
    l = []
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            l.append(i)
            l.append(n//i)
    if len(l)==2 and is_prime(l[0]) and is_prime(l[1]):
        return True
    return False

#print(es1(12))

'''
Dato un albero di n nodi rappresentato tramite il vettore dei padri P e due nodi 
dell'albero u e v, dare lo pseudocodice di un algoritmo che in tempo O(n) calcola 
la distranza tra u e v nell'albero
'''
def es2(P, u, v):
    t = 0
    i = u
    l = [0]*len(P)
    while P[i]!=i and P[i]!=v:
        t+=1
        l[i]=1
        i=P[i]

    if P[i] == i:
        c=v
        o = 0
        while True:
            if l[c] == 0:
                o+=1
                c=P[c]
            else:
                o-=1
                break
            if c==u: return o
            if c==P[c]: break

    return t+o

P = [1,1,0,1,3,2,2,8,0]
#print(es2(P,4,2))

'''
Dato un grafo diretto G con n nodi e m archi e
due suoi nodi a e b, chiamiamo equidistante un qualunque nodo
x di G che ha uguale distanza da a e da b, in caso contrario
diciamo che x è nella sfera di influenza di quello dei due nodi
che è a lui più vicino. Chiamiamo infine vettore delle influenze
rispetto ai nodi a e b il vettore D di n componenti dove D[i]
indica il nodo alla cui sfera d’influenza i appartiene e nel caso
x sia equidistante da a e b allora D[i] = −1.

In figura ad esempio è riportato a sinistra un grafo con evi-
denziati in bianco i due nodi a = 2 e b = 6 e sulla destra

i nodi colorati differentemente ad indicare le influenze e le
equidistanze. In questo caso il vettore delle influenze è D =
[2, −1, 2, −1, 6, −1, 6, −1, 2, 6, 6].
'''
def BFS_es3(G, x):
    D = [-1]*len(G)
    D[x] = 0
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u] + 1
                coda.append(y)
    return D


def es3(G, a, b):
    GT = [[] for _ in G]
    for i in range(len(G)):
        for v in G[i]:
            GT[v].append(i)
    A = BFS_es3(GT, a)
    B = BFS_es3(GT, b)
    E = [-1]*len(G)
    for i in range(len(A)):
        if A[i] == -1 and B[i] != -1:  # Nodo raggiungibile solo da b
            E[i] = b
        elif B[i] == -1 and A[i] != -1:  # Nodo raggiungibile solo da a
            E[i] = A
        elif A[i] < B[i]:
            E[i] = a
        elif A[i] > B[i]:
            E[i] = b
    return E

G = [[1, 2, 10],[4, 5, 9],[7],[0, 4, 9],[9],[2, 6, 8],[4, 7],[5],[0, 2],[6],[9]]
#print(es3(G, 2, 6))

'''
Dato un albero di n nodi rappresentato tramite il vettore dei padri P (per
covenzione il padre del nodo radice `e il nodo stesso) e un suo nodo x, dare lo
pseudocodice di un algoritmo che in tempo O(n) produce la lista dei nodi di T
presenti nel sottoalbero radicato in x.
'''
def es4(P, x):
    D = [x]
    i=0
    while len(D)>i:
        for y in range(len(P)):
            if P[y] == D[i]:
                D.append(y)
        i+=1
    return D

P = [2,3,2,4,2,3,4,0]
#print(es4(P, 4))


'''
Descrivere un algoritmo che, dato un grafo G non diretto e connesso e due suoi
nodi u e v, in tempo O(n + m) trova i nodi che hanno la stessa distanza da u e v.
'''
def DFS_es5(G, u):
    D = [-1]*len(G)
    D[u] = 0
    coda = [u]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i+=1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u]+1
                coda.append(y)
    return D

def es5(G, u, v):
    U = DFS_es5(G, u)
    V = DFS_es5(G, v)

    result = []
    for i in range(len(U)):
        if U[i] == V[i]:
            result.append(i)


'''
Descrivere un algoritmo che dato un grafo diretto G trova il minimo numero di
vertici da cui `e possibile raggiungere tutti gli altri vertici del grafo. L’algoritmo
deve avere complessit`a O(n + m).
'''
def DFSr_es6(G, x, visitati):
    visitati[x] = 0
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es6(G, y, visitati)

def es6(G):
    c = 0
    visitati = [-1]*len(G)
    for x in range(len(G)):
        if visitati[x] == -1:
            c+=1
            DFSr_es6(G, x, visitati)
    return c

G = [[1, 5], [0, 5], [4], [], [2], [0, 1]]
#print(es6(G))

'''
Un vertice v in un grafo diretto G, si dice principale se ogni altro vertice in G
pu`o essere raggiunto con un cammino diretto che parte da v.
a) Descrivere un algoritmo che dati un grafo G e un vertice v, determina se v
`e un vertice principale in G. L’algoritmo deve avere complessit`a O(n+m).
b) Descrivere un algoritmo che, dato un grafo G, determina se G contiene un
vertice principale. L’algoritmo deve avere complessit`a O(n + m).
'''
def DFSr_es7(G, x, visitati):
    visitati[x] = 0
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es7(G, y, visitati)

def es7a(G, v):
    visitati = [-1]*len(G)
    DFSr_es7(G, v, visitati)
    return sum(visitati) == 0

def es7b(G):
    visitati = [-1]*len(G)
    c = 0
    for x in range(len(G)):
        if visitati[x] == -1:
            DFSr_es7(G, x, visitati)
            c += 1
        if c == 2: return False
    return True

G = [[1],[2,3,4,5],[1,4,5],[0,1],[0,1],[1,2]]
#print(es7b(G))


'''
Dato un grafo diretto G chiamiamo pozzo un suo nodo privo di archi uscenti.
Dare lo pseudo-codice di un algoritmo che, dato un grafo diretto G ed un suo
nodo u, conta i nodi pozzo raggiungibili a partire da u. L’algoritmo deve avere
complessit`a O(n+ m). Ad esempio per il grafo in figura (che ha nodi pozzo 3, 6
e 9) l’algoritmo con u = 10 ritorna 0, con u = 2 ritorna 3 e con u = 9 ritorna 1.
'''
def DFSr_es8(G, x, visitati, raggiunti):
    visitati[x] = 0
    if len(G[x])>0: raggiunti[x] = -1
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es8(G, y, visitati, raggiunti)

def es8(G, u):
    visitati = [-1]*len(G)
    raggiunti = [0]*len(G)

    DFSr_es8(G, u, visitati, raggiunti)
    c = 0
    for i in range(len(G)):
        if visitati[i]==raggiunti[i]==0:
            c+=1
    return c

G = [[2,9],[0,2,5,7],[],[4,6],[10],[],[9],[8],[],[10],[3]]
#print(es8(G, 0))

'''
Dare lo pseudo-codice di un algoritmo che, dato un grafo non diretto G, conta
il numero delle componenti connesse di G che sono anche alberi. L’algoritmo
deve avere complessit`a O(n + m). Ad esempio per il grafo in figura l’algoritmo
ritorna 3.
'''
def DFSr_es9(G, x, visitati):
    visitati[x] = 0
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es9(G, y, visitati)

def cicli_es9(u, padre, G, cicli):
    cicli[u] = 1
    for v in G[u]:
        if cicli[v] == 1:
            if v != padre:
                return True
        else:
            if cicli_es9(v, u, G, cicli):
                return True
    return False

def es9(G):
    c = 0
    visitati = [-1]*len(G)
    cicli = [0]*len(G)
    for x in range(len(G)):
        if visitati[x] == -1:
            c+=1
            DFSr_es9(G, x, visitati)
            
            if cicli_es9(x, x, G, cicli):
                c-=1
    return c

G = [[1,2],[0,2],[0,1],[4,6,10],[3],[],[3],[8],[7],[10],[3,9],[12,13],[11,14,15],[11,14],[12,13],[12]]
#print(es9(G))

'''
esercizio appello straordinario
'''
def DFSr_es10(G, x, visitati):
    visitati[x] = 0
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es10(G, y, visitati)

def es10(G):
    visitati = [-1]*len(G)
    conn = []

    for x in range(len(G)):
        if visitati[x] == -1:
            DFSr_es10(G, x, visitati)
            conn.append(x)

    if len(conn) == 1:
        return []
    else:
        res = []
        for i in range(1,len(conn)):
            res.append((conn[i-1],conn[i]))

        return res

G = [[1,4],[0,4],[5,7],[6],[0,1],[2,7],[3],[2,5]]
#print(es10(G))

'''
Sia G un grafo completo con m archi. Descrivere un algoritmo che dato
G rappresentato tramite liste di adiacenza iun O(m) ne orienta gli archi
producento un grafo diretto aciclico
'''
def es11(G):
    res = []
    for i in range(len(G)):
        t = []
        for y in G[i]:
            if i<y:
                t.append(y)
        res.append(t)
    return res

G = [
    [1,2,3],
    [0,2,3],
    [0,1,3],
    [0,1,2]
]
#print(es11(G))

'''
Dato un grafo G, progettare un algoritmo che trovi i
punti di articolazione 
'''
def DFSr_es12(x, padre, altezza, ponti, figli):
    if padre == -1:
        altezza[x] = 0
    else:
        altezza[x] = altezza[padre]+1
    minR = altezza[x]
    for y in G[x]:
        if altezza[y] == -1:
            figli[x]+=1
            b = DFSr_es12(y, x, altezza, ponti, figli)
            if b > altezza[x]:
                ponti.append(x)
                ponti.append(y)
            minR = min(minR, b)
        elif y != padre:
            minR = min(minR, altezza[y])
    return minR

def es12(G):
    figli = [0]*len(G)
    ponti = []
    altezza = [-1]*len(G)

    DFSr_es12(0, -1, altezza, ponti, figli)

    if figli[0] > 1:
        art = [0]
    else:
        art = []

    for x in ponti:
        if figli[x] >= 1 and x != 0:
            art.append(x)
    return art

'''
Dato un grafo G e due sottoinsiemi V1 e V2 dei suoi vertici
si definisce distanza tra V1 e V2 la distanza minima per
andare da un nodo in V1 ad un nodo in V2. Nel caso V1 e V2
non sono disgiunti allora il valore 0.
Descrivere un algoritmo che, dato un grafo G e i due sottoinsiemi
dei vertici V1 e V2 calcola la loro distanza. L'algoritmo deve
avere complessità O(n+m)
'''
def es13(G, V1, V2):
    if V1&V2:
        return 0
    
    D = [-1]*len(G)
    for x in V1:
        D[x] = 0

    coda = list(V1)
    i = 0
    while len(coda) > i:
        u = coda[i]
        i+=1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u]+1
                coda.append(y)

    d = float('inf')
    for x in V2:
        if D[x] != -1:
            d = min(D[x], d)
    return d

G = [[1,11,12],[0,2,10,11],[1,3,9,13],[2,4],[3,5,8,13],[4,6,7],[5,13],[5,8],[4,7,9,14],[2,8,10],[1,8,9,14],[0,1,12],[0,11],[2,4,6],[8,10]]
V1 = {5, 11, 13}
V2 = {9, 14}
#print(es13(G, V1, V2))

'''
Una foglia di un albero è un vertice con un solo vicino. Dare
lo pseudocodice per un algoritmo che prende in input un albero
di n vertici in formato vettore dei padri e restituisce un
elenco di tutte le foglie con complessità O(n)
'''
def es14(P):
    F = [0]*len(P)

    for x in P:
        F[x] += 1

    r = []
    for i in range(len(F)):
        if F[i] == 0:
            r.append(i)

    return r

P = [7,0,7,2,5,2,7,7]
#print(es14(P))

'''
Dato un grafo G, restituire l'insieme X dei nodi che non formano cicli
'''
def cicli_es15(u, G, visitati):
    visitati[u] = 1
    for v in G[u]:
        if visitati[v] == 1:
            return True
        if visitati[v] == 0:
            if cicli_es15(v, G, visitati):
                return True
    visitati[u] = 2
    return False
        

def es15(G):
    visitati = [0]*len(G)
    X = []
    for u in range(len(G)):
        if visitati[u] == 0:
            cicli_es15(u, G, visitati)

    for i in range(len(visitati)):
        if visitati[i] == 2:
            X.append(i)
    print(visitati)
    return X

G = [
    [1,6],
    [],
    [0],
    [1],
    [2],
    [2],
    [5,7],
    [0,3]
]
#print(es15(G))

'''
Si consideri un labirinto rappresentato da una matrice quadrata binaria M di 
dimensioni n x n, in cui:
- M[i][j] = 0 indica una cella attraversabile
- M[i][j] = 1 indica un muro, quindi non attraversabile
Una porta è una cella M[i][j] = 0 che si trova sul bortdo della matrice. Una
cella attraversabile è detta raggiungibile se esiste un cammino formato solo da 
celle con valore 0 che le collega a una porta. Tra una cella e l'altra nei cammini
ci si può spostare solo orizzontalmente e verticalmente.
Progettare un algoritmo che, data la matrice M, in tempo O(n^2) determini il 
numero totale di celle raggiungibili nel labirinto
'''
def es16(G):
    tot = 0
    
    # prima e ultima riga
    for j in range(len(G[0])):
        # prima riga
        if G[0][j] == 0:
            G[0][j] = -1
            tot+=1

        # ultima riga
        if G[len(G)-1][j] == 0:
            G[len(G)-1][j] = -1
            tot+=1
    
    # prima e ultima colonna
    for i in range(len(G)):
        # prima colonna
        if G[i][0] == 0:
            G[i][0] = -1
            tot+=1

        # ultima colonna
        if G[i][len(G[0])-1] == 0:
            G[i][len(G[0])-1] = -1
            tot+=1

    # aggingo quelli dentro la matrice
    for i in range(1,len(G)-1):
        for j in range(1,len(G[0])-1):
            if G[i][j-1] == -1 or G[i-1][j] == -1:
                if G[i][j] == 0:
                    G[i][j] = -1
                    tot+=1

    # aggiungo i restanti
    for i in range(len(G)-2,0,-1):
        for j in range(len(G[0])-2,0,-1):
            if G[i][j+1] == -1 or G[i+1][j] == -1:
                if G[i][j] == 0:
                    G[i][j] = -1
                    tot+=1

    for i in range(1,len(G)-1):
        for j in range(1,len(G[0])-1):
            if G[i][j-1] == -1 or G[i-1][j] == -1:
                if G[i][j] == 0:
                    G[i][j] = -1
                    tot+=1

    return tot

def DFSr_es16_alt(x, G, visitati):
    visitati[x] = 0
    for u in G[x]:
        if visitati[u] == -1:
            DFSr_es16_alt(u, G, visitati)

def es16_alt(G):
    # trasformo il grafo in liste di adiancenza
    T = [[] for _ in range(len(G)*len(G))]
    entrance = []
    nodes = -1
    for i in range(len(G)):
        for j in range(len(G[0])):
            nodes += 1
            if G[i][j] == 0:
                if j<len(G[0]) and G[i][j+1] == 0:
                    T[nodes].append(nodes+1)
                    T[nodes+1].append(nodes)

                if i<len(G)-1 and G[i+1][j] == 0:
                    T[nodes].append(nodes+len(G))
                    T[nodes+len(G)].append(nodes)

                if i==0 or j==0 or i==len(G)-1 or j==len(G[0])-1:
                    entrance.append(nodes)

    visitati = [-1]*len(T)
    for x in entrance:
        if visitati[x] == -1:
            DFSr_es16_alt(x, T, visitati)

    return visitati.count(0)

G = [
    [1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,0,1,1,1,1],
    [1,1,1,0,1,0,1],
    [0,0,1,0,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1]
]
#print(es16(G))

'''
Sia dato un grafo non orientato e connesso G,
i cui nodi sono colorati. Un cammino lecito nel grafo è un
cammino che non attraversa nodi adiacenti dello stesso colore.
Dati due nodi a e b, l’obiettivo è trovare il numero minimo di
archi da percorrere per andare da aa a bb seguendo un cammino lecito.
Il grafo G è rappresentato tramite liste di adiacenza e i colori
dei nodi sono memorizzati in un vettore C, dove C[i] rappresenta
il colore del nodo i.

Progettare un algoritmo che, dati G, C, a, e b, risolva il problema
restituendo il minimo numero di archi da percorrere per spostarsi
da a a b lungo un cammino lecito. Se non esiste alcun cammino lecito
che connette a e b, l’algoritmo deve restituire None.

L’algoritmo deve avere una complessità O(m), dove m è il numero di archi nel grafo G.
'''
def es17(G, C, a, b):
    D = [-1]*len(G)
    D[a] = 0
    coda = [a]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        color = C[u]
        for y in G[u]:
            if D[y] == -1 and color != C[y]:
                D[y] = D[u]+1
                coda.append(y)

    return D[b]

G = [[1,2,3],[0,4,5,6],[0,6],[0,4],[1,3,5],[1,4,6],[1,2,5]]
C = [0,0,1,1,1,2,0]
#print(es17(G,C,6,1))

'''
Devo eseguire n lavori, ognuno dei quali ha un tempo d’esecuzione specifico. Mi
`e fornito un vettore T di n componenti, dove T [i] rappresenta il tempo richiesto
per eseguire il lavoro i. Inoltre ho una lista di liste P di n componenti, dove
P [i] contiene i lavori che devono essere completati prima che io possa iniziare il
lavoro i.
Procgettare un algoritmo che, dati T e P , in tempo O(n2), calcoli il tempo
minimo necessario per completare tutti i lavori tenendo conto che `e possibile
eseguire pi`u lavori in parallelo. L’algoritmo deve restituire +1 nel caso in
cui non sia possibile comletare tutti i lavori (ad esempio a causa di cicli di
dipendenza tra i lavori)
'''
def cicli_es18(u, G, visitati):
    visitati[u] = 0
    for y in G[u]:
        if visitati[y] == 1:
            return True
        if visitati[y] == 0:
            if cicli_es18(y, G, visitati):
                return True
    visitati[u] = 2
    return False

def es18(P, T):
    visitati = [-1]*len(P)
    for x in visitati:
        if visitati[x] == -1:
            if cicli_es18(x,P,visitati):
                return float('inf')

    S = [[] for _ in range(len(P))]
    for x in range(len(P)):
        for y in P[x]:
            S[y].append(x)

    D = [0]*len(P)
    ord = sortTop(S)
    for u in ord:
        for v in P[u]:
            D[u] = max(D[u],T[v]+D[v])
    return max(D[i]+T[i] for i in range(len(P)))


    
T = [3,2,5,4,3,1]
P = [[1,2],[3],[3],[4],[5],[]]
#print(es18(P,T))

'''
Progettare un algoritmo che, dato un DAG pesato G rappresentato mediante
liste di adiacenza ed un suo vertice sorgente s, restituisca il vettore delle distanze
dei nodi da s.
'''
def es19(G, s):
    D = [float('inf')]*len(G)
    D[s] = 0
    coda = [s]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i+=1
        for y in G[u]:
            if D[y[0]] == float('inf'):
                coda.append(y[0])
            D[y[0]] = min(D[y[0]], y[1]+D[u])

    return D

G = [[(2,1),(3,2),(5,4)],[(0,5),(3,1)],[],[(2,-3),(5,6)],[(1,6),(2,-2)],[],[]]
#print(es19(G,4))


'''
Dare lo pseudo-codice di un algoritmo che preso in input un grafo non diretto e 
connesso G, un suo nodo u, un vettore dei padri P relativo a una BFS da u in
G e un arco {v,w} di G, ritorna True se e solo se la rimozione dell'arco {v,w}
non cambia le distanze da u. L'algoritmo deve avere complessità O(n)
'''
def dist_es20(x, u, P):
    d = 0
    while x != u:
        x = P[x]
        d+=1
        if d > len(P):
            return -1
    return d

def es20(P,G,arco,u):
    # verifico se l'arco appartiene al grafo dei padri e verifico l'ordine
    v, w = arco
    if P[v] == w:
        # da w a v
        v, w = w, v
    # l'arco non appartiene al grafo
    elif P[w] != v:
        return False
    
    d = dist_es20(w, u, P)

    # questa modifica dell'albero non necessariamente deve essere corretta
    # mi serve solamente per verificare se il nodo w cambia livello
    for y in G[w]:
        if y != v:
            P[w]=y
            break

    #print(P)

    # calcolo la distanza di w da u 
    c = dist_es20(w, u, P)
    return c == d

G = [
    [1,3,4],
    [0,2,3],
    [1,3],
    [0,1,2,4],
    [0,3]
]
P = [1,2,2,2,3]
#print(es20(P,G,(2,1),2))

'''
Dare un algoritmo che, dato un grafo non diretto G, conta il numero delle componenti connesse di G che sono anche alberi. L'algoritmo deve avere complessità O(n+m)
'''
def albero_es21(G, x, visitati, u):
    if x!=u:
        visitati[x] = (0,0)
    visitati[u] = (visitati[u][0]+1, visitati[u][1])
    for y in G[x]:
        visitati[u] = (visitati[u][0], visitati[u][1]+1)
        if visitati[y] == (-1,-1):
            albero_es21(G, y, visitati, u)

def es21(G):
    visitati = [(-1,-1)]*len(G)
    alb=0
    for x in range(len(G)):
        if visitati[x] == (-1,-1):
            visitati[x] = (0,0)
            albero_es21(G, x, visitati, x)
            n, a = visitati[x][0], visitati[x][1]
            if a == 2*(n-1):
                alb+=1
    return alb

G = [[1,2],[0,2],[0,1],[4,6,10],[3],[],[3],[8],[7],[10],[3,9],[12,13],[11,14,15],[11,14],[12,13],[12]]
print(es21(G))
