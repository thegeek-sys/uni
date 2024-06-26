def es21(matrice):
    '''
    es21(matrice) presa la matrice di caratteri rappresentata tramite una lista di liste di caratteri, 
    la restituisce dopo averne ordinato le colonne in ordine lessicografico. 
    La matrice passata in input al termine della funzione non deve risultare modificata.  
    Ad esempio se la matrice di input e'
     [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] 
    la funzione restituira' la matrice:
     [['a','a','g','f'],
      ['b','b','m','g'],
      ['q','s','n','z']]     
    '''
    # M = [sorted([matrice[y][x] for y in range(len(matrice))]) for x in range(len(matrice[0]))]
    # return [[M[y][x] for y in range(len(M))] for x in range(len(M[0]))]

    # return [[[sorted([matrice[y][x] for y in range(len(matrice))]) for x in range(len(matrice[0]))][y][x] for y in range(len([sorted([matrice[y][x] for y in range(len(matrice))]) for x in range(len(matrice[0]))]))] for x in range(len([sorted([matrice[y][x] for y in range(len(matrice))]) for x in range(len(matrice[0]))][0]))]

    return [[[sorted([matrice[y][x] for y in range(len(matrice))]) for x in range(len(matrice[0]))][y][x] for y in range(len(matrice[0]))] for x in range(len(matrice))]

print(es21([['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] ))