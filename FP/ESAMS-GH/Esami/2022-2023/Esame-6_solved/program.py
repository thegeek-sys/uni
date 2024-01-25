#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.
"""
nome       = "Flavio"
cognome    = "Sperandeo"
matricola  = "2108912"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################


# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 points
Si definisca la funzione func1(int_list, bottom, up) che prende in
ingresso una lista di interi e due interi e modifica la lista rimuovendo
tutti gli interi che non sono compresi nell'intervallo [bottom, up],
estremi inclusi. Attenzione: la lista risulta modificata alla fine
della funzione.
La funzione ritorna il numero di elementi rimossi dalla lista.
Esempio:
    func1([4, 5, 10, 3, -1, 2], 0, 5) deve restituire il valore 2 e modificare
    la lista in input in [4, 5, 3, 2].
'''
def func1(int_list, bottom, up):
    i = 0
    for x in int_list[::-1]:
        if not (bottom <= x <= up):
            int_list.remove(x)
            i+=1
    return i

# l1 = [4, 5, 10, 3, -1, 2]
# print(func1(l1, 0, 5))
# print (l1)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Si definisca una funzione func2(dict1, dict2) che prende in ingresso
due dizionari che hanno valori di tipo stringa e restituisce un nuovo
dizionario. Nel nuovo dizionario sono presenti soltanto le chiavi comuni
ai due dizionari in input. Ad ogni chiave del nuovo dizionario è associato
il valore minore fra i valori dei dizionari in input associati a quella
chiave. Tutte le stringhe valore del nuovo dizionario sono trasformate
in minuscolo.
Esempio:
    func2({'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}, {'a':'Bad', 'c':'greaT'})
    deve restituire il dizionario {'a':'bad', 'c':'excellent'}
'''
def func2(dict1, dict2):
    rez = {}
    for k, v in dict1.items():
        if k in dict2:
            rez[k] = min(v, dict2[k]).lower()
    return rez

# print(func2({'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}, {'a':'Bad', 'c':'greaT'}))

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Si definisca una funzione func3(str1, str2) che prende in ingresso due stringhe
e costruisce una nuova stringa str3 ottenuta selezionando soltanto i caratteri
per cui str1 e str2 sono uguali, senza distinzione fra minuscole e maiuscole,
ma selezionando il carattere della stringa più corta.
La funzione restituisce la stringa così costruita.
Esempio:
    func3('abracadabra', 'ABerrant') deve restituire la stringa 'ABa'
'''

def func3(str1, str2):
    M, m = max(str1, str2, key=len), min(str1, str2, key=len)
    rez = ''
    for i in range(len(m)):
        if m[i].lower() == M[i].lower():
            rez += m[i]
    return rez


# print(func3('abracadabra', 'ABerrant'))
# print(func3('delIberAtIVelY', 'ReproductIvE'))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca una funzione func4(input_filename, output_filename, length) che
prende in ingresso due stringhe che rappresentano due nomi di file e un
intero.
Il file input_filename contiene una serie di stringhe separate da spazi,
tabulazioni o a capo.
La funzione deve creare un nuovo file di testo con nome output_filename
contenente tutte le stringhe di lunghezza length presenti nel file
input_filename organizzate per righe.
Le righe sono in ordine alfabetico.
Le parole di ogni riga:
    - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
      minuscole
    - sono separate da uno spazio
    - sono ordinate in base all'ordine alfabetico, senza distinzione fra
      maiuscole e minuscole. In caso di parole uguali, in ordine alfabetico.

La funzione deve ritornare il numero di stringhe della lunghezza
richiesta trovate nel file in input.

Esempio
Se nel file 'func4_test1.txt' sono presenti le seguenti tre righe
cat bat    rat
Condor baT
Cat cAr CAR

la funzione func4('func4_test1.txt', 'func4_out1.txt', 3) dovrà scrivere
nel file 'func4_out1.txt' le seguenti 3 righe:
baT bat
CAR cAr Cat cat
rat

e ritornare il valore 7.

"""

def func4(input_filename, output_filename, length):
    with open(input_filename, mode='rt') as fr:
        fr = fr.read().split()
        words = [x  for x in fr if len(x) == length]
    words = sorted(words, key = lambda x: (x[0].lower(), x.lower(), x))

    rez = []
    a = []
    for i in range(len(words)):
        if i == 0:
            a.append(words[i])
        else:
            if words[i][0].lower() == words[i-1][0].lower():
                a.append(words[i])
            else:
                rez.append(a)
                a = []
                a.append(words[i])
    rez.append(a)
    
    el = 0
    for i in range(len(rez)):
        for j in range(len(rez[i])):
            el += 1
            if rez[i][j] != rez[i][-1]:
                rez[i][j] = rez[i][j]+' '
    
    with open(output_filename, mode='wt') as fw:
        for x in rez:
            fw.write(''.join(x))
            fw.write('\n')
    
    return el
        
