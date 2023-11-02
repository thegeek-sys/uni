import testing

# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.
def check_pwd(pwd: str) -> bool:
    chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz','0123456789','$#@')
    str = ''
    every = False
    if 6 <= len(pwd) <= 16:
        for x in chars:
            for char in x:
                if char in pwd:
                    pwd = pwd.replace(char, '')
                    str += char
            for y in str:
                if x.find(y) != -1:
                    every = True
                else:
                    every = False
    if len(pwd) > 0 or not every:
        return False
    return True
    #    for x in chars:
    #        for char in x:
    #            if pwd.find(char) != -1:
    #                i += 1
    #                print(char, i)
    #                break
    #for item in chars:
    #    str += item
    #for x in pwd:
    #    if str.find(x) == -1:
    #        return False
    #return (True if i==4 else False)


# Scrivere una funzione che data una tupla (x, y, z)
# restituisca la tupla (z+1, x-1, y+2)
def tuple_ex(t: tuple) -> tuple:
    x, y, z = t
    return z+1, x-1, y+2

# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
def intersect(a: list, b: list) -> list:
    c = []
    for x in a:
        for y in b:
            if x == y:
                c.append(x)
    return c

# Scrivere una funzione che data una lista contenente valori >= 0, 
# crei una nuova lista contentente soltanto gli elementi della lista 
# originale tali che soddisfano la seguente proprietà:
#    lista[i] > 2*media(lista[0:i])
# (Il primo elemento non viene quindi mai inserito)
# Ad esempio, si consideri la lista [5, 3, 10, 0]
#  Il primo elemento è 5. Non viene inserito
#  Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5. Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista
#  Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4. Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista
#  Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6. Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista
def remove_avg(a: list) -> list:
    b = []
    def media(lista):
        y = 0
        for x in lista:
            y += x
        return y//len(lista)

    for i in range(len(a)):
        if i != 0:
            if a[i] > 2*media(a[0:i]):
                b.append(a[i])
    return b
        



# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
def frequency(a: list) -> list:
    out = []
    for x in a:
        i = 0
        for y in a:
            if x == y:
                i += 1
        if (x,i) not in out:
            out.append((x,i))
    return sorted(out)

# Scrivere una funzione che restituisce True
# se la lista è palindroma, o False altrimenti
def is_palindrome(a: list) -> bool:
    if a == a[::-1]:
        return True
    return False

# Scrivere una funzione che prende in input una lista, e 
# restituisce True se la lista è ordinata in ordine
# crescente o decrescente, e False altrimenti.
# Suggerimento: fare attenzione ai valori duplicati
# Utilizzare un solo ciclo e non utilizzare sorted/sort.
def is_sorted(a: list) -> bool:
    sorted = True
    asc = False
    for i in range(-len(a),-1,1):
        if a[i] >= a[i+1] and not asc:
            sorted = True
        elif a[i] <= a[i+1] and asc:
            sorted = True
        elif len(a) == 1:
            sorted = True
        else:
            sorted = False
            asc = True
    return sorted

# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
    pass


# Test funzioni
testing.check_test(check_pwd, False, "a")
testing.check_test(check_pwd, False, "000000000000000000")
testing.check_test(check_pwd, False, "almeno6")
testing.check_test(check_pwd, False, "Aa@09asng2/")
testing.check_test(check_pwd, True, "Aa@09asng2")
testing.check_test(tuple_ex, (3, -2, 1), (-1, -1, 2))
testing.check_test(intersect, [2, 3], [1, 2, 3], [2, 3, 4])
testing.check_test(intersect, [], [1, 2, 3], [10, 11, 12])
testing.check_test(intersect, [], [1, 2, 3], [])
testing.check_test(intersect, [], [], [1, 2, 3])
testing.check_test(remove_avg, [10], [5, 3, 10, 0])
testing.check_test(remove_avg, [20, 1000], [5, 20, 10, 1000])
testing.check_test(remove_avg, [], [])
testing.check_test(frequency, [(1, 1), (4, 2), (5, 1)], [5, 4, 1, 4])
testing.check_test(frequency, [(0, 1), (23, 3), (99, 1)], [23, 99, 0, 23, 23])
testing.check_test(is_palindrome, True, [])
testing.check_test(is_palindrome, True, [1])
testing.check_test(is_palindrome, True, [1, 2, 8, 2, 1])
testing.check_test(is_palindrome, True, [1, 2, 8, 8, 2, 1])
testing.check_test(is_palindrome, False, [1, 3, 8, 8, 2, 1])
testing.check_test(is_sorted, True, [1])
testing.check_test(is_sorted, True, [1, 1, 1])
testing.check_test(is_sorted, True, [1, 2, 3, 4])
testing.check_test(is_sorted, True, [4, 3, 2, 1])
testing.check_test(is_sorted, True, [1, 1, 2, 3, 3, 4])
testing.check_test(is_sorted, True, [4, 4, 3, 2, 2, 1])
testing.check_test(is_sorted, False, [1, 1, 3, 3, 2])
testing.check_test(is_sorted, False, [4, 4, 3, 3, 5])
testing.check_test(is_sorted_half, False, [1, 2, 3])
testing.check_test(is_sorted_half, False, [3, 2, 1])
testing.check_test(is_sorted_half, True, [1, 3, 2])
testing.check_test(is_sorted_half, True, [3, 1, 2])
testing.check_test(is_sorted_half, True, [1, 2, 5, 6, 8, 9, 3])