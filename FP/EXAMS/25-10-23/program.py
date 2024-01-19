#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario soddisfare tutti i seguenti vincoli:
    - risolvere almeno 3 esercizi di tipo func; AND
    - risolvere almeno 1 esercizio di tipo ex; AND
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è dato dalla somma dei punteggi dei problemi risolti.
Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"


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
dev'essere ordinata in ordine alfabetico inverso.
'''
def func1(string_list1, string_list2):
    # Inserire qui il proprio codice
    pass


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
    # scrivi qui il tuo codice
    pass

# print(func2('welcome'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe con lo stesso numero di stringhe.
Due stringhe prese a coppie da string_list1 e string_list2 hanno sempre
la stessa lunghezza.

Esempio: se  string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
             string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

'sIN' ha la stessa lunghezza di 'cas', 'VUL' ha la stessa lunghezza di 'sia'.

Si restituisca una nuova lista che ha gli stessi elementi della lista
string_list2, modificati con le seguenti regole:
 - il case dei caratteri della stringa della lista string_list1 serve
   come guida per impostare il case dei caratteri della stringa della lista
   string_list2
- in particolare se un carattere della stringa della lista string_list1
  è lowercase allora il nuovo carattere da creare dovrà essere preso dal
  carattere corrispondente della stringa della lista string_list2 ma reso
  lowercase.
- viceversa, se un carattere della stringa della lista string_list1
  è UPPERCASE allora il nuovo carattere da creare dovrà essere preso dal
  carattere corrispondente della stringa della lista string_list2 ma reso
  UPPERCASE.
- Nel caso un carattere non sia né lowercase né UPPERCASE si lascia invariato
- Le liste possono contenere stringhe vuote.

La lista finale va ordinata in ordine decrescente in base alla lunghezza
delle stringhe, in caso di parità, in ordine alfabetico.

Esempio: Dato l'input di prima, l'invocazione di func3(string_list1, string_list2)
         dovrà restituire la lista ['cE', 'SIA', 'TOO', 'cAs', 'ceo']

Ad esempio 'ce' --> 'cE' perche 'sO' ha la 's' miniuscola e 'O' maiuscola.

NOTA: si usino le funzioni delle stringhe isupper(), lower() etc.
'''


def func3(string_list1, string_list2):
    # scrivi qui il tuo codice
    pass

# string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
# string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

# print(func3(string_list1, string_list2))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4+2 points
4 points:
Definire una funzione func4(input_filename, output_filename, lunghezza)
che prende in input due stringhe che rappresentano due nomi di file e un intero
come input.
Il file indicato da input_filename contiene stringhe separate da spazi,
tabulazioni o ritorni a capo.

La funzione deve restituire il numero di stringhe della lunghezza richiesta
trovate nel file di input.

+2 punti:
La funzione deve creare un nuovo file di testo denominato output_filename
contenente tutte le stringhe di lunghezza 'lunghezza' presenti nel file
input_filename organizzate per righe.
Le righe sono in ordine alfabetico.
Le parole di ogni riga:
    - hanno la stessa lettera iniziale, senza distinzione tra
      maiuscole e minuscole
    - sono separate da uno spazio
    - sono ordinate in ordine alfabetico, senza distinzione tra maiuscole
      e minuscole. Nel caso di parole uguali, sono in ordine alfabetico.

Esempio
Se nel file "func4_test1.txt" sono presenti le tre righe seguenti
cat bat rat
Condor baT
cat cAr CAR

la funzione func4('func4_test1.txt', 'func4_out1.txt', 3) 
deve scrivere nel file 'func4_out1.txt' le seguenti 3 righe:
baT bat
CAR cAr cat
rat

e ritornare il valore 7.

