################################################################################
# Stringhe
################################################################################
import testing
from typing import List

# Scrivere una funzione che restituisce una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    saluto = str("Ciao "+name+" Buona giornata")
    return saluto


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    return string.replace(' ', '')


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    pass



# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    substrings_index = []
    for i in range(len(string)-len(find)+1):
        if string[i:i+len(find)] == find:
            substrings_index.append((i,i+len(find)))

    out, i = string, 0
    for x, y in substrings_index:
        out = out[:x+i]+replace+out[i+y:]
        i = len(replace)-len(find)
    return out


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    beth = list("abcdefghijklmnopqrstuvwxyz")
    cryt = []
    for i in range(len(beth)):
        if chr(ord(beth[i])+offset) not in beth:
            cryt.append(chr(ord(beth[i])+offset-26))
        else:
            cryt.append(chr(ord(beth[i])+offset))

    cryt_decryt = ''
    if not decrypt:
        for i in range(len(string)):
            if string[i] == ' ':
                cryt_decryt += ' '
            else:
                cryt_decryt += cryt[beth.index(string[i])]
    else:
        for i in range(len(string)):
            if string[i] == ' ':
                cryt_decryt += ' '
            else:
                cryt_decryt += beth[cryt.index(string[i])]
    return cryt_decryt



# Test funzioni
testing.print_test(make_hello, 'Pippo')
testing.print_test(strip_whitespace, '  Pippo  ')
testing.print_test(strip_whitespace, '   ')
testing.print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
testing.print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
testing.print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
testing.print_test(caesar_cypher, 'ciao pippo', 17, False)
testing.print_test(caesar_cypher, 'tzrf gzggf', 17, True)
