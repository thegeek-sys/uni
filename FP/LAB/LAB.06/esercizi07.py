
# Ignorare le righe fino alla 35
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato


def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Funzione da usare:
def load_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


# Dato il nome di un file di testo, ritornare il numero di volte che una parola
# e' presente nel file. La ricerca ignora la distinzione tra maiuscole e minuscole,
# e la punteggiatura.
def search_word(filename: str, word: str) -> int:
    fr = load_file(filename).lower()
    unique = set(fr)
    for x in unique:
        if not x.isalpha():
            fr = fr.replace(x, ' ')
    fr = fr.split()
    return fr.count(word)

# Dato il nome di un file di testo, si ritorna una "tabella" formata da una
# lista di dizionari. Nel file, la prima riga contiene i nomi delle colonne
# (chiavi nel dizionario) e le righe contengono i valori, tutti separati da
# spazi.
def load_table(filename: str) -> List[Dict[str, str]]:
    tab = []
    fr = load_file(filename).split('\n')
    keys = fr[0].split()
    for x in fr[1:]:
        l = x.split()
        elem = {}
        for i in range(len(l)):
            elem[keys[i]] = l[i]
        tab.append(elem)
    return tab
        


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# che rappresentano numeri interi vanno convertiti in interi e non lasciati come
# stringhe.
def load_data(filename: str) -> List[Dict[str, Union[int, str]]]:
    tab = []
    fr = load_file(filename).split('\n')
    keys = fr[0].split()
    for x in fr[1:]:
        l = x.split()
        elem = {}
        for i in range(len(l)):
            if l[i].isdecimal():
                elem[keys[i]] = int(l[i])
            else:
                elem[keys[i]] = l[i]
        tab.append(elem)
    return tab


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# sono separati da virgole e ci posso essere valori non presenti (due virgole
# consecutive). I valori mancanti devono essere aggiunti se `empties==True` come
# None, oppure essere omessi.
def load_csv(filename: str, empties: bool) -> List[Dict[str, Union[int, str, None]]]:
    tab = []
    fr = load_file(filename).split('\n')
    keys = fr[0].split(',')
    for x in fr[1:]:
        l = x.split(',')
        elem = {}
        for i in range(len(l)):
            if l[i].isdecimal():
                elem[keys[i]] = int(l[i])
            elif l[i] == '' and empties:
                elem[keys[i]] = None
            elif l[i] == '' and not empties:
                pass
            else:
                elem[keys[i]] = l[i]
        tab.append(elem)
    return tab


# Dato una file CSV, che si carica con la funzione precedente, ritornare un
# dizionario con la somma dei valori di ogni colonna numerica.
# Usare la funzione load_csv(), con la variable empties data a vostra scelta.
def column_stats(filename: str) -> Dict[str, Tuple[str, int]]:
    tab = load_csv(filename, True)
    out = {}
    for record in tab:
        for key, value in record.items():
            if isinstance(value, int):
                out[key] = out.get(key, 0)+value
    return out


# Test funzioni
check_test(search_word, 4, 'file01.txt', 'ciao')
check_test(search_word, 0, 'file01.txt', 'buon')
check_test(search_word, 1, 'file01.txt', 'buongiorno')
check_test(
    load_table, [{'Nome': "Luigi", "Telefono": '555-871612'},
                 {'Nome': "Mario", "Telefono": '555-826781'}], 'file02.txt')
check_test(
    load_data, [{'Nome': "Luigi", "Spese": 100},
                {'Nome': "Mario", "Spese": 1000}], 'file03.txt')
check_test(
    load_csv, [{'Nome': "Luigi", "Telefono": None, "Spese": 100, "Tasse": 10},
               {'Nome': "Mario", "Telefono": '555-1234', "Spese": 1000, "Tasse": None}], 'file04.csv', True)
check_test(
    load_csv, [{'Nome': "Luigi", "Spese": 100, "Tasse": 10},
               {'Nome': "Mario", "Telefono": '555-1234', "Spese": 1000}], 'file04.csv', False)
check_test(
    column_stats, {"Spese": 2100, "Tasse": 1011}, 'file05.csv')