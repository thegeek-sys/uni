#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame e' necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "Flavio"
cognome    = "Sperandeo"
matricola  = "2108912"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(a_dict, word) che prende in ingresso un
dizionario 'a_dict' e una parola 'word'. Ogni chiave del dizionario è
una stringa che ha una lista di stringhe come valore. La funzione deve
rimuovere dal dizionario tutte quelle chiavi associate ad una lista
che contiene una stringa 'word'.  La funzione restituisce il numero di
chiavi rimosse dal dizionario 'a_dict'.

Esempio: se a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
  l'invocazione di func1(a_dict, 'b') deve restituire 2 e
  a_dict deve risultare modificato in {'c': ['a', 'c']}.
  In quanto: e' rimossa la chiave 'a' perche' la lista ['a','b','c']
  contiene 'b' come word; e' inoltre rimossa la chiave 'b' perche' la lista
  ['a','b'] contiene 'b' come word.
'''
def func1(a_dict, word):
    to_remove = []
    removed = []
    for k, v in a_dict.items():
        if word in v:
            to_remove.append(k)
    
    for x in to_remove:
        removed.append(a_dict.pop(x))

    return len(removed)
        


# a = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
# print(func1(a, 'b'))
# print(a)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(a_string) che prende in ingresso una
stringa 'a_string' e restituisce un'altra stringa. La nuova stringa ha
tutte le lettere della stringa in input ripetute una volta sola e in
ordine alfabetico inverso.

Esempio: se a_string='welcome' l'invocazione di func2(a_string) dovrà
         restituire la stringa 'womlec'
'''

def func2(a_string):
    sstr = set(a_string)
    return ''.join(sorted(sstr, reverse=True))

# print(func2('welcome'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe con lo stesso numero di elementi e
restituisce una nuova lista composta dalle stringhe ottenute
concatenando:
 - la prima stringa della prima lista con l'ultima stringa della
   seconda lista,
 - la seconda stringa della prima lista con la penultima della seconda
   lista,
 - e così via.
La lista risultante deve essere ordinata per numero di caratteri
crescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['so', 'sin', 'vas', 'rin', 'vul']  e
            string_list2=['cane', 'casai', 'to', 'cero', 'sia']
         l'invocazione di func3(string_list1, string_list2) dovrà restituire
         la lista ['sosia','vasto','sincero','vulcane','rincasai']
