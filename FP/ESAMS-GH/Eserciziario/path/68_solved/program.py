"""
Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es68(dir, estensioni),
che deve contare quanti file di certi tipi si trovano in una directory o in una delle sue sottodirectories,
e che riceve come argomenti
    dir: il path della directory in cui cercare
    estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
La funzione deve tornare un dizionario che ha come chiavi le estensioni passate come argomento
e come valori il numero di file il cui nome termina in quel modo, solo se > 0
(ovvero, se nessun file con una data estensione appare nella directory o nelle sottodirectories
la chiave non deve apparire nel dizionario tornato dalla funzione).

Tests: date alcune directory contenenti file di tipo (ext) diverso, si chiama la funzione per contare alcuni dei tipi di file nelle diverse directory
Test: che la funzione sia ricorsiva
"""

import os


def es68(directory, estensioni):
    ext = {}
    for ls in os.listdir(directory):
        path = f'{directory}/{ls}'
        
        if os.path.isfile(path) and path[-3:] in estensioni:
            ext[path[-3:]] = ext.get(path[-3:], 0) + 1
        elif os.path.isdir(path):
            p = es68(path, estensioni)
            for k, v in p.items():
                ext[k] = ext.get(k, 0) + v
            
    return ext
    
print(es68('t1', ['txt', 'jpg']))