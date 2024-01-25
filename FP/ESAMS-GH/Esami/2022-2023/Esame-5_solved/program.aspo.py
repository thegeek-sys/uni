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

nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(list_a, list_b, list_c) che prende in ingresso
tre liste che contengono delle stringhe. La funziona restituisce tutte le
stringhe che sono presenti in tutte e tre le liste, senza ripetizioni.
La lista risultante deve essere ordinata in ordine alfabetico.

Esempio:
    list_a = ['pippo', 'pluto', 'minnie', 'minnie','pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pippo', 'pluto', 'gastone', 'pippo', 'analecto','minnie']
sia 'minnie' che 'pippo' sono in tutti e tre le lista quindi si torna
in ordine alfabetico ['minnie', 'pippo'].
'''

def func1(list_a, list_b, list_c):
    return sorted(set(list_a).intersection(set(list_b)).intersection(set(list_c)))

# list_a = ['pippo', 'pluto', 'minnie', 'minnie','pippo']
# list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
# list_c = ['pippo', 'pluto', 'gastone', 'pippo', 'analecto','minnie']
# print(func1(list_a, list_b, list_c))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(d1, d2) che prende in ingresso due dizionari
d1 e d2 e ritorna un nuovo dizionario d3. d1 e d2 hanno come chiave stringhe
e come valori liste di interi. d3 deve contenere solo le chiavi che sono in d1
e d2. Data una chiave presente in d1 e d2, il nuovo valore associato a quella
chiave e' la concatenazione della lista presa da d1 con la lista presa da d2.

Ad esempio:
    d1 = {'pippo': [5, 2,],
          'pluto': [1, 2, 3],
          'gastone': [50, 50 ]}

    d2 = {'gastone': [5, 23, 2],
          'paperino': [3, 2, 1],
          'pluto': [10, -1]}

    expected = {'gastone': [50, 50, 5, 23, 2], 'pluto': [1, 2, 3, 10, -1]}
'''

def func2(d1, d2):

    return {k:d1[k]+d2[k] for k in d1.keys() if k in d2}


# d1 = {'pippo': [5, 2,],
#       'pluto': [1, 2, 3],
#       'gastone': [50, 50 ]}

# d2 = {'gastone': [5, 23, 2],
#       'paperino': [3, 2, 1],
#       'pluto': [10, -1]}

# print(func2(d1,d2))

# d1 = {'pippo': [5, 23, 2, 3, 5],
#       'pluto': [1, 2, 3],
#       'gastone': [50, ]*7}

# d2 = {'paperoga': [5, 23, 2, 3, 5],
#       'topolino': [3, 2, 1],
#       'minnie': [10, 10, -1]}



# print(func2(d1,d2))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe con lo stesso numero di stringhe.
Due stringhe prese a coppie da string_list1 e string_list2 hanno sempre
la stessa lunghezza.

Esempio: se  string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
             string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

'sIN' ha la stessa lunghezza di 'cas', 'VUL' ha la stessa lunghezza di 'sia'.

Si restituisca una nuova lista che trasforma la lista string_list2 con le
seguenti regole:
 - il case dei caratteri della stringa della lista string_list1 serve
   come guida per impostare il case dei caratteri della stringa della lista
   string_list2
- in particolare se un carattere della stringa della lista string_list1
  e' lowercase allora il nuovo carattere da creare dovra' essere preso dal
  carattere corrispondente della stringa della lista string_list2 ma reso
  lowercase.
- viceversa, se un carattere della stringa della lista string_list1
  e' UPPERCASE allora il nuovo carattere da creare dovra' essere preso dal
  carattere corrispondente della stringa della lista string_list2 ma reso
  UPPERCASE.
- Nel caso un carattere non sia ne lowercase ne UPPERCASE si lascia invariato
- Le liste possono contenere stringhe vuote.

La lista finale va ordinata in ordine decrescente in base alla lunghezza
delle stringhe, in caso di parità, in ordine alfabetico.

Esempio: Dato l'input di prima, l'invocazione di func3(string_list1, string_list2)
         dovrà restituire la lista ['cE', 'SIA', 'TOO', 'cAs', 'ceo']

Ad esempio 'ce' --> 'cE' perche 'sO' ha la 's' miniuscola e 'O' maiuscola.

