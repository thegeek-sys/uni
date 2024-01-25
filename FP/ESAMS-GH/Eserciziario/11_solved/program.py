'''
    Es 11: 3 punti
progettare la funzione es11(ftesto) che, preso in input 
l'indirizzo di un file di testo restituisce un dizionario avente per chiavi delle stringhe 
ed attributo liste di  stringhe.
Il file di testo contiene stringhe distinte di caratteri, si guardi 
ad esempio il file f9.txt. 
Le chiavi del dizionario si ottengono dalle stringhe presenti nel file dopo aver 
eliminato da queste le vocali ed aver riordinato lessicograficamente i caratteri rimanenti 
(ad esempio dalla stringa 'angelo' si ottine la chiave 'gln').
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata. 
Nota che  stringhe diverse possono generare una stessa chiave come nel caso 
di  'casa', 'caso' e 'cose'
Le stringhe nella lista devono comparire  ordinate per lunghezza decrescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f10.txt  la funzione restituisce  il dizionario:
{'prt': ['parto', 'porta'], 
'r': ['era', 'ora'], 
'pr': ['arpia', 'arpa'], 
'cs': ['casa', 'cosa'], 
'fll': ['follia', 'fallo', 'folla'], 
'rt': ['otre', 'tre'], 
'lp': ['piolo', 'polo']
}
'''

def es11(ftesto):
    rez = {}
    vowels = ['a','e','i', 'o', 'u']
    with open(ftesto, mode='rt') as fr:
        for line in fr:
            line = line.strip()
            if line != '':
                cons = line
                for vowel in vowels:
                    cons = cons.replace(vowel, '')
                cons = ''.join(sorted(cons, key = lambda x: x))
                rez[cons] = rez.get(cons, [])+[line]
    for k, v in rez.items():
        rez[k] = sorted(v, key = lambda x: (-len(x), x))
    return rez
    
print(es11('ft10a.txt'))
