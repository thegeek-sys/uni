"""
Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es71(dir, minimo, massimo)
che cerca nella directory dir  i files che hanno una dimensione compresa tra minimo e massimo (inclusi).
La funzione deve tornare un dizionario che contiene come chiavi i nomi dei files individuati (senza path),
e come valori le corrispondenti profondita' (contando la directory 'dir' iniziale come profondita' 0)
Nel caso in cui un nome di file sia presente a profondita' diverse, il dizionario deve contenere quella maggiore.
Nota: per individuare la dimensione del file potete usare la funzione os.stat

Test:   date alcune directory contenenti files di dimensioni varie a varie profondita',
        controllare che il risultato sia il dizionario corretto
Test:   che la funzione sia ricorsiva
"""

import os

def es71(directory, minimo, massimo, l=0):
    rez = {}
    
    for ls in os.listdir(directory):
        if ls.startswith('.'):
            continue
        
        path = f'{directory}/{ls}'
        
        if os.path.isfile(path) and (minimo <= os.path.getsize(path) <= massimo):
            rez[ls] = l
        elif os.path.isdir(path):
            p = es71(path, minimo, massimo, l+1)
            for k, v in p.items():
                rez[k] = max(rez.get(k, 0), v)
    return rez

print(es71('t4', 0, 100))