# print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 3))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Si scriva una funzione func5(input_filename, output_imagefile) che prende
in ingresso due stringhe che rappresentano due nomi di file.
Il file input_filename in ogni riga contiene una serie di interi separati
da una virgola. Per ogni serie di interi, la funzione deve disegnare il
perimetro di una forma in un'immagine con sfondo nero, rispettando l'ordine
delle righe del file in input.
Ogni serie può essere formata da 6 oppure 7 interi, a seconda che la forma
da disegnare sia un quadrato oppure un rettangolo.
La struttura di ogni serie di valori è la seguente: (r, g, b, x, y, w, h), dove
- r, g, b rappresentano i tre canali del colore con cui disegnare la forma
- x, y rappresentano le coordinate dell'angolo superiore sinistro della forma
- w, h rappresentano rispettivamente la larghezza e l'altezza della forma.
Nel caso di un quadrato, non è presente il valore h.
Le dimensioni dell'immagine sono tali da contenere perfettamente tutte le
forme, per cui:
    - la forma con l'angolo inferiore destro più a destra avrà il lato
      destro sul bordo dell'immagine,
    - la forma con l'angolo inferiore destro più in basso avrà il lato
      inferiore sul bordo dell'immagine.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna il numero di forme disegnate nell'immagine in output.

Per gli esempi si vedano i file nella directory func5.
"""
import images

def draw_img(shapes):
    x = []
    y = []
    for shape in shapes:
        coords = shape[1]
        dims = shape[2]
        if len(dims) == 2:
            x.append((coords[0],coords[0]+dims[0]))
            y.append((coords[1],coords[1]+dims[1]))
        else:
            x.append((coords[0],coords[0]+dims[0]))
            y.append((coords[1],coords[1]+dims[0]))
    Mx = max([i[1] for i in x])
    My = max([i[1] for i in y])
    
    img = [[ (0,)*3 for i in range(Mx) ] for i in range(My)]
    return img

def draw_rect(img, color, x, y, xr, yr):
    for i in range(x, x+xr):
        img[y][i] = color
        img[y+yr-1][i] = color
    
    for i in range(y, y+yr):
        img[i][x] = color
        img[i][x+xr-1] = color
    
    return img



def draw_square(img, color, x, y, l):
    for i in range(x, x+l):
        img[y][i] = color
        img[y+l-1][i] = color
    
    for i in range(y, y+l):
        img[i][x] = color
        img[i][x+l-1] = color
        
    return img



def func5(input_filename, output_imagefile):
    shapes = []
    with open(input_filename, mode='rt') as fr:
        for line in fr:
            line = line.strip().split(',')
            shapes.append([(int(line[0]),int(line[1]),int(line[2])),(int(line[3]),int(line[4])),tuple(int(x) for x in line[5:])])
    
    img = draw_img(shapes)
    for shape in shapes:
        color = shape[0]
        x, y = shape[1][0], shape[1][1]
        if len(shape[2]) == 2:
            img = draw_rect(img, color, x, y, shape[2][0], shape[2][1])
        else:
            img = draw_square(img, color, x, y, shape[2][0])
    images.save(img, output_imagefile)
    
    return len(shapes)
    
    
# img = images.load('func5/func5_exp4.png')
# print(len(img), len(img[0]))
# print(func5('func5/func5_test4.txt', 'func5/func5_test4.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(n, faces), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso due interi, n e faces.

La funzione deve restituire una lista con tutti i possibili esiti del
lancio di 'n' dadi, ognuno con 'faces' facce. Ogni esito è rappresentato
da una tupla con 'n' elementi, un elemento per ogni dado.
La lista restituita deve essere ordinata in ordine crescente.

Esempio:
    ex1(2, 3) deve restituire la lista
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
"""

def aux_1(face, faces, n, l=1):
    rez = []
    if n == l:
        return face
    else:
        for i in face:
            for j in faces:
                tu = i + (j,)
                rez.append(tu)
        rez = aux_1(rez, faces, n, l+1)
    return rez

def ex1(n, faces):
    faces = list(range(1,faces+1))
    rez = []
    
    for face in faces:
        p = aux_1([(face,)], faces, n)
        rez = rez+p
    
    return sorted(rez)

# print(ex1(3,4))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso il nodo root che è la radice di
un albero binario costituito da nodi del tipo BinaryTree,
come definito nel modulo tree.py.
La funzione deve trasformare l'albero in input in modo che ogni nodo
con due figli abbia il figlio sinistro con un valore minore del
figlio destro, scambiando i valori dei nodi dei due figli se necessario.
La funzione restituisce il numero di scambi effettuati.

Esempio:

        root                   expected root
    ______5______              ______5______
   |             |            |             |
   8__        ___2___         2__        ___8___
      |      |       |           |      |       |
      3      9       1           3      1       9

      expected = 2

    Se l'albero è quello a sinistra, la funzione deve ritornare il
    valore 2 e trasformare l'albero in quello a destra.

Altro esempio:

              root                          expected root
          ______2______                      ______2______
         |             |                    |             |
      __ 7__        ___5___              __ 5__        ___7___
     |      |      |       |            |      |      |       |
    _4_     3_    _0_     _5_          _3_     4_    _0_     _5_
   |   |      |  |   |   |   |        |   |      |  |   |   |   |
   2   -1     1  8   3   2   9       -1   2      1  3   8   2   9

       expected = 4

    Se l'albero è quello a sinistra, la funzione deve ritornare il
    valore 4 e trasformare l'albero in quello a destra.

"""
import tree        

def ex2(root):
    i = 0
    if root.left and root.right:
        if root.left.value > root.right.value:
            vl = root.left.value
            rl = root.right.value
            root.left.value = rl
            root.right.value = vl
            i += 1
    
    if root.left:
        pi = ex2(root.left)
        i = i + pi
    
    if root.right:
        pi = ex2(root.right)
        i = i + pi
    
    return i

# root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root))


###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
