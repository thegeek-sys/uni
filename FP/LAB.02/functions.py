
from typing import Any, Callable, List
# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')

################################################################################
# Funzioni
################################################################################
# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.

def cubic_root(n):
    if n < 0:
        n = (-n)**(1/3)
        n = -n
    else:
        n = n**(1/3)
    return n

# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e ritorna la maggiore.
# Se le radici sono complesse, la funzione restituisce una qualsiasi
# delle due radici
def root_max(a, b, c):
    delta = b**2-4*a*c
    if delta >= 0:
        root_1 = (-b+delta**(1/2))/(2*a)
        root_2 = (-b-delta**(1/2))/(2*a)
        if root_1 > root_2:
            return root_1
        else:
            return root_2
    else:
        return -1

# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e le ritorna entrambe.
def roots(a, b, c):
    delta = b**2-4*a*c
    if delta >= 0:
        root_1 = (-b+delta**(1/2))/(2*a)
        root_2 = (-b-delta**(1/2))/(2*a)
        return root_1, root_2
    else:
        return -1

# Scrivere una funzione che prende come input cinque numeri e ritorna la somma
# dei numeri pari meno quella dei numeri dispari.
def even_minus_odd(a, b, c, d, e):
    args = [a, b, c, d, e]
    even = 0
    odd = 0
    for x in args:
        if x%2==0:
            even += x
        else:
            odd += x
    return even-odd

# Scrivere una funzione che prende tre valori di input, e ritorna la
# loro somma se i valori sono punteggi di esame validi(`0 <= grade <= 30`),
# e altrimenti ritorna `- 1`. Scriverne poi una variante che legge i valori da
# terminale con `input`.
def check_grade(a, b, c):
    if (a <= 30 and a >= 0) and (b <= 30 and b >= 0) and (c <= 30 and c >= 0):
        return a+b+c
    else:
        return -1

# Scrivere una funzione che prende tre valori(`d`, `m`, `y`) e ritorna se la
# data è valida o no. Si possono ignorare gli anni bisestili. Ad esempio,
# ritorna `False` per `30/2/2017` e `True` per `1/1/1111`.
def check_date(d, m, y):
    if m==1 and (d > 0 and d <= 31):
        return True
    elif m==2 and (d > 0 and d <= 28):
        return True
    elif m==3 and (d > 0 and d <= 31):
        return True
    elif m==4 and (d > 0 and d <= 30):
        return True
    elif m==5 and (d > 0 and d <= 31):
        return True
    elif m==6 and (d > 0 and d <= 30):
        return True
    elif m==7 and (d > 0 and d <= 31):
        return True
    elif m==8 and (d > 0 and d <= 31):
        return True
    elif m==9 and (d > 0 and d <= 30):
        return True
    elif m==10 and (d > 0 and d <= 31):
        return True
    elif m==11 and (d > 0 and d <= 30):
        return True
    elif m==1 and (d > 0 and d <= 31):
        return True
    else:
        return False
    

# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome letto come input e poi da `Buona giornata!`
def print_hello():
    nome = input('Nome: ')
    return 'Ciao '+nome+', bouna giornata!'

print_test(cubic_root, 8)
print_test(cubic_root, -1)
print_test(root_max, 2, 3, 4)
print_test(root_max, 1, 200, 4)
print_test(roots, 2, 3, 4)
print_test(roots, 1, 200, 4)
print_test(even_minus_odd, 2, 4, 1, 3, 6)
print_test(even_minus_odd, 2, 2, 2, 2, 2)
print_test(even_minus_odd, 1, 1, 1, 1, 1)
print_test(check_grade, 21, 18, 2)
print_test(check_grade, 21, 32, 2)
print_test(check_grade, 21, 18, -2)
print_test(check_date, -1, 12, 2011)
print_test(check_date, 1, 14, 2011)
print_test(check_date, 1, 12, -1)
print_test(check_date, 31, 4, 2011)
print_test(check_date, 30, 4, 2011)
print_test(print_hello)