NOTA: si usino le funzioni delle stringhe isupper(), lower() etc.
'''


def func3(string_list1, string_list2):
    res = []
    for c, l in zip(string_list1, string_list2):
        s = ''
        for i, k in enumerate(c):
            if k.isupper():
                s+=l[i].upper()
            elif k.islower():
                s+=l[i].lower()
            else:
                s+=l[i]
        res.append(s)
    return sorted(res, key = lambda x: (-len(x), x))

# string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
# string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

# print(func3(string_list1, string_list2))
#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.  All'interno del file indicato da 'input_file'
e' codificata una matrice, dove ogni linea del file rappresenta una riga
della matrice. Ad esempio func4/func4_test1.txt contiene:

1,    2, 3
 4, 5,      6
7,   8,    9

La funzione deve leggere il file in 'input_file' e scrivere di nuovo la
stessa matrice ma aggiungendo parantesi quadre ad ogni riga e togliendo
gli spazi tranne il primo in modo da avere scritto in 'output_file':

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

e ritornare il numero di elementi della matrice.
Si apra 'func4/func4_test1.txt per vedere l'input e
'func4/func4_exp1.txt' per vedere l'output atteso.
"""


def func4(input_file, output_file):
    with open(input_file) as f, open(output_file, 'w') as g:
        l = f.readlines()
        for line in l:
            line = list(map(int,line.replace(' ','').strip().split(',')))
            print(line, file=g)
    return len(l)*len(line)




#print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4_test2.txt','func4_out2.txt'))
# print(func4('func4_test3.txt','func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG. L'immagine indicata dal 'input_pngfile' contiene solo
pixel neri e bianchi. E' necessario trovare tutti i segmenti
orizzontali di colore bianco.
I segmenti orizzontali su una riga possono essere al più uno.
Inoltre un segmento puo' essere lungo quanto tutta la larghezza
dell'immagine oppure anche lungo solamente un punto. I segmenti
orizzontali sono ritornati dalla funzione dentro una lista, dove ogni
segmento è codificato come tupla con coordinate (y, xstart, xend)
dove y è il numero di riga, xstart il primo pixel del segmento, xend
l'ultimo pixel del segmento. La lista ordina i segmenti in ordine crescente
in base alla coordinata y.

Ad esempio data l'immagine:

 0 1 2 3 4 5
0. . . . . .
1. . . . . .
2. . x . . .
3. . . . . .
4. . . . . .
5x x x x x x

dove . e' nero e x e' bianco, si ritorna:
[(2,2,2), (5,0,5)].

Per vedere i casi di test si vedano le immagini in func5/image01.png etc.
"""

import images

def segment(y, row):
    try:
        x = xstart = row.index((255,255,255))
        while x+1 < len(row) and row[x+1] == (255,255,255):
            x+=1
        # print(y, xstart, x)
        return(y, xstart, x)
    except ValueError:
        return None


def func5(input_pngfile):
    img = images.load(input_pngfile)
    return list(filter(None, [segment(y, row) for y,row in enumerate(img)]))


#print(func5('func5_test1.png'))
#print(func5('func5_test2.png'))
#print(func5('func5_test3.png'))
#print(func5('func5_test4.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.  La funzione
deve esplorare ricorsivamente l'albero delle directory con radice in
'directory' e restituire una lista di tuple di due elementi.  Ciascuna
tupla contiene in prima posizione il percorso ad un file testuale il
cui filename finisce per .txt; il secondo valore della tupla e' la
lunghezza L della riga piu' lunga del suddetto file txt, escludendo
il carattere di newline. La lista e'
ordinata in maniera crescente in base ad L e a partita' di lunghezza
in ordine alfabetico in base al percorso del file.

Se la funzione e' chiamata su 'ex1/A', ritorna:

[('ex1/A/QBwXM/KVobU.txt', 19)]

infatti il file 'ex1/A/QBwXM/KVobU.txt' ha la riga di massima lunghezza
di 19 caratteri (escluso lo \n e inclusi gli spazi).

NOTA: e' proibito usare la funzione os.walk. Si possono usare:
  os.listdir, os.path.isfile, os.path.exists, etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.
"""

import os
def check_file(fn):
    with open(fn) as f:
        lines = f.readlines()
    return len(max(lines, key = len).strip('\n'))

def ex1(directory):
    res = []
    for f in os.listdir(directory):
        fn = directory+'/'+f
        if fn.endswith('.txt') and os.path.isfile(fn):
            res.append((fn, check_file(fn)))
        if os.path.isdir(fn):
            res.extend(ex1(fn))
    return sorted(res, key=lambda t: (t[1], t[0]))




# print(ex1('ex1/A'))
# print(ex1('ex1/B'))
# print(ex1('ex1/C'))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che riceve in ingresso la radice di
un albero binario, come definito nella classe `BinaryTree` del modulo
tree.py.  L'albero in ingresso ha delle stringhe come valori. La
funzione deve restituire la stringa risultante dalla concatenazione di
tutti i valori associati ai nodi dell'albero con la seguente regola:
  - la stringa concatena in valori in base al livello, quindi
  prima tutti i valori del livello 0, poi tutti i valori del livello 1 etc.
  - fra i valori concatenati fra livelli viene aggiunto il carattere '-'

Esempio:

        ______A______                        ______A______
       |             |                      |             |
       B__        ___C___                __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F             _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                                      H   I      J  K   L   M   N

  Se l'albero è quello di sinistra, la funzione deve restituire il
  valore A-BC-DEF.

 Se l'albero è quello di destra, la funzione deve restituire il valore
   A-BC-DEFG-HIJKLMN
  """


def ex2(root):
    res = {}
    ex2a(root, 0, res)

    return '-'.join(res.values())

def ex2a(root, level, res):
    if not root:
        return
    if level not in res:
        res[level] = ''
    res[level]+=root.value
    ex2a(root.left, level+1, res)
    ex2a(root.right, level+1, res)

# from tree import BinaryTree
# root = BinaryTree.fromList(['A', ['B',[],['D',[],[]]], ['C', ['E',[],[]], ['F',[],[]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',[],[]],['I',[],[]]],['E',[],['J',[],[]]]], ['C', ['F',['K',[],[]],['L',[],[]]], ['G',['M',[],[]],['N',[],[]]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',['L',[],[]],[]],[]],['E',[],['I',[],[]]]],['C', ['F',['J',[],[]],[]],['G',[],['K',[],['M',[],[]]]]]])
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


# %%
# for n in (2,3,4):
    # i = images.load(f'func5/image0{n}.png')
    # for x,row in enumerate(i):
    #     for y, pixel in enumerate(row):
    #         if pixel != (0,0,0):
    #             i[x][y]=(255,255,255)
    # images.save(i, f'func5/image0{n}.png')