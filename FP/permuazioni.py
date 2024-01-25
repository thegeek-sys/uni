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

def aux_1(cur, a_set, n, l=1):
    rez = set()
    
    if n == l:
        return cur
    else:
        for i in cur:
            for j in a_set:
                if not j in i:
                    rez.add(j+i)
        rez = aux_1(rez, a_set, n, l+1)
    return rez

def ex1(a_set, n):
    # a_list = list(a_set)
    out = set()
    for x in a_set:
        p = aux_1({x}, a_set, n)
        out = p|out
    return out

# a_set = {'a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'}

# expected = {'cda', 'bad', 'dac', 'cab', 'bca', 'cdb', 'adc', 'bac', 'dba', 'dcb', 'adb', 'dbc', 'bda', 'abc', 'bcd', 'cba', 'cad', 'dab', 'dca', 'acd', 'acb', 'abd', 'cbd', 'bdc'}
# print(expected)
# print(ex1(a_set, 4))
# print(ex1({'a','b','c','d'}, 3)==expected)

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    pass
