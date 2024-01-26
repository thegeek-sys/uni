"""
ATTENZIONE: e' VIETATO usare la funzione os.walk o altre funzioni di libreria che 
permettono di cercare tutti i file presenti in una directory. 
(la directory la dovete esplorare voi)

Si definisca la funzione ricorsiva (o che fa uso di vostre funzioni ricorsive) es67 che:
- riceve come argomento un path del filesystem
- esplora ricorsivamente la directory corrispondente e torna un dizionario.

NOTA: tutti i file e directory che iniziano con '.' vanno ignorati.

Il dizionario ha come chiave le estensioni dei file trovati nella directory 
(ovvero gli ultimi 3 caratteri del nome dei file, es: 'txt', 'pdf', 'png').
Il valore associato a ciascuna chiave K e' la distanza (differenza delle profondita')
tra il piu' profondo file che ha quella estensione e il meno profondo.
Assumete che i file contenuti nella directory path siano a profondita' 0.
Esempio:
se nella directory con path='A1' sono presenti i soli due file di tipo 'txt'
    A1/a/b/c/d/e/f/g/h/pippo.txt    a profondita' 8    (contando A1 = 0)
    A1/d/f/pappo.txt                a profondita' 2
    risultato contiene la coppia chiave: valore
    'txt' : 6
"""

import os

def aux(directory, l=0):
    depth = {}
    for ls in os.listdir(directory):
        path = f'{directory}/{ls}'
        
        if os.path.basename(path)[0] == '.':
            continue
        
        if os.path.isfile(path):
            depth[path[-3:]] = depth.get(path[-3:], []) + [l]
        else:
            p = aux(path, l+1)
            for k, v in p.items():
                depth[k] = depth.get(k, []) + v
    
    return depth




def es67(path):
    rez = aux(path)
    for k, v in rez.items():
        rez[k] = max(v)-min(v)
    
    return rez


a = es67('A1')
print(a)
exp = {'www': 4, 'sss': 3, 'nnn': 2, 'uuu': 2, 'zzz': 0, 'txt': 2, 'jjj': 0, 'aaa': 0, 'ppp': 1, 'ooo': 0, 'ccc': 0, 'vvv': 1, 'xxx': 1, 'iii': 2, 'bbb': 1, 'ggg': 2, 'png': 0, 'ttt': 3, 'hhh': 3, 'kkk': 5, 'fff': 0, 'mmm': 0, 'rtf': 0, 'qqq': 0, 'doc': 0, 'ddd': 0}
assert exp == a






