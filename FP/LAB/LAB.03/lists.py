################################################################################
# Liste
################################################################################
import testing
from typing import List

# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    quad = 0
    for x in elements:
        quad += x**2
    return quad

# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    if elements:
        for x in elements:
            if 'comp' not in locals() or x > comp:
                comp = x
        return comp
    return None


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    result = []
    for x in elements:
        if x not in result:
            result.append(x)
    return result


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    return elements[::-1]


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e restituisce una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    result = []
    for x in elements:
        if isinstance(x, list):
            x = flatten_list(x)
            for y in x:
                result.append(y)
        else:
            result.append(x)
    return result


# Test funzioni
testing.print_test(sum_squares, [1, 2, 3])
testing.print_test(max_element, [1, 2, 3, -1, -2])
testing.print_test(max_element, [-1, -2])
testing.print_test(max_element, [])
testing.print_test(remove_duplicates, [1, 2, 3, 2, 3])
testing.print_test(reverse_list, [1, 2, 3])
testing.print_test(flatten_list, [1, [2, 3]])
testing.print_test(flatten_list, [1, [2, [3, 4]]])
