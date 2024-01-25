#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA
 3) Rinominare la directory examPY inserendo il proprio numero di matricola

Per superare l'esame e' necessario soddisfare tutti i seguenti vincoli:
    - risolvere almeno 3 esercizi di tipo func; AND
    - risolvere almeno 1 esercizio di tipo ex; AND
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.
Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""
nome       = "Flavio"
cognome    = "Sperandeo"
matricola  = "2108912"


#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci
# corrispondenti ai test che non si vogliono eseguire all'interno della lista
# `test` alla FINE di `grade.py`.
#
# Per eseguire il debug di funzioni ricorsive potete disattivare il test di
# ricorsione, assegnando `DEBUG=True` all'interno file `grade.py`.
#
# L'impostazione DEBUG=True attiva anche lo la stampa a terminale dello STACK
# TRACE degli errori, che permette di conoscere il numero della linea di
# program.py che ha generato un errore.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(string_list1, string_list2) che riceve in
ingresso due liste di stringhe e restituisce una nuova lista di stringhe
contenente le stringhe presenti soltanto in una delle due liste in ingresso
(ossia, che non compaiono in entrambe le liste). La lista in output
dev'essere ordinata in ordine lessicografico inverso.
'''
def func1(string_list1, string_list2):
    slist1 = set(string_list1)
    slist2 = set(string_list2)
    rez = slist1^slist2
    return sorted(rez, key=lambda x: x.lower(), reverse=True)

# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 2 punti
Si definisca una funzione funct2(path_to_file) che riceve in ingresso
una stringa che rappresenta il percorso ad un file testuale. La funzione
deve restituire il dizionario che associ ad ogni carattere nel testo il
conteggio delle sue occorrenze.

Esempio:
  Il contenuto di func2_test_1.txt è:
    cat rat fat
    art
  L'output atteso dall'invocazione di func2('func2/func2_test_1.txt') è:
  {'c':1, 'a':4, 't':4, 'r':2, 'f':1, ' ':2, '\n':1}

Nota:
  Aprire il file con encoding 'utf-8'.
'''
def func2(path_to_file):
    rez = {}
    with open(path_to_file, mode='rt') as fr:
        fr = fr.read()
        for i in fr:
            rez[i] = rez.get(i, 0) + 1
    return rez

# %% -------------------------------- FUNC.3 -------------------------------- #
'''  func3: 2 punti
Si definisca una funzione func3(a_list) che riceve in ingresso una lista
di numeri ed opera su di essa (ossia, provocando side-effect) rimuovendo tutti
gli elementi uguali al massimo e al minimo.
La funzione deve restituisce la differenza fra la lunghezza iniziale e la
lunghezza finale della lista.

Esempio:
    se a_list = [3, 12, -3, 4, 6, 12]
    dopo la chiamata a func3(a_list) si ha che
    a_list = [3, 4, 6]
    e la funzione restituisce 3.

IMPORTANTE: la lista `a_list` deve risultare cambiata alla fine
dell'esecuzione della funzione.
'''

def func3(a_list):
    i = 0
    Mm = [max(a_list), min(a_list)]
    for a in a_list[::-1]:
        if a in Mm:
            a_list.remove(a)
            i += 1
    return i

# %% -------------------------------- FUNC.4 -------------------------------- #
""" func4: 6 punti
Si definisca una funzione func4(input_filepath, output_filename) che
riceve in ingresso due percorsi a file:
  - Il file `input_filepath` contiene una sequenza di parole, ossia stringhe
    separate da spazi, tabulazioni o invii a capo.
  - Il file `output_filename` indica dove salvare un nuovo file di testo,
    i cui contenuti sono specificati di seguito.
Il file in output deve contenere tutte le parole presenti in
`input_filename`, ripetute una sola volta e organizzate in righe nel modo
seguente.

Le righe nel file di output sono in ordine alfabetico.
All'interno di ogni riga, le parole
  - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
    minuscole;
  - sono separate da uno spazio;
  - sono ordinate in base alla loro lunghezza e, in caso di pari
    lunghezza, in base all'ordine alfabetico, senza distinzione fra
    maiuscole e minuscole. Nel caso in cui nessuno dei criteri sin qui
    forniti distingua le parole, quelle coincidenti devono essere
    disposte secondo ordinamento lessicografico (ovverosia, si tiene conto
    della differenza tra lettere maiuscole e minuscole solo in ultima
    istanza).

La funzione deve restituire il numero di righe scritte nel file
`output_filename`.

Esempio:
  Nel file 'func4/func4_test1.txt' sono presenti le seguenti due righe:
cat bat    rat
Condor baT
  L'invocazione di func4('func4/func4_test1.txt', 'func4/func4_out1.txt')
  dovrà scrivere nel file 'func4/func4_out1.txt' le seguenti tre righe
  restituendo il valore 3:
baT bat
cat Condor
rat
"""

