'''
Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva)  
es78(parola), che presa in input una stringa di caratteri  parola restituisce la lista delle  
diverse "sottoparole crescenti"  di parola. Le sottoparole devono comparire nella lista in ordine lessicografico.
Si ricorda che una sottoparola e' quello che si ottiene da una parola concellandone 0 o piu'
caratteri (in testa, in coda o nel mezzo).
Inoltre una sottoparola si dice crescente se i caratteri che la compongono
letti da sinistra  a destra risultano ordinati lessicograficamente.

Ad esempio  la lista restituita da es78('zanzara') sara'
['a', 'aa', 'aaa', 'aar', 'an', 'anr', 'anz', 'ar', 'az', 'n', 'nr', 'nz', 'r', 'z', 'zz']
'''

def aux(cur, parola, num, fin, l=1):
    rez = []
    
    if num == l:
        # return cur
        rez.extend(cur)
    else:
        # rez = rez + cur
        for i in cur:
            # rez.add(i)
            for j in range(len(parola)):
                p = i+parola[j]
                
                if all([p.count(x) <= fin.count(x) for x in p]):
                # if all([[p.count(x) for x in set(p)] <= ['zanzara'.count(x) for x in set('zanzara')]]):
                # if ()
                    if p == ''.join(sorted(p)):
                        cur = [i+parola[j]] + cur
                        p = aux(cur, parola[j:], num, fin, l+1)
                        rez = rez+p
        
    return rez



def es78(parola):
    rez = []
    for i in range(len(parola)-1):
        p = aux([parola[i]], parola[i+1:], len(parola[i+1:]), parola)
        rez = rez + p
    print(rez)
    return sorted(set(rez))


print(es78('zanzara'))
