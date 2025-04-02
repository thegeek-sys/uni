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
    coda = [x]
    i = 0
    D = [-1]*len(G)
    D[x] = 0
    while len(coda) > i:
        u = coda[i]
        i+=1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u]+1
                coda.append(y)
    return D

def es3(G, u, v):
    GT = [[] for _ in G]
    for i in range(len(G)):
        for y in G[i]:
            GT[y].append(i)

    Du = BFS_es3(GT, u)
    Dv = BFS_es3(GT, v)
    f = [-1]*len(G)
    for i in range(len(G)):
        if Du[i]>Dv[i]:
            f[i] = v
        elif Dv[i]>Du[i]:
            f[i] = u
    return f

G = [[1, 2, 10],[4, 5, 9],[7],[0, 4, 9],[9],[2, 6, 8],[4, 7],[5],[0, 2],[6],[9]]
#print(es3(G, 2, 6))

'''
Dato un albero di n nodi rappresentato tramite il vettore dei padri P (per
covenzione il padre del nodo radice `e il nodo stesso) e un suo nodo x, dare lo
pseudocodice di un algoritmo che in tempo O(n) produce la lista dei nodi di T
presenti nel sottoalbero radicato in x.
'''
def DFSr_es4(G,x,visitati):
    visitati[x] = 0
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es4(G,y,visitati)

def es4(P,x):
    G = [[] for _ in P]
    for i in range(len(P)):
        G[P[i]].append(i)

    visitati = [-1]*len(G)
    DFSr_es4(G,x,visitati)
    f = []
    for i in range(len(visitati)):
        if visitati[i] == 0:
            f.append(i)
    return f

P = [2,3,2,4,2,3,4,0]
#print(es4(P, 4))


'''
Descrivere un algoritmo che, dato un grafo G non diretto e connesso e due suoi
nodi u e v, in tempo O(n + m) trova i nodi che hanno la stessa distanza da u e v.
'''
def BFS_es5(G, x):
    D = [-1]*len(G)
    D[x] = 0
    coda = [x]
    i=0
    while len(coda) > i:
        u = coda[i]
        for y in G[u]:
            if D[y] == -1:
                coda.append(y)
                D[y] = D[u]+1
    return D

def es5(G, u, v):
    Du = BFS_es5(G, u)
    Dv = BFS_es5(G, v)
    f = []
    for i in range(len(G)):
        if Du[i]==Dv[i]:
            f.append(i)
    return f


'''
Descrivere un algoritmo che dato un grafo diretto G trova il minimo numero di
vertici da cui `e possibile raggiungere tutti gli altri vertici del grafo. L’algoritmo
deve avere complessit`a O(n + m).
'''

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
def es7_a(G,x):
    D = [-1]*len(G)
    D[x] = 0
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u]+1
    return D.count(1)==len(G)

def es7_b(G):
    for x in G:
        if len(x) == len(G)-1:
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
def DFSr_es8(G, x, visitati, pozzi):
    visitati[x] = 0
    if len(G[x])==0:
        pozzi.append(x)
    for y in G[x]:
        if visitati[y] == -1:
            DFSr_es8(G, y, visitati, pozzi)

def es8(G, x):
    pozzi = []
    visitati = [-1]*len(G)
    DFSr_es8(G, x, visitati, pozzi)
    return len(pozzi)

G = [[2,9],[0,2,5,7],[],[4,6],[10],[],[9],[8],[],[10],[3]]
#print(es8(G,8))

'''
Dare lo pseudo-codice di un algoritmo che, dato un grafo non diretto G, conta
il numero delle componenti connesse di G che sono anche alberi. L’algoritmo
deve avere complessit`a O(n + m). Ad esempio per il grafo in figura l’algoritmo
ritorna 3.
'''

G = [[1,2],[0,2],[0,1],[4,6,10],[3],[],[3],[8],[7],[10],[3,9],[12,13],[11,14,15],[11,14],[12,13],[12]]
#print(es9(G))

'''
esercizio appello straordinario
'''

G = [[1,4],[0,4],[5,7],[6],[0,1],[2,7],[3],[2,5]]
#print(es10(G))