"""


def func4(input_filename, output_filename, length):
    ## Write your code here
    pass

# print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 3))

#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 8 punti
Si definisca la funzione func5(txt_input, width, height, png_output) che riceve come argomenti

- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file.

Il file txt_file contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura

Possono essre presenti 2 tipi di figura:
- diagonale discendente di un quadrato (in direzione -45°)
    diagonalDOWN R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in BASSO a destra, ed è lunga L pixel
- diagonale ascendente di un quadrato (in direzione +45°)
    diagonalUP R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in ALTO a destra, ed è lunga L pixel

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di diagonali disegnate dei due tipi
come tupla dei due valori (DIAGUP,DIAGDOWN)

NOTA: va gestito correttamente lo sbordare delle figure dalla
immagine, infatti sono ammesse anche coordinate negative, e dimensioni
o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func5/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

l'esecuzione della funzione func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
produrrà una figura uguale al file 'func5/expected_1.png'
e tornerà la coppia (2, 1)
'''


import images

def func5(txt_input, width, height, png_output):
    core = []
    with open(txt_input, mode='rt') as fr:
        for line in fr:
            part = line.split()
            core.append([part[0], (int(part[1]), int(part[2]), int(part[3])), (int(part[4]), int(part[5])), int(part[6])])
    
    img = [ [ (0,0,0) ] * width for _ in range(height) ]
    
    # return core
    down, up = 0, 0
    for diagonal in core:
        ty = diagonal[0]
        color = diagonal[1]
        coords = diagonal[2]
        pixs = diagonal[3]
        
        row = coords[1]
        col = coords[0]
        
        while row < 0 or col < 0:
            row += 1
            col += 1
        
        while row > height-1 or col > width-1:
            row -= 1
            col -= 1
        
        row = min(max(row, 0), height-1)
        col = min(max(col, 0), width-1)
        if ty.endswith('DOWN'):
            down += 1
            for pix in range(pixs):
                if row > height-1 or col > width-1:
                    break
                # img[min(row, height-1)][min(col, width-1)] = color
                img[row][col] = color
                row += 1
                col += 1
                
        elif ty.endswith('UP'):
            up += 1
            for pix in range(pixs):
                if row < 0 or col > width-1:
                    break
                # img[max(row, 0)][min(col, height-1)] = color
                img[row][col] = color
                row -= 1
                col += 1
    
    images.save(img, png_output)
    return (down,up)
    

print(func5('func5/in_1.txt', 50, 100, 'func5/out_1.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(a_set, n), o che al suo interno
usa una funzione ricorsiva, che prende in ingresso un set di stringhe
'a_set' e un intero n e restituisce un nuovo set.
Il set in output deve contenere tutte le possibili stringhe ottenute
con la concatenazione di n elementi appartenenti ad a_set, senza
ripetizione.  Se n è maggiore del numero di elementi presenti in
a_set, la funzione restituisce un set vuoto.

Esempio:
    la funzione ex1({'a','b','c'}, 2) deve restituire l'insieme
    {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
"""

def ex1(a_set, n):
    # INSERT HERE YOUR CODE
    pass
# print(ex1({'a','b','c'}, 2))

# ----------------------------------- EX.2 ----------------------------------- #


"""
Es 2: 6 punti

Si progetti la funzione ex2(node, k), ricorsiva o che fa uso di
funzioni o metodi ricorsivi, che riceve come argomenti un albero
binario e trova il nodo divisibile per k che si trova a profondità
massima (partendo da radice=0). La funzione restituisce la profondità
del nodo individuato. Se nessun nodo è divisibile per k la funzione
ritorna il valore -1.

Ciascun nodo è un oggetto della classe tree.BinaryTree

Esempio: se k=5 e l'albero è il seguente
                1                          # profondità 0
            /      \                       #
          25        7  ------------------- # 1
        /    \                             #
       3      65 ------------------------- # 2
     /   \                                 #
    4     55  ---------------------------- # 3

la funzione ex2 deve ritornare 3, perchè 55 è il nodo con valore
multiplo di 5 che si trova a profondità massima, ovvero 3. Gli
altri nodi potenziali sono 25 e 65, ma sono a una profondità
inferiore (rispettivamente 1 e 2).
"""
import tree

def ex2(node, k):
    # INSERISCI QUI IL TUO CODICE
    pass

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
