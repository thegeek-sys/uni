from typing import Any, Callable, List, Tuple
from testing import check_test

# Scrivere una funzione che converte una stringa di caratteri numerici
# nell'intero corrispondente. Non usare la funzione `int(string)`.
def string_to_int(string: str) -> int:
    pass


# Scrivere una funzione che converte un intero in una stringa di caratteri
# numerici corrispondenti all'intero. Non usare la funzione `str(integer)`.
def int_to_string(integer: int) -> str:
    pass


# Scrivere una funzione che data una stringa, ritorna una lista di tuple
# consituita da parola e frequenza, ordinata per frequenza. La frequenza è
# il numero di volte in cui la parole appare nel testo.
# Per evitare problemi nel trovare le parole, togliere tutti i caratteri
# non alfanumerici, a parte gli spazi, e convertire le parole in minuscolo.
# Usare la funzione `isalnum()` per testare i caratteri.
def word_frequency(string: str) -> List[Tuple[str, int]]:
    for x in string:
        if not x.isalnum() and x != ' ':
            string = string.replace(x, '')
    string = string.lower().split(' ')

    out = []
    for x in set(string):
        i = 0
        while x in string:
            string.remove(x)
            i+=1
        out.append((i,x))
    return sorted(out)



# Scrivere una funzione che data una stringa di numeri interi separati da spazi,
# ritorna la lista ordinata dei numeri interi con frequenza massima.
def number_frequency(string: str) -> List[int]:
    string = string.split()
    string = [int(elem) for elem in string]
    max_freq = 0
    check=[]
    for x in string:
        if string.count(x) > max_freq:
            max_freq = string.count(x)
            check = [x]
        elif string.count(x) == max_freq:
            check.append(x)
    return list(set(check))




# Implementare una funzione *ricorsiva* che data una lista contenente valori
# e sottoliste, ritorna una lista contenente tutti i valori. Ad esempio:
# [1, [2, 3]] => [1, 2, 3] e [1, [2, [3, 4]]] => [1, 2, 3, 4]
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


# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: List[dict]) -> dict:
    out = {}
    for dictionary in dictionaries:
        for key, val in dictionary.items():
            out[key] = val
    return out


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono le chiavi presenti nei due di input e come
# valori ritorna una lista con i valori presenti nei dizionari di input.
# Si possono usare i set.
def merge_dict(dictionaries: List[dict]) -> dict:
    out = {}
    for dictionary in dictionaries:
        for key, val in dictionary.items():
            if key not in out:
                out[key] = [val]
            else:
                out[key].append(val)
    return out


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: List[dict]) -> dict:
    out = {}
    for i in range(len(dictionaries)):
        dictionary = set(dictionaries[i]) & set(dictionaries[len(dictionaries)-i-1])
        for key, val in dictionaries[i].items():
            if key in dictionary and key not in out:
                out[key] = [val]
            elif key in dictionary:
                out[key].extend([val])
    return(out)


# Test funzioni
check_test(string_to_int, 5, "5")
check_test(string_to_int, 123, "123")
check_test(int_to_string, "5", 5)
check_test(int_to_string, "123", 123)
check_test(word_frequency, [(1, "ciao"), (1, "pippo")], "Ciao Pippo")
check_test(word_frequency, [(1, "pluto"), (2, "pippo")], "Pippo Pluto Pippo")
check_test(word_frequency, [(1, 'pippo'), (1, 'pluto'),
           (2, 'ciao')], "Ciao Pippo! Ciao Pluto!")
check_test(number_frequency, [10], "1 2 2 3 10 10 10")
check_test(number_frequency, [2, 5], "1 1 5 5 5 2 2 2")
check_test(flatten_list, [1, 2, 3], [1, [2, 3]])
check_test(flatten_list, [1, 2, 3, 4], [1, [2, [3, 4]]])
check_test(flatten_list, [1, 2, 3, 4, 5, 6, 7, 8],
           [1, [2, [3, 4], 5, [6, [7, 8]]]])
check_test(update_dict, {'Ciao': 1, 'Pippo': 2, 'Pluto': 3},
           [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
check_test(update_dict, {'Ciao': 1, 'Pippo': 4, 'Pluto': 3}, [{
           "Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
check_test(merge_dict, {'Ciao': [1], 'Pippo': [2], 'Pluto': [3]},
           [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
check_test(merge_dict, {'Ciao': [1], 'Pippo': [2, 4], 'Pluto': [3]}, [{
           "Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
check_test(intersect_dict, {'Pippo': [2, 3]},
           [{"Ciao": 1, "Pippo": 2}, {"Pippo": 3, "Pluto": 4}])
check_test(intersect_dict, {'Pippo': [2, 3], 'Pluto': [5, 4]},
           [{"Ciao": 1, "Pippo": 2, "Pluto": 5}, {"Pippo": 3, "Pluto": 4}])