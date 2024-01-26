

'''
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''

import os

def aux(pathDir, lastDir):
    rez = []
    for sub in os.listdir(pathDir):
        path = f'{pathDir}/{sub}'
        
        if os.path.isfile(path) and (path.endswith('.txt') or path.split('/')[-1][0] == '.'):
            rez.append(path)
        elif os.path.isdir(path):
            path = aux(path, lastDir)
            rez = rez + path
    return rez

def es9(pathDir):
    rez = {}
    out = []
    ls = aux(pathDir, pathDir.split('/')[-1])
    for x in ls:
        dire = x.split('/')[-2]
        rez[dire] = rez.get(dire, 0) + os.path.getsize(x)
        
    for k, v in rez.items():
        out.append((k,v))
    return sorted(out, key = lambda x: (-x[1], x[0]))
    
print(es9('Informatica/Software'))
                
    
        
