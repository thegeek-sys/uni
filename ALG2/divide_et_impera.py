'''
Progettare un algoritmo che, preso un vettore ordinato V di n interi distinti,
determini se esiste un indice i tale che V[i] = i in O(log n) tempo.
'''
def es1(V):
    sx = 0
    dx = len(V)-1
    while sx<=dx:
        m = (sx+dx)//2
        if V[m]==m:
            return True
        if V[m]>m:
            dx=m-1
        elif V[m]<m:
            sx=m=1
    return False
    
V = [0, 2, 3, 4, 5]
#print(es1(V))

'''
Sia V un vettore di n interi. Si dice che V è continuo se per ogni i = 1, 2,...,n
1, |V[i+1]-V[i]| <= 1. Si dice zero del vettore un indice k tale che V[k]=0
Progettare un algoritmo che, dato un vettore V di n
2 interi continuo e tale che V[1]<0 e V[n]>0,
trovi uno zero in O(log n) tempo.
'''
def es2(V):
    sx = 0
    dx = len(V)-1
    while sx<=dx:
        m = (sx+dx)//2
        if V[m]==0:
            return m
        if V[m]<0:
            sx=m+1
        else:
            dx=m-1
    return None

V = [-2, -1, 0, -1, 1, 2]
#print(es2(V))

'''
Sia A un array ordinato di n interi
dove ogni valore in A occorre esattamente due volte tranne uno. Progettare
un algoritmo di tempo O(log n) che trovi l’elemento non doppione in A.
'''
def es3(V, c=True):
    sx=0
    dx=len(V)-1
    c=True
    while dx-sx>2:
        m=(sx+dx)//2
        if V[m]==V[m+1]:
            if c:
                dx=m+1
            else:
                sx=m
        else:
            if c:
                dx=m+1
            else:
                sx=m
        c=not c
    return sx+1

V=[0,0,1,1,2,3,3,4,4,5,5]
#print(es3(V))

'''
Dato un array A di n elementi, un indice i al suo interno è
detto ”pozzo” se si verifica che A[1]>...>A[i]<...<A[n].
Progettare un algoritmo di complessità O(log n) che, assumendo la sua
esistenza, trovi il pozzo di un array.
'''
def es4(V):
    sx=0
    dx=len(V)-1
    while sx<dx:
        m=(sx+dx)//2
        if V[m]>V[m+1]:
            sx=m+1
        elif V[m]>V[m-1]:
            dx=m
        else:
            return m

V=[2,1,0,1,2]
print(es4(V))

