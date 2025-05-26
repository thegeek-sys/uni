'''
Progettare un algoritmo che, dati due  interi n e k, stampa tutte le stringhe  binarie di
lunghezza n in cui siano presenti almeno k zeri  consecutivi.
'''
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

#es15(2)

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

'''
Progettare un algoritmo che dato un intero positivo n in input stampi 
tutte le stringhe contenenti n coppie di parentesi, ossia per ogni
parentesi aperta deve esservene una chiusa. La complessit`a dell’algoritmo
deve essere O(nS(n)), dove S(n) sono il numero
di stringhe da stampare.
'''
def es17(n, sol=[], open=0, close=0):
    if len(sol)==2*n:
        print(''.join(sol))
        return
    if open<n:
        sol.append('(')
        es17(n, sol, open+1, close)
        sol.pop()
    if close<open:
        sol.append(')')
        es17(n, sol, open, close+1)
        sol.pop()

#es17(3)

'''
Dato un numero intero positivo n, definiamo come partizioni di tutte
le sequenze di elementi inferiori o uguali ad n la cui somma `e
esattamente n. In particolare, distinguiamo tra partizioni con ordine
e senza ordine.
'''
def es18(n, sol=[], s=0):
    if s==n:
        print(sol)
        return
    for i in range(1,n+1):
        if s+i<=n:
            sol.append(i)
            es18(n, sol, s+i)
            sol.pop()
#es18(4)

'''
progettare  un  algoritmo  che  data    una  stringa  lunga   sull’alfabeto   stampa tutte  le  stringhe  lunghe   sull’alfabeto   che  differiscono  da   in  ciascuna posizione e non hanno simboli adiacenti uguali. 
'''
def es19(X, sol=[]):
    if len(X)==len(sol):
        print(sol)
        return
    for i in range(0,3):
        if str(i)!=X[len(sol)] and (len(sol)==0 or (len(sol)>0 and str(i)!=sol[-1])):
            sol.append(str(i))
            es19(X,sol)
            sol.pop()

#es19('2001')

'''
Progettare un algoritmo che, dato un intero    , stampa tutte le matrici binarie con  la proprietà che nella riga , ,  della matrice sono presenti esattamente  uni. L'algoritmo proposto deve avere complessità  dove  è il numero di matrici  da  stampare.
'''
def es20(n):
    sol=[[0]*n for _ in range(n)]
    es20_1(n,sol,0,0,0)

def es20_1(n,sol,i,j,k):
    if i==len(sol):
        for x in sol:
            print(x)
        print()
        return
    if j==n-1:
        j1=0
        i1=i+1
    else:
        j1=j+1
        i1=i
    
    if k<i:
        sol[i][j]=1
        if j1==0:
            es20_1(n,sol,i1,j1,0)
        else:
            es20_1(n,sol,i1,j1,k+1)

    if n-(j+1)>=i-k:
        sol[i][j]=0
        if j1==0:
            es20_1(n,sol,i1,j1,0)
        else:
            es20_1(n,sol,i1,j1,k)
#es20(3)

'''
bbiamo una matriceMdi interi di dimensionen⇥nconn>1. Unadiscesasu questa matrice `e una sequenza dincelle della matrice con i seguenti vincoli•le celle appartengono a righe diverse della matrice•la prima cella appartiene alla prima riga della matrice•ogni altra cella `e adiacente (in verticale o in diagonale) alla cella che laprecede.
'''
def es21(M,sol=[],i=0,j=0):
    if len(sol)==len(M)-1:
        sol.append(M[i][j])
        print(sol)
        return

    sol.append(M[i][j])
    if j>0:
        es21(M,sol,i+1,j-1)
        sol.pop()
    es21(M,sol,i+1,j)
    sol.pop()
    if j+1<len(M):
        es21(M,sol,i+1,j+1)
        sol.pop()


M=[
    [1,2],
    [3,4]
]
#es21(M)

