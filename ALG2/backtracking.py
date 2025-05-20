'''
Progettare un algoritmo che, dati due  interi n e k, stampa tutte le stringhe  binarie di
lunghezza n in cui siano presenti almeno k zeri  consecutivi.
'''
from re import L


def es1(n,k,sol=[],cur=0,m=0):
    if len(sol)==n:
        print(sol)
        return
    sol.append(0)
    cur+=1
    es1(n,k,sol,cur,max(cur,m))
    sol.pop()
    cur-=1
    if k<n-len(sol) or m>=k:
        sol.append(1)
        es1(n,k,sol,0,m)
        sol.pop()

#es1(4,2)

'''
Progettare  un  algoritmo  che  dati tre  interi  positivi n, m e k, 
con 1<=m,k<=n, stampa tutte le stringhe ternarie lunghe n sull'alfabeto {0,1,2}
dove il numero di occorrenze di 1 non supera m ed il numero di occorrenze di 2 non supera k
L’algoritmo  proposto  deve  avere  complessità   dove  è il numero di stringhe da  stampare. 
'''
def es2(n,m,k,sol=[],uni=0,due=0):
    if len(sol)==n:
        print(sol)
        return

    sol.append(0)
    es2(n,m,k,sol,uni,due)
    sol.pop()

    if uni+1<=m:
        uni+=1
        sol.append(1)
        es2(n,m,k,sol,uni,due)
        uni-=1
        sol.pop()

    if due+1<=k:
        due+=1
        sol.append(2)
        es2(n,m,k,sol,uni,due)
        due-=1
        sol.pop()

#es2(3,1,2)

'''
Vogliamo trovare le sequenze di lunghezzansull’alfabeto{0,1,2}in cui non appaiono cifre
pari adiacenti. Progettare un algoritmo che prendecome parametro l’interone stampa
tutte le sequenze cui siamo interessati.
'''
def es3(n,sol=[],p=False):
    if len(sol)==n:
        print(sol)
        return

    sol.append(1)
    es3(n,sol,False)
    sol.pop()

    if p==False:
        sol.append(0)
        es3(n,sol,True)
        sol.pop()
        sol.append(2)
        es3(n,sol,True)
        sol.pop()

#es3(2)

'''
Progettare un algoritmo che dato un intero n ≥ 3
stampa tutte le stringhe ternarie lunghe n in cui non compaiono
3 elementi adiacenti la cui somma sia un numero pari. 
'''
def es4(n, sol=[]):
    if len(sol)==n:
        print(sol)
        return
    if len(sol)<2 or ((sol[-1]+sol[-2]+0)%2==1):
        sol.append(0)
        es4(n,sol)
        sol.pop()
    if len(sol)<2 or ((sol[-1]+sol[-2]+1)%2==1):
        sol.append(1)
        es4(n,sol)
        sol.pop()
    if len(sol)<2 or ((sol[-1]+sol[-2]+2)%2==1):
        sol.append(2)
        es4(n,sol)
        sol.pop()

#es4(4)

'''
Progettare un algoritmo che, dato un interon, stampa tutte le stringhe binariedi
lunghezza 2ntali che il numero di zeri presenti nella prima metà della stringa
è inferiore o uguale al numero di uni presenti nella seconda metà.
'''
def es5(n, sol=[], zero=0, uno=0):
    if len(sol)==2*n:
        print(sol)
        return
    if zero<=uno or len(sol)<n:
        sol.append(0)
        if len(sol)<=n:
            zero+=1
        es5(n, sol, zero, uno)
        if len(sol)<=n:
            zero-=1
        sol.pop()
    sol.append(1)
    if len(sol)>=n:
        uno+=1
    es5(n, sol, zero, uno)
    if len(sol)>=n:
        uno-=1
    sol.pop()

#es5(2)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le stringhe lunghe n con simboli in {a, b} dove i blocchi di simboli
a di lunghezza massima che appaiono nella stringa hanno lunghezza
pari
'''
def es6(n, sol=[], k=0):
    if len(sol)==n:
        print(sol)
        return
    if len(sol)!=n-1 or (len(sol)==n-1 and k%2!=0):
        sol.append('a')
        es6(n, sol, k+1)
        sol.pop()
    if k%2==0:
        sol.append('b')
        es6(n, sol, k)
        sol.pop()

#es6(5)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le stringhe lunghe n con simboli in {a, b} che contengono un
numero dispari di simboli a ed un numero dispari di simboli b.
'''
def es7(n, sol=[], a=0, b=0):
    if n%2==1:
        return
    if len(sol)==n:
        print(sol)
        return
    if a%2==0 or (a%2==1 and a+b<n-1):
        sol.append('a')
        es7(n,sol,a+1,b)
        sol.pop()
    if b%2==0 or (b%2==1 and a+b<n-1):
        sol.append('b')
        es7(n,sol,a,b+1)
        sol.pop()

#es7(4)

'''
Dare lo pseudo-codice di un algoritmo che dato un intero n, stampa
tutte le stringhe palindromi lunghe 2n con valori in {a, b}
'''
def es8(n, sol=[],k=-1):
    if 2*n==len(sol):
        print(sol)
        return
    if len(sol)<n:
        sol.append('a')
        es8(n,sol,k)
        sol.pop()
        sol.append('b')
        es8(n,sol,k)
        sol.pop()
    else:
        sol.append(sol[k])
        k-=2
        es8(n,sol,k)
        sol.pop()