def func4(input_filename, output_filename):
    with open(input_filename, mode='rt') as fr:
        words = fr.read().split()
    
    words = set(words)
    words = sorted(words, key = lambda x: (x[0].lower(), len(x), x.lower(),x))
    a, p = [], []
    
    for i in range(len(words)):
        if i == 0:
            p.append(words[i])
        else:
            if words[i][0].lower() == words[i-1][0].lower():
                p.append(words[i])
            else:
                a.append(p)
                p = [words[i]]
    a.append(p)

    with open(output_filename, mode='wt') as fw:
        for x in a:
            fw.write(' '.join(x))
            fw.write('\n')
            
    return len(a)

# func4('func4/func4_test2.txt', 'func4/func4_out2.txt')

# %% -------------------------------- FUNC.5 -------------------------------- #
""" func5: 8 punti
Si definisca una funzione func5(imagefile, output_imagefile, color) che riceve
in ingresso due stringhe che rappresentano due percorsi a file di immagini PNG e
un colore fornito come una tupla RGB.
L'immagine nel file `imagefile` contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza massima utilizzando il colore `color` in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso `output_imagefile`.

La funzione restituisce il numero di segmenti colorati nell'immagine
in output.
"""
import images
def func5(imagefile, output_imagefile, color):
    img = images.load(imagefile)
    l = -1
    r_o = []
    for row in range(len(img)):
        if img[row].count((255,255,255)) > l:
            l = img[row].count((255,255,255))
            r_o = [row]
        elif img[row].count((255,255,255)) == l:
            r_o.append(row)
    
    for r in r_o:
        for col in range(len(img[r])):
            if img[r][col] == (255,255,255):
                img[r][col] = color
    
    images.save(img, output_imagefile)
    return len(r_o)

# img_in  = 'func5/image01.png'
# img_ou  = 'func5/your_image01.png'
# func5(img_in, img_ou, (255,0,0))

# %% --------------------------------- EX.1 --------------------------------- #
"""
Ex1: 6 punti

Implementare la funzione ex1 (in modo ricorsivo o utilizzando funzioni
ricorsive) come segue. La funzione ex1 riceve in ingresso i seguenti
argomenti:
  - `directory`, una stringa che rappresenta il percorso di una directory
  - `ext`, una stringa che rappresenta un'estensione di file.
La funzione deve cercare in modo ricorsivo all'interno della `directory`
e in tutte le sue sottodirectory i file che abbiano `ext` come estensione.
Questi file devono essere interpretati come file di testo. La funzione
ex1 deve calcolare la somma delle dimensioni di tutti i file trovati
nelle sottodirectory e restituire un dizionario strutturato come
come segue:
  - le chiavi sono tutte le sottodirectory in cui è presente almeno
    un file con estensione `ext`
  - i valori sono la somma delle dimensioni di tali file contenuti in quella
  sottodirectory.
Le sottodirectory devono essere riportate con il percorso relativo alla
directory corrente. Per esempio, data la struttura di directory:
A/
  B/
    file1.png    #4 byte
  file2.txt      #8 byte

L'invocazione `ex1("A", ".png")` deve restituire `{"A/B":4}`

La dimensione di un file può essere calcolata contando il numero di caratteri
letti dal file.

Si consiglia di utilizzare le funzioni os.listdir, os.path.isfile e
os.path.isdir e NON la funzione os.join in Windows. Utilizzare
la concatenazione tra stringhe con il carattere '/'.
"""

import os

def aux_1(directory, ext):
    rez = []
    for fold in os.listdir(directory):
        path = f'{directory}/{fold}'
        if path.endswith(ext):
            rez.append(path)
        elif os.path.isdir(path):
            p = aux_1(path, ext)
            rez = p + rez
            
    return rez

def ex1(directory, ext):
    rez = {}
    files = aux_1(directory, ext)
    for file in files:
        rez[os.path.dirname(file)] = rez.get(os.path.dirname(file), 0) + os.path.getsize(file)
        
    return rez

# print(ex1("ex1/A", ".txt"))


# %% --------------------------------- EX.2 --------------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che riceve in ingresso la radice di un
albero binario, come definito nella classe `BinaryTree` del modulo tree.py.
La funzione deve restituire la somma di tutti i valori associati ai nodi che
sono ad un livello pari nell'albero con radice `root`, e sottraendo tutti i
valori associati ai nodi ad un livello dispari. La radice si assume a livello 0.

Esempio:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

  Se l'albero è quello di sinistra, la funzione deve restituire il valore 8.
  Se l'albero è quello di destra, la funzione deve restituire il valore -22.
"""

import tree

def ex2(root, l=0):
    nodes = 0
    if l%2==0:
        nodes += root.value
    elif l%2==1:
        nodes -= root.value
    
    if root.right:
        p = ex2(root.right, l+1)
        nodes += p
    if root.left:
        p = ex2(root.left, l+1)
        nodes += p
        
    return nodes

# root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root))



###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
