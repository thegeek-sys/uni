"""
Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es69(dir, profondita, estensioni),
che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
solo se si trovano alla profondita' indicata, e che riceve come argomenti:
    dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
    profondita: la profondita' in cui dobbiamo cancellare i file, contando da 0 per la directory radice passata come argomento
    estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
La funzione deve tornare il numero totale di files presenti nelle directories di profondita' minore o uguali a 'profondita',
che NON sono stati cancellati

NOTA: ignorate tutti i file e directory che iniziano con '.'

NOTA: per eliminare un file usate la funzione os.remove

Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', si chiama la funzione e si controlla che i file contenuti nelle directories esistano/non esistano a seconda del caso (senza usare una soluzione ricorsiva ma testando direttamente i path dei files relativi alla dir iniziale)
Test: che la funzione sia ricorsiva
"""

import os


def es69(directory, profondita, estensioni, l=0):
    n = 0
    for ls in os.listdir(directory):
        if ls[0] == '.':
            continue
        
        path = f'{directory}/{ls}'
        
        if os.path.isfile(path) and path[-3:] in estensioni and profondita == l:
            os.remove(path)
            # a.append(path)
        elif os.path.isfile(path) and l <= profondita:
            n+=1
        elif os.path.isdir(path):
            n += es69(path, profondita, estensioni, l+1)
    return n

# print(es69('t2 copia', 3, ['jpg', 'png']))