'''


def func3(string_list1, string_list2):
    rez = []
    l = len(string_list1)-1
    for i in range(len(string_list1)):
        rez.append(string_list1[i]+string_list2[l])
        l -= 1
    
    return sorted(rez, key = lambda x: (len(x), x))


# string_list1=['so', 'sin', 'vas', 'rin', 'vul']
# string_list2=['cane', 'casai', 'to', 'cero', 'sia']
# print(func3(string_list1, string_list2))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti

Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.  All'interno del file indicato da 'input_file'
sono presenti su una sola riga una serie di parole (composte da
caratteri alfabetici) separate da virgole, spazi, punti e virgole e da
punti.
La funzione deve individuare tutte le parole contenute nel file
indicate da 'input_file' e scriverle all'interno di un nuovo file
indicato da 'output_file'.  Le parole devono essere scritte
all'interno del file su una sola riga terminata dal carattere di
a capo, separate da uno spazio e con il seguente ordine:
    - numero di caratteri crescente,
    - in caso di parità, in ordine alfabetico, indipendentemente da
      maiuscole e minuscole
    - in caso di parole identiche, in ordine lessicografico.
La funzione deve restituire il numero di parole scritte nel file in
output.

Esempio: se il contenuto del file 'input_file' è il seguente
Dog,cat,dog;Cat.bird car

l'invocazione di func4('input_file', 'output_file') dovrà scrivere nel
file 'output_file' la seguente riga
car Cat cat Dog dog bird

e ritornare il valore 6.
"""


def func4(input_file, output_file):
    with open(input_file, mode='rt') as fr:
        fr = fr.read()
        for x in fr:
            if not x.isalpha():
                fr = fr.replace(x, ' ')
        rez = fr.split()
    rez = sorted(rez, key = lambda x: (len(x), x.lower(), x))
    with open(output_file, mode='wt') as fw:
        fw.write(' '.join(rez))
    return len(rez)

# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
# print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene una serie di punti
diversi bianchi su uno sfondo nero. La funzione deve individuare tutti
i rettangoli definiti da quattro pixel bianchi che possono essere
considerati gli spigoli di tali rettangoli (si veda l'esempio più avanti).

Si può assumere che:
    - ogni riga ha al più due punti bianchi e
    - ogni colonna ha al più due punti bianchi.

La funzione deve ritornare una lista contenente l'area di tutti i rettangoli
individuati nell'immagine, ordinati per dimensione crescente.

Esempio: nell'immagine del file func5/image01.png ci sono gli spigoli del
         rettangolo (5,5), (45,5), (5,25), (45,25) con area 861
         e del rettangolo (10,10), (20,10), (10,20), (20,20) con area 121
         e c'è un pixel in (31, 15), per cui l'invocazione di
         func5('func5/image01.png') deve restituire la lista [121, 861].
         Gli spigoli riportati sopra sono nel formato:
         top-left, top-right, bottom-left, bottom-right.
         Le coordinate sono (x,y).
"""
import images

def find_rect(img, x, y, w, h, white=(255,255,255)):
    for x1 in range(x+1, w):
        if img[y][x1] == white:
            break
    else:
        return False
    
    for y1 in range(y+1, h):
        if img[y1][x] == white:
            break
    else:
        return False
    
    if img[y1][x1] == white:
        img[y][x] = img[y1][x] = img[y][x1] = img[y1][x1] = (0,)*3
        return (x1-x+1)*(y1-y+1)
    else:
        return False


def func5(input_pngfile):
    img = images.load(input_pngfile)
    rez = []
    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] == (255,255,255):
                rect = find_rect(img, col, row, len(img[0]), len(img))
                if rect:
                    rez.append(rect)
                
                    
    return sorted(rez)

                
        

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.
La funzione deve explorare ricorsivamente l'albero delle directory con
radice in 'directory' e restituire un dizionario.
Le chiavi del dizionario sono i percorsi delle sotto-directory di
'directory', sottoforma di stringa.
Il valore della chiave di una directory è un set di stringhe con i nomi
di quei file '.txt' presenti in 'directory' per i quali il primo carattere
del contenuto del file è uguale all'ultimo.
Se una directory non contiene nessun file .txt con tale caratteristica,
allora quella directory non appare nel dizionario.

Esempio: se la funzione è chiamata su 'ex1/A', ritorna:

{'ex1/A/B': {'b.txt'}, 'ex1/A/C': {'c.txt'}}

poiché ex1/A/B/b.txt e ex1/A/C/c.txt sono gli unici file in cui
il primo carattere del contenuto è uguale all'ultimo ('k' per il primo,
'a' per il secondo).

NOTA: è proibito usare la funzione os.walk. Si possono usare:
  os.listdir, os.path.isfile, os.path.exists, etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.
"""

import os

def aux_1(root):
    rez = []
    for ls in os.listdir(root):
        path = f'{root}/{ls}'
        
        if path.endswith('.txt'):
            with open(path, mode='rt') as fr:
                fr = fr.read()
                if fr[0] == fr[-1]:
                    rez.append(path)
        elif os.path.isdir(path):
            p = aux_1(path)
            rez = rez+p
    return rez

def ex1(root):
    rez = {}
    files = aux_1(root)
    for file in files:
        rez[os.path.dirname(file)] = rez.get(os.path.dirname(file), set()) | {os.path.basename(file)}

    return rez

print(ex1('ex1/A'))
# print(ex1('ex1/B'))
# print(ex1('ex1'))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) ricorsiva (o che al suo interno
usa una funzione ricorsiva) che riceve in ingresso la radice di
un albero binario, come definito nella classe `BinaryTree` del modulo
tree.py.  L'albero in ingresso ha delle stringhe come valori. La
funzione deve restituire la stringa risultante dalla concatenazione di
tutti i valori associati ai nodi dell'albero con la seguente regola:
  - la concatenazione avviene con l'ordine LNR se il nodo si trova
    in un livello pari
  - con l'ordine RNL se il nodo è in un livello dispari
dove L è il sottoalbero sinistro, N il nodo e R il sottoalbero destro.
La radice si assume a livello 0.

Esempio:

        ______A______                        ______A______
       |             |                      |             |
       B__        ___C___                __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F             _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                                      H   I      J  K   L   M   N

  Se l'albero è quello di sinistra, la funzione deve restituire
  la stringa 'DBAFCE'.

  Se l'albero è quello di destra, la funzione deve restituire la
  stringa 'EJBHDIAMGNCKFL'
  """

def ex2(root, l=0):
    rez = ''
    
    R, L = '', ''
    
    if l%2==0:
        N = root.value
        if root.left:
            L = ex2(root.left, l+1)
        if root.right:
            R = ex2(root.right, l+1)
        
        rez += L + N + R
    else:
        N = root.value
        if root.left:
            L = ex2(root.left, l+1)
        if root.right:
            R = ex2(root.right, l+1)
        
        rez += R + N + L
    return rez


# from tree import BinaryTree
# root = BinaryTree.fromList(['A', ['B',None,['D',None,None]], ['C', ['E',None,None], ['F',None,None]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',None,None],['I',None,None]],['E',None,['J',None,None]]], ['C', ['F',['K',None,None],['L',None,None]], ['G',['M',None,None],['N',None,None]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',['L',None,None],None],None],['E',None,['I',None,None]]],['C', ['F',['J',None,None],None],['G',None,['K',None,['M',None,None]]]]])
# print(ex2(root))
###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
