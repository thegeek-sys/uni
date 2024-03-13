'''
Si definisca la funzione es25(n) che calcola la riga i-esima del triangolo di Tartaglia,
ovvero la lista dei coefficienti della potenza i-esima del binomio (a+b).

Si ricorda la definizione del triangolo di Tartaglia:
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   ...........
Tartaglia(0) = [1]   # caso base
I numeri che appaiono in ciascuna riga del triangolo di Tartaglia si ottengono
come somma di quelli sovrastanti nella riga precedente.
Dove non troviamo una cifra consideriamo che si trovi un valore 0 (zero)
'''

def aux(n):
    rez = []
    if n == 1:
        return [1]
    # else:
    for i in range(n):
        # print([aux(n-1)*i])
        rez = rez + [sum(aux(n-1)[i],aux(n-1)[i-1])]
    
    return rez
        
        
print(aux(2))

def es25(n):
    
    pass
