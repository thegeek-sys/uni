'''
Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva)  
es76(parola), che presa in input una stringa di caratteri  parola restituisce la lista dei 
suffissi di parola. Gli elementi della lista devono risultare ordinati per lunghezza decrescente .
Si ricorda che un suffisso di una parola e' quello che si ottiene concellando 0 o piu' 
caratteri iniziali della parola.
Ad esempio per es76("fondamenti") la lista restituita sara'
['fondamenti', 'ondamenti', 'ndamenti', 'damenti', 'amenti', 'menti', 'enti', 'nti', 'ti', 'i']
'''

def es76(parola):
    rez = []
    if len(parola) == 1:
        rez.append(parola)
    else:
        p = es76(parola[1:])
        rez = rez + [parola] + p
    return rez
        
print(es76("fondamenti"))