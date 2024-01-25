    
def es5(insieme,k):
    '''
    Es 11: 6 punti
    Si definisca la funzione es5(insieme, k) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti un insieme di stringhe  ed un intero k>0 
    - trova le diverse stringhe che si possono ottenere concatenando k copie delle stringhe 
    originali (una stessa stringa puo' essere utilizzata  piu' volte nelle concatenazioni). 
    - torna come risultato l'insieme delle stringhe trovate.
    Esempi: sia insieme={'a','bb','c'}
    1)  es5(insieme, 1) restituisce l'insieme {'a','bb','c'}
    2)  es5(insieme, 2) restituisce l'insieme {'aa','abb','ac','bba','bbbb','bbc','ca','cbb','cc' }
    3)  es5(insieme, 3) restituisce l'insieme
    {'bbca', 'bbbbbb', 'ccc', 'cca', 'caa', 'ccbb', 'bbaa', 'abbc', 'aac', 'abbbb', 'acbb', 'cbbc', 
    'bbbba', 'bbabb', 'cbba', 'cac', 'bbac', 'acc', 'aabb', 'aca', 'bbbbc', 'aaa', 'cbbbb', 'abba', 
    'bbcbb', 'cabb', 'bbcc}

    SUGGERIMENTO: potete simulare il ciclo su k con la ricorsione
    '''
    
    out = set()
    for x in insieme:
        part = aux_es5({x}, insieme, k)
        out = out | part
    return out


def aux_es5(let, insieme, k, l=1):
    rez = set()
    if l==k:
        return let
    else:
        for i in let:
            for j in insieme:
                rez.add(i+j)
        rez = aux_es5(rez, insieme, k, l+1)
            
    return rez

print(es5({'a','bb','c'}, 3))


