def es3(ins1, ins2):
    '''
    progettare la funzione es3(ins1, ins2) che:
    - riceve  in input due insiemi  di numeri naturali
    - trova le terne (a,b,c) con a,b e c in insi1 con la proprieta' che a<b<c e a+b+c e' in insi2
    - restituisce l'insieme di tutte le triple trovate.
    Nella lista restituita le triple devono essere  rappresentate tramite tuple e le
    varie tuple devono comparire nella lista per somma di componenti crescenti e in caso di parita'
    in ordine lessicografico crescente.
    ESEMPIO:
    se ins1={ 2,4,5,6,8,9} e ins2={5,15,19,25} la funzione restituisce la lista
    [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
    ''' 
    
    ins1 = list(ins1)
    rez = []
    for i in range(len(ins1)):
        for j in range(len(ins1)):
            for p in range(len(ins1)):
                p = (ins1[i], ins1[j], ins1[p])
                if p[0]<p[1]<p[2] and sum(p) in ins2:
                    rez.append(p)
    return sorted(rez, key=lambda x: (sum(x), x))
print(es3({ 2,4,5,6,8,9}, {5,15,19,25}))
#print(es3({ 1,2,4,5,6,8,9}, {16,18}))
