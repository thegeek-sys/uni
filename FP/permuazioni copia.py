#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

def aux1(a, a_set, n, l=1):
    rez = set()
    if n == l:
        return a
    else:
        for i in a:
            for j in a_set:
                if j not in i:
                    rez.add(j+i)
        rez = aux1(rez, a_set, n, l+1)
    
    return rez
        

def ex1(a_set, n):
    rez = set()
    for a in a_set:
        p = aux1({a}, a_set, n)
        rez = rez | p
    return rez
    

# a_set = {'a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'}

expected = {'cda', 'bad', 'dac', 'cab', 'bca', 'cdb', 'adc', 'bac', 'dba', 'dcb', 'adb', 'dbc', 'bda', 'abc', 'bcd', 'cba', 'cad', 'dab', 'dca', 'acd', 'acb', 'abd', 'cbd', 'bdc'}
# print(expected)
# print(ex1(a_set, 4))
print(ex1({'a','b','c','d'}, 3)==expected)

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    pass
