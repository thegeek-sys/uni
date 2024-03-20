'''
ATTENZIONE: usate come separatore dei file il carattere "/" che funziona sia in Windows che in Linux
ATTENZIONE: e' VIETATO usare la funzione os.walk

Si definisca la funzione  es80(dir1, parole), che presi in input:
    dir1:   il path di una directory
    parole: un insieme di parole (stringhe di caratteri tra 'a' e 'z')
esegue il seguente lavoro:
Ricerca nella directory il cui path e'  dir1 e nelle sue subdirectories eventuali file con estensione .txt contenenti
stringhe appartenenti all'insieme delle parole e restituisce un dizionario delle parole trovate.
Nel dizionario restituito devono comparire  solo le parole effettivamente riscontrate all'interno
dei file con estensione .txt e ciascuna chiave deve avere  come attributo una lista  di due interi.
Il primo elemento della lista riporta il numero complessivo di volte che la parola  e' stata ritrovata in questi file,
il secondo elemento della lista riporta la profondita' massima dei file in cui la parola e' risultata presente.
La profondita' dei file nella directory dir1 vale 0
Per parola intendiamo una sequenza di lunghezza massimale di caratteri tra 'a' e 'z'.
Si puo' assumere che tutti i file con estensione .txt contengono solo parole  separate da  spazi, tab o andate a capo.
(non sono presenti caratteri maiuscoli o segni di interpunzione)
'''

import os

def es80(dir1, parole, l=0):
    rez = {}
    for ls in os.listdir(dir1):
        path = f'{dir1}/{ls}'
        if path.endswith('.txt'):
            with open(path, mode='rt') as fr:
                fr = fr.read().split()
                for parola in parole:
                    if parola in fr:
                        rez[parola] = [rez.get(parola, [0,0])[0] + fr.count(parola), max(rez.get(parola, [0,0])[1], l)]
        elif os.path.isdir(path):
            p = es80(path, parole, l+1)
            for k, v in p.items():
                rez[k] = [rez.get(k, [0,0])[0] + v[0], max(rez.get(k, [0,0])[1], v[1])]
    return rez