'''
Cerchiamo un particolare numero telefonico e sappiamo che:•il numero `e composto dancifre.•non contiene cifre uguali adiacenti•nel comporre il numero sul tastierino basta spostarsi solo tra tasti adiacentiin orizzontale o verticale
Progettare un algoritmo che, daton, enumera tutte le combinazioni possibiliper il numero telefonico da ricercare
'''
def es22(n):
    next = {
        0: [8],
        1:[2,4],
        2:[1,3,5],
        3:[2,6],
        4:[1,5,7],
        5:[2,4,6,8],
        6:[3,5,9],
        7:[4,8],
        8:[5,7,9,0],
        9:[6,8]
    }
    for x in range(10):
        es22_1(n, [x], next)


def es22_1(n, sol, next):
    if len(sol)==n:
        print(sol)
        return
    
    for i in next[sol[-1]]:
        sol.append(i)
        es22_1(n, sol, next)
        sol.pop()

#es22(2)
        
'''
Progettare  un  algoritmo  che,  dato  un  intero ,  stampa  tutte  le  stringhe  binarie  di lunghezza     tali  che  il  numero  di  uni  presenti  nella  prima  metà  della  stringa  è  lo stesso del numero di uni presenti nella seconda metà.
'''
def es23(n, sol=[], first=0, sec=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append(1)
        es23(n, sol, first+1, sec)
        sol.pop()
        sol.append(0)
        es23(n, sol, first, sec)
        sol.pop()
    else:
        if sec<first:
            sol.append(1)
            es23(n, sol, first, sec+1)
            sol.pop()
        if sec==first or 2*n-len(sol)>first-sec:
            sol.append(0)
            es23(n, sol, first, sec)
            sol.pop()

#es23(2)

'''
Progettare  un  algoritmo  che,  data  una  sequenza  decimaleSlungan, stampa le sottosequenze diSstrettamente crescenti.L’algoritmo proposto deve avere complessit`aO(nD(n)) doveD(n)`eilnumerodi sequenze da stampare.
'''
def es24(S, i=0, sol=[]):
    if i==len(S) and len(sol)>0:
        print(sol)
        return
    if len(sol)==0 or S[i]>sol[-1]:
        sol.append(S[i])
        es24(S,i+1,sol)
        sol.pop()
    es24(S,i+1,sol)

#es24([3,2,4,5,4])

'''
Progettare un algoritmo che,  dato l’interon,  stampa tutte lesequenze  lunghensull’alfabeto  ternario{a,b,c}dove  il  simboloa`e  sempreseguito da almeno due simbolib.L’algoritmo proposto deve avere complessit`aO(nS(n)) doveS(n)`eilnumerodi sequenze da stampare.
'''
def es25(n, sol=[], a=0):
    if len(sol)==n:
        print(''.join(sol))
        return
    if a>0:
        sol.append('b')
        es25(n,sol,a-1)
        sol.pop()
    else:
        sol.append('b')
        es25(n,sol,a)
        sol.pop()
        sol.append('c')
        es25(n,sol,a)
        sol.pop()
    if n-len(sol)>2 and a==0:
        sol.append('a')
        es25(n,sol,2)
        sol.pop()

#es25(4)

'''
Progettare un algoritmo che, dati due  interi    e , stampa tutte le stringhe  binarie di lunghezza    in cui siano presenti almeno  zeri  consecutivi.
'''
def es26(n,k,sol=[],l=0):
    if len(sol)==n:
        print(sol)
        return
    sol.append(0)
    es26(n,k,sol,l+1)
    sol.pop()
    if n-(len(sol)+1)>=k or l>=k:
        sol.append(1)
        if l>=k:
            es26(n,k,sol,l)
        else:
            es26(n,k,sol,0)
        sol.pop()

#es26(4,2)

'''
Progettare  un  algoritmo  che  dati    tre  interi  positivi ,  e ,  con , stampa tutte le     stringhe ternarie lunghe  sull'alfabeto    dove il numero di occorrenze di  non  supera  ed il numero di occorrenze di  non supera L’algoritmo  proposto  deve  avere  complessità   dove  è il numero di stringhe da  stampare.
'''
def es27(n,m,k,sol=[],uno=0,due=0):
    if len(sol)==n:
        print(sol)
        return
    sol.append(0)
    es27(n,m,k,sol,uno,due)
    sol.pop()
    if uno<m:
        sol.append(1)
        es27(n,m,k,sol,uno+1,due)
        sol.pop()
    if due<k:
        sol.append(2)
        es27(n,m,k,sol,uno,due+1)
        sol.pop()

#es27(3,1,2)

'''
Vogliamo trovare le sequenze di lunghezzansull’alfabeto{0,1,2}in cui non appaiono cifre pari adiacenti. Progettare un algoritmo che prendecome parametro l’interone stampa tutte le sequenze cui siamo interessati.
'''
def es28(n, sol=[]):
    if len(sol)==n:
        print(sol)
        return
    sol.append(1)
    es28(n,sol)
    sol.pop()
    if len(sol)==0 or sol[-1]%2!=0:
        sol.append(0)
        es28(n,sol)
        sol.pop()
        sol.append(2)
        es28(n,sol)
        sol.pop()
#es28(2)

'''
Progettare un algoritmo che, dato un interon, stampa tutte le stringhe binariedi lunghezza 2ntali che il numero di zeri presenti nella prima met`a della stringa`e inferiore o uguale al numero di uni presenti nella seconda met`a.L’algoritmo proposto deve avere complessit`aO(nS(n)) doveS(n)`eilnumerodi stringhe da stampare.
'''
def es29(n,sol=[],zero=0,uno=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append(0)
        es29(n,sol,zero+1,uno)
        sol.pop()
        sol.append(1)
        es29(n,sol,zero,uno)
        sol.pop()
    else:
        if 2*n-len(sol)>zero-uno:
            sol.append(0)
            es29(n,sol,zero,uno)
            sol.pop()
        sol.append(1)
        es29(n,sol,zero,uno+1)
        sol.pop()
#es29(2)

'''
Progettare un algoritmo che, dato un interon, stampa tutte le stringhe binariedi lunghezza 2ntali che il numero di zeri presenti nella prima met`a della stringa`e inferiore o uguale al numero di uni presenti nella seconda met`a.L’algoritmo proposto deve avere complessit`aO(nS(n)) doveS(n)`eilnumerodi stringhe da stampare.
'''
def es30(n, sol=[], half1=0, half2=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append(1)
        es30(n,sol,half1+1,half2)
        sol.pop()
        sol.append(2)
        es30(n,sol,half1,half2)
        sol.pop()
        sol.append(3)
        es30(n,sol,half1+1,half2)
        sol.pop()
    else:
        if 2*n-len(sol)>half1-half2:
            sol.append(2)
            es30(n,sol,half1,half2)
            sol.pop()
        if half2<half1:
            sol.append(1)
            es30(n,sol,half1,half2+1)
            sol.pop()
            sol.append(3)
            es30(n,sol,half1,half2+1)
            sol.pop()

#es30(2)

'''
Progettare  un  algoritmo  che  data    una  stringa  lunga   sull’alfabeto   stampa tutte  le  stringhe  lunghe   sull’alfabeto   che  concordano  con  la  stringa  in esattamente una posizione.
'''
def es31(S, sol=[], u=False):
    if len(sol)==len(S):
        print(sol)
        return

    if not u and len(sol)==len(S)-1:
            sol.append(int(S[-1]))
            es31(S,sol,True)
            sol.pop()
    elif not u:
        sol.append(0)
        es31(S,sol,False if S[len(sol)-1]!='0' else True)
        sol.pop()
        sol.append(1)
        es31(S,sol,False if S[len(sol)-1]!='1' else True)
        sol.pop()
        sol.append(2)
        es31(S,sol,False if S[len(sol)-1]!='2' else True)
        sol.pop()
    else:
        if S[len(sol)]!='0':
            sol.append(0)
            es31(S,sol,u)
            sol.pop()
        if S[len(sol)]!='1':
            sol.append(1)
            es31(S,sol,u)
            sol.pop()
        if S[len(sol)]!='2':
            sol.append(2)
            es31(S,sol,u)
            sol.pop()
#es31('200')

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le stringhe lunghe n con simboli in {a, b} dove i blocchi di simboli
a di lunghezza massima che appaiono nella stringa hanno lunghezza
pari.
'''
def es32(n, sol=[],cons=0):
    if len(sol)==n:
        print(sol)
        return
    if cons%2==0:
        sol.append('b')
        es32(n,sol,0)
        sol.pop()
    if n-len(sol)>=2 or cons%2==1:
        sol.append('a')
        es32(n,sol,cons+1)
        sol.pop()
#es32(5)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le stringhe lunghe n con simboli in {a, b} che contengono un
numero dispari di simboli a ed un numero dispari di simboli b.
'''
def es33(n, sol=[], a=0, b=0):
    if len(sol)==n:
        print(sol)
        return
    if a%2==0 or (a%2==1 and n-len(sol)>1):
        sol.append('a')
        es33(n,sol,a+1,b)
        sol.pop()
    if b%2==0 or (b%2==1 and n-len(sol)>1):
        sol.append('b')
        es33(n,sol,a,b+1)
        sol.pop()
#es33(4)

'''
Dare lo pseudo-codice di un algoritmo che dato un intero n, stampa
tutte le stringhe palindromi lunghe 2n con valori in {a, b}.
'''
def es34(n,sol=[],i=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append('a')
        es34(n,sol,i+1)
        sol.pop()
        sol.append('b')
        es34(n,sol,i+1)
        sol.pop()
    elif sol[i-1]=='a':
        sol.append('a')
        es34(n,sol,i-1)
        sol.pop()
    elif sol[i-1]=='b':
        sol.append('b')
        es34(n,sol,i-1)
        sol.pop()
#es34(3)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le sequenze lunghe n formate da interi nell’insieme {1, 2, 3, 4}
con la propriet`a che nella sequenza numeri adiacenti distano almeno
2.
'''
def es35(n, sol=[]):
    if len(sol)==n:
        print(sol)
        return
    for i in range(1,5):
        if len(sol)==0 or abs(sol[-1]-i)>=2:
            sol.append(i)
            es35(n,sol)
            sol.pop()
#es35(3)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero pari n, stampa
tutte le permutazioni dei primi n interi in cui nell’ordinamento non
appaiono mai due pari consecutivi n`e due dispari consecutivi
'''
def es36(n,sol=[]):
    if len(sol)==n:
        print(sol)
        return
    for i in range(1,n+1):
        if len(sol)==0 or (sol[-1]%2!=i%2 and i not in sol):
            sol.append(i)
            es36(n,sol)
            sol.pop()
#es36(4)

'''
Progettare  un  algoritmo  che,  data  una  sequenza  decimaleSlungan, stampa le sottosequenze diSstrettamente crescenti.L’algoritmo proposto deve avere complessit`aO(nD(n)) doveD(n)`eilnumerodi sequenze da stampare.
'''
def es37(S,sol=[],i=0):
    if i==len(S):
        print(sol)
        return
    if len(sol)==0 or sol[-1]<S[i]:
        sol.append(S[i])
        es37(S,sol,i+1)
        sol.pop()
    es37(S,sol,i+1)

#es37([3,2,4,5,4])

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici ternarie n⇥n con la propriet`a che le righe e le colonne
della matrice risultano ordinate in modo crescente.
'''
def es38(n):
    sol=[[0]*n for _ in range(n)]
    es38_1(n, sol, 0, 0)

def es38_1(n, sol, i, j):
    if n==i:
        for x in sol:
            print(x)
        print()
        return

    if j==n-1:
        j1=0
        i1=i+1
    else:
        j1=j+1
        i1=i

    for k in range(1,4):
        if (i==0 or sol[i-1][j]<=k) and (j==0 or sol[i][j-1]<=k):
            sol[i][j]=k
            es38_1(n,sol,i1,j1)

#es38(2)

'''
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici binarie n ⇥ n con la propriet`a che nella matrice non
compaiono mai due uni adiacenti in orizzontale, in verticale o in di-
agonale.
'''
def es39(n):
    sol=[[0]*n for _ in range(n)]
    es39_1(n,sol,0,0)
    
def es39_1(n,sol,i,j):
    if i==n:
        for x in sol:
            print(x)
        print()
        return
    if j==n-1:
        j1=0
        i1=i+1
    else:
        j1=j+1
        i1=i

    if (j==0 or sol[i][j-1]!=1) and (i==0 or sol[i-1][j]!=1) and (i==j==0 or sol[i-1][j-1]!=1):
        sol[i][j]=1
        es39_1(n,sol,i1,j1)
    sol[i][j]=0
    es39_1(n,sol,i1,j1)
#es39(3)

'''
Progettare  un  algoritmo  che  dato  un  intero  n   stampa  tutte  le  matrici  binarie  quadrate 
n×n dove   il numero di zeri presenti in ciascuna colonna è minore o uguale   al numero di uni 
della colonna
'''
def es40(n):
    T=[[0]*n for _ in range(n)]
    es40_1(n,T,0,0,0,0)

def es40_1(n,sol,i,j,uni,zeri):
    if j==n:
        for x in sol:
            print(x)
        print()
        return
    if i==n-1:
        i1=0
        j1=j+1
    else:
        i1=i+1
        j1=j
    sol[i][j]=1
    if i1==0:
        es40_1(n,sol,i1,j1,0,0)
    else:
        es40_1(n,sol,i1,j1,uni+1,zeri)
    if zeri<uni or zeri+1<=n-i:
        sol[i][j]=0
        if i1==0:
            es40_1(n,sol,i1,j1,0,0)
        else:
            es40_1(n,sol,i1,j1,uni,zeri+1)
#es40(2)

'''
Progettare  un  algoritmo  che  data    una  stringa  lunga   sull’alfabeto   stampa tutte  le  stringhe  lunghe   sull’alfabeto   che  differiscono  da   in  ciascuna posizione e non hanno simboli adiacenti uguali.
'''
def es41(X, sol=[]):
    if len(X)==len(sol):
        print(sol)
        return
    for i in range(3):
        if (len(sol)==0 and X[0]!=str(i)) or (len(sol)>0 and i!=sol[-1] and str(i)!=X[len(sol)]):
            sol.append(i)
            es41(X,sol)
            sol.pop()
#es41('2001')

'''
Progettare un algoritmo che, dato un intero    , stampa tutte le matrici binarie con  la proprietà che nella riga , ,  della matrice sono presenti esattamente  uni. L'algoritmo proposto deve avere complessità  dove  è il numero di matrici  da  stampare
'''
def es42(n):
    sol=[[0]*n for _ in range(n)]
    es42_1(n,sol,0,0,0)

def es42_1(n,sol,i,j,uni):
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
    if n-j>i-uni:
        sol[i][j]=0
        if j1==0: es42_1(n,sol,i1,j1,0)
        else: es42_1(n,sol,i1,j1,uni)
    if uni<i:
        sol[i][j]=1
        if j1==0: es42_1(n,sol,i1,j1,0)
        else: es42_1(n,sol,i1,j1,uni+1)
#es42(3)

'''
Abbiamo una matriceMdi interi di dimensionen⇥nconn>1. Unadiscesasu questa matrice `e una sequenza dincelle della matrice con i seguenti vincoli•le celle appartengono a righe diverse della matrice•la prima cella appartiene alla prima riga della matrice•ogni altra cella `e adiacente (in verticale o in diagonale) alla cella che laprece
'''
def es43(M,sol=[],i=0,j=0):
    if len(sol)==len(M):
        print(sol)
        return
    if i==0:
        for k in range(len(M[0])):
            sol.append(M[0][k])
            es43(M,sol,i+1,k)
            sol.pop()
    else:
        for k in range(max(0,j-1),min(j+2, len(M))):
            sol.append(M[i][k])
            es43(M,sol,i+1,k)
            sol.pop()
M=[
    [12,10,3],
    [0,1,13],
    [8,9,17]
]
#es43(M)

'''
Progettare  un  algoritmo  che,  dato  un  intero ,  stampa  tutte  le  stringhe  binarie  di lunghezza     tali  che  il  numero  di  uni  presenti  nella  prima  metà  della  stringa  è  lo stesso del numero di uni presenti nella seconda metà.
'''
def es44(n,sol=[],f=0,s=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append(0)
        es44(n,sol,f,s)
        sol.pop()
        sol.append(1)
        es44(n,sol,f+1,s)
        sol.pop()
    else:
        if s<f:
            sol.append(1)
            es44(n,sol,f,s+1)
            sol.pop()
        if 2*n-len(sol)>f-s:
            sol.append(0)
            es44(n,sol,f,s)
            sol.pop()
#es44(2)

'''
Progettare  un  algoritmo  che,  data  una  sequenza  decimaleSlungan, stampa le sottosequenze diSstrettamente crescenti.L’algoritmo proposto deve avere complessit`aO(nD(n)) doveD(n)`eilnumerodi sequenze da stampare.
'''
def es45(S,sol=[],i=0):
    if i==len(S):
        if len(sol)>0:
            print(sol)
        return
    if len(sol)==0 or sol[-1]<S[i] :
        sol.append(S[i])
        es45(S,sol,i+1)
        sol.pop()
    es45(S,sol,i+1) 

#es45([3,2,4,5,4])

'''
Progettare un algoritmo che,  dato l’interon,  stampa tutte lesequenze  lunghensull’alfabeto  ternario{a,b,c}dove  il  simboloa`e  sempreseguito da almeno due simbolib.L’algoritmo proposto deve avere complessit`aO(nS(n)) doveS(n)`eilnumerodi sequenze da stampare.
'''
def es46(n,sol=[],s=0):
    if len(sol)==n:
        print(sol)
        return
    if len(sol)==0 or (sol[-1]!='a' and s==0):
        if n-len(sol)>2:
            sol.append('a')
            es46(n,sol,2)
            sol.pop()
        sol.append('c')
        es46(n,sol,s)
        sol.pop()
    sol.append('b')
    if s>0: es46(n,sol,s-1)
    else: es46(n,sol,s)
    sol.pop()
#es46(4)

'''
Progettare un algoritmo che, dati due  interi    e , stampa tutte le stringhe  binarie di lunghezza    in cui siano presenti almeno  zeri  consecutivi.
'''
def es47(n,k,sol=[],cons=0):
    if len(sol)==n:
        print(sol)
        return
    if n-len(sol)>k or cons>=k:
        sol.append(1)
        es47(n,k,sol,cons if cons>=k else 0)
        sol.pop()
    sol.append(0)
    es47(n,k,sol,cons+1)
    sol.pop()
#es47(4,2)

'''
Progettare  un  algoritmo  che  dati    tre  interi  positivi ,  e ,  con , stampa tutte le     stringhe ternarie lunghe  sull'alfabeto    dove il numero di occorrenze di  non  supera  ed il numero di occorrenze di  non supera L’algoritmo  proposto  deve  avere  complessità   dove  è il numero di stringhe da  stampare.
'''
def es48(n,m,k,sol=[],uni=0,due=0):
    if len(sol)==n:
        print(sol)
        return
    sol.append(0)
    es48(n,m,k,sol,uni,due)
    sol.pop()
    if uni<m:
        sol.append(1)
        es48(n,m,k,sol,uni+1,due)
        sol.pop()
    if due<k:
        sol.append(2)
        es48(n,m,k,sol,uni,due+1)
        sol.pop()
#es48(3,1,2)

'''
Vogliamo trovare le sequenze di lunghezzansull’alfabeto{0,1,2}in cui non appaiono cifre pari adiacenti. Progettare un algoritmo che prendecome parametro l’interone stampa tutte le sequenze cui siamo interessati.
'''
def es49(n,sol=[]):
    if len(sol)==n:
        print(sol)
        return
    sol.append(1)
    es49(n,sol)
    sol.pop()
    if len(sol)==0 or sol[-1]%2==1:
        sol.append(0)
        es49(n,sol)
        sol.pop()
        sol.append(2)
        es49(n,sol)
        sol.pop()
#es49(2)

'''
Progettare un algoritmo che, dato un interon, stampa tutte le stringhe binariedi lunghezza 2ntali che il numero di zeri presenti nella prima met`a della stringa`e inferiore o uguale al numero di uni presenti nella seconda met`a.L’algoritmo proposto deve avere complessit`aO(nS(n)) doveS(n)`eilnumerodi stringhe da stampare.
'''
def es50(n,sol=[],zeri=0,uni=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append(0)
        es50(n,sol,zeri+1,uni)
        sol.pop()
        sol.append(1)
        es50(n,sol,zeri,uni)
        sol.pop()
    else:
        if uni>zeri or 2*n-len(sol)>zeri-uni:
            sol.append(0)
            es50(n,sol,zeri,uni)
            sol.pop()
        sol.append(1)
        es50(n,sol,zeri,uni+1)
        sol.pop()
#es50(2)

'''
Progettare un algoritmo che, dato un intero , stampa tutte le stringhe  di lunghezza sull’alfabeto   tali  che  il  numero  di  cifre  dispari  presenti  nella  prima  metà  della stringa è lo stesso del numero di cifre dispari presenti nella seconda metà. 
'''
def es51(n,sol=[],d=0,p=0):
    if len(sol)==2*n:
        print(sol)
        return
    if len(sol)<n:
        sol.append(1)
        es51(n,sol,d+1,p)
        sol.pop()
        sol.append(2)
        es51(n,sol,d,p)
        sol.pop()
        sol.append(3)
        es51(n,sol,d+1,p)
        sol.pop()
    else:
        if p<d:
            sol.append(1)
            es51(n,sol,d,p+1)
            sol.pop()
            sol.append(3)
            es51(n,sol,d,p+1)
            sol.pop()
        if 2*n-len(sol)>d-p:
            sol.append(2)
            es51(n,sol,d,p)
            sol.pop()
#es51(2)

'''
Progettare  un  algoritmo  che  data    una  stringa  lunga   sull’alfabeto   stampa tutte  le  stringhe  lunghe   sull’alfabeto   che  concordano  con  la  stringa  in esattamente una posizione.
'''
def es52(X,sol=[],s=False):
    if len(X)==len(sol):
        print(sol)
        return

    for i in range(3):
        if s==False and len(sol)==len(X)-1 and X[-1]!=str(i):
            continue
        if s==False:
            sol.append(i)
            if X[len(sol)-1]==str(i): es52(X,sol,True)
            else: es52(X,sol,s)
            sol.pop()
        elif X[len(sol)]!=str(i):
            sol.append(i)
            es52(X,sol,s)
            sol.pop()
#es52('200')
