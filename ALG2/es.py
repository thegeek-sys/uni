from math import sqrt

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

def cicli_es9(x, G, cicli):
    cicli[x] = 1
    for v in G[x]:
        if cicli[v] == 1:
            return True
        if cicli[v] == 0:
            if cicli_es9(v, G, cicli):
                return True
    cicli[x] = 2
    return False

def es9(G):
    c = 0
    visitati = [-1]*len(G)
    cicli = [0]*len(G)
    for x in range(len(G)):
        if visitati[x] == -1:
            c+=1
            DFSr_es9(G, x, visitati)
            
            if cicli_es9(x, G, cicli):
                c-=1
    return c

G = [
    [1,2],
    [0,2],
    [0,1],
    [4,6,10],
    [3],
    [],
    [3],
    [8],
    [7],
    [10],
    [3,9],
    [12,13],
    [11,14,15],
    [11,14],
    [12,13],
    [12]
]
#print(es9(G))
visitati = [0]*len(G)
#print(cicli_es9(8,G,visitati))

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