'''
Sia G un grafo completo con m archi. Descrivere un algoritmo che dato
G rappresentato tramite liste di adiacenza iun O(m) ne orienta gli archi
producento un grafo diretto aciclico
'''

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
    D=[-1]*len(G)
    coda = []
    for x in V1:
        coda.append(x)
        D[x]=0
    i=0
    while len(coda) > i:
        u = coda[i]
        i+=1
        for v in G[u]:
            if D[v]==-1:
                D[v]=D[u]+1
                coda.append(v)

    d=float('inf')
    for i in V2:
        if D[i]!=-1:
            d=min(d,D[i])

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
    vis=[-1]*len(P)
    for i in range(len(vis)):
        vis[P[i]]=0
    f=[]
    for i in range(len(vis)):
        if vis[i]==-1:
            f.append(i)
    return f

P = [7,0,7,2,5,2,7,7]
#print(es14(P))

'''
Dato un grafo G, restituire l'insieme X dei nodi che non formano cicli
'''

G = [[1,6],[],[0],[1],[2],[2],[5,7],[0,3]]
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
def DFSr_es16(x,G,vis):
    vis[x] = 0
    for y in G[x]:
        if vis[y]==-1:
            DFSr_es16(y,G,vis)

def es16(G):
    T = [[] for _ in range(len(G)*len(G))]
    e = []
    nodes = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            nodes+=1
            if G[i][j]==0:
                if i!=len(G)-1 and G[i+1][j]==0:
                    T[nodes].append(nodes+len(G))
                    T[nodes+len(G)].append(nodes)

                if j!=len(G)-1 and G[i][j+1]==0:
                    T[nodes].append(nodes+1)
                    T[nodes+1].append(nodes)

                if i==0 or j==0 or i==len(G)-1 or j==len(G)-1:
                    e.append(nodes)

    print(e)
    vis = [-1]*len(T)
    for x in e:
        if vis[x]==-1:
            DFSr_es16(x, T, vis)
    return vis.count(0)

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
def es17(G,C,a,b):
    D=[-1]*len(G)
    D[a]=0
    coda=[a]
    i=0
    while len(coda) > i:
        u=coda[i]
        i+=1
        for y in G[u]:
            if D[y]==-1 and C[y]!=C[u]:
                D[y]=D[u]+1
                coda.append(y)
    if D[b]==-1:
        return None
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
    
T = [3,2,5,4,3,1]
P = [[1,2],[3],[3],[4],[5],[]]
#print(es18(P,T))

'''
Progettare un algoritmo che, dato un DAG pesato G rappresentato mediante
liste di adiacenza ed un suo vertice sorgente s, restituisca il vettore delle distanze
dei nodi da s.
'''

G = [[(2,1),(3,2),(5,4)],[(0,5),(3,1)],[],[(2,-3),(5,6)],[(1,6),(2,-2)],[],[]]
#print(es19(G,4))


'''
Dare lo pseudo-codice di un algoritmo che preso in input un grafo non diretto e 
connesso G, un suo nodo u, un vettore dei padri P relativo a una BFS da u in
G e un arco {v,w} di G, ritorna True se e solo se la rimozione dell'arco {v,w}
non cambia le distanze da u. L'algoritmo deve avere complessità O(n)
'''

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

G = [[1,2],[0,2],[0,1],[4,6,10],[3],[],[3],[8],[7],[10],[3,9],[12,13],[11,14,15],[11,14],[12,13],[12]]
#print(es21(G))

def es(s,t,A):
    G = [[] for _ in A]
    for i in range(len(A)):
        for j in range(len(A)):
            if i!=j:
                d=0
                for k in range(len(s)):
                    if A[i][k]!=A[j][k]:
                        d+=1
                if d<=1:
                    G[i].append(j)
    u=A.index(s)
    v=A.index(t)
    
    P=[-1]*len(A)
    P[u]=u
    coda=[u]
    i=0
    
    while len(coda) > i:
        x = coda[i]
        i+=1
        for y in G[x]:
            if P[y]==-1:
                P[y]=x
                coda.append(y)

    if P[v]==-1:
        return []
    f = []
    while v!=P[v]:
        f.append(A[v])
        v=P[v]
    f.append(A[v])
    f.reverse()
    return f

A = ['dote','rata','cave','data','cate','rapa','cane','core','rate','cose']
print(es('cane','data',A))