#es8(2)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le sequenze lunghe n formate da interi nell’insieme {1, 2, 3, 4}
con la propriet`a che nella sequenza numeri adiacenti distano almeno
2.
'''
def es9(n, sol=[]):
    if len(sol)==n:
        print(sol)
        return
    for i in range(1,5):
        if len(sol)<1 or (sol[-1]!=i-1 and sol[-1]!=i+1 and sol[-1]!=i):
            sol.append(i)
            es9(n, sol)
            sol.pop()

#es9(3)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero pari n, stampa
tutte le permutazioni dei primi n interi in cui nell’ordinamento non
appaiono mai due pari consecutivi n`e due dispari consecutivi.
'''
def es10(n, sol=[]):
    if len(sol)==n:
        print(sol)
        return
    for i in range(1,n+1):
        if len(sol)==0 or (i%2!=sol[-1]%2 and i not in sol):
            sol.append(i)
            es10(n,sol)
            sol.pop()

#es10(4)

'''
Dare lo pseudo-codice di un algoritmo che presi i tre interi n, m e k,
stampa tutte le sequenze di n interi positivi con interi di valore al pi`u
m e nelle quali nessun intero compare pi`u di k volte.
'''
def es11(n,m,k):
    L=[0]*(m+1)
    es11_1(n,m,k,[],L)

def es11_1(n,m,k,sol,L):
    if len(sol)==n:
        print(sol)
        return
    for i in range(1, m+1):
        if L[i]<k:
            L[i]+=1
            sol.append(i)
            es11_1(n,m,k,sol,L)
            sol.pop()
            L[i]-=1

#es11(3,2,2)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici n ⇥ n e valori in {a, b, c} con la propriet`a che i simboli
in ogni riga sono tutti uguali.
'''
def es12_1(n,sol=[]):
    if n==len(sol):
        for x in sol:
            print(x)
        print()
        return
    sol.append(['a']*n)
    es12_1(n,sol)
    sol.pop()
    sol.append(['b']*n)
    es12_1(n,sol)
    sol.pop()
    sol.append(['c']*n)
    es12_1(n,sol)
    sol.pop()

#es12_1(2)

'''
Progettare un algoritmo che, dato un intero n, stampa tutte le stringhe di lunghezza 2*n
sull’alfabeto {1,2,3} tali che il numero di cifre dispari presenti nella prima metà della
stringa è lo stesso del numero di cifre dispari presenti nella seconda metà.
'''
def es13(n, sol=[], f=0, s=0):
    if len(sol)==n*2:
        print(sol)
        return
    for i in range(1,4):
        if len(sol)<n:
            sol.append(i)
            es13(n, sol, f+(1 if i%2==1 else 0), s)
            sol.pop()
        elif s<f and i%2==1:
            sol.append(i)
            es13(n, sol, f, s+1)
            sol.pop()
        elif i%2==0 and (s==f or (s<f and 2*n-len(sol)>f-s)):
            sol.append(i)
            es13(n, sol, f, s)
            sol.pop()

#es13(2)

'''
Progettare un algoritmo che data una stringa X lunga n sull’alfabeto {0,1,2} stampa 
tutte le stringhe lunghe n sull’alfabeto {0,1,2} che concordano con la stringa X in
esattamente una posizione.
'''
def es14(X, sol=[], got=False):
    if len(sol)==len(X):
        print(sol)
        return
    if len(sol)==len(X)-1 and not got:
        sol.append(X[-1])
        es14(X, sol, not got)
        sol.pop()
    for i in range(3):
        if got and str(i)!=X[len(sol)]:
            sol.append(str(i))
            es14(X, sol, got)
            sol.pop()
        elif not got and len(sol)!=len(X)-1:
            sol.append(str(i))
            es14(X, sol, True if X[len(sol)-1]==str(i) else False)
            sol.pop()

#es14('200')

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici ternarie n×n con la proprietà che le righe e le colonne
della matrice risultano ordinate in modo crescente.
'''
def es15(n):
    sol=[[0]*n for _ in range(n)]
    es15_1(n, sol, 0, 0)

def es15_1(n, sol, i, j):
    if i==n:
        for x in sol:
            print(x)
        print()
        return
    
    if j==n-1:
        i1=i+1
        j1=0
    else:
        i1=i
        j1=j+1

    sol[i][j]=3
    es15_1(n, sol, i1, j1)

    if (j==0 or sol[i][j-1]<=2) and (i==0 or sol[i-1][j]<=2):
        sol[i][j]=2
        es15_1(n, sol, i1, j1)

    if (j==0 or sol[i][j-1]<=1) and (i==0 or sol[i-1][j]<=1):
        sol[i][j]=1
        es15_1(n, sol, i1, j1)

es15(2)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici binarie n×n con la proprietà che nella matrice non
compaiono mai due uni adiacenti in orizzontale, in verticale o in di-
agonale.
'''
def es16(n):
    sol=[[0]*n for _ in range(n)]
    es16_1(n, sol, 0, 0)

def es16_1(n, sol, i, j):
    if i==n:
        for x in sol:
            print(x)
        print()
        return

    if j==n-1:
        i1=i+1
        j1=0
    else:
        i1=i
        j1=j+1

    sol[i][j]=0
    es16_1(n, sol, i1, j1)

    if (i==0 or sol[i-1][j]==0) and (j==0 or sol[i][j-1]==0) and ((j==0 or i==0) or sol[i-1][j-1]==0) and ((j==n-1 or i==0) or sol[i-1][j+1] == 0):
        sol[i][j]=1
        es16_1(n, sol, i1, j1)

#es16(3)
