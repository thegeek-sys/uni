# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['BOLD']+COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['BOLD']+COL['RED']
        if col:
            return func(f'{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
        else:
            return func(*args, **kwargs, )
    return wrapped_func

my_print = my_decorator(print)

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = True
#DEBUG = False
#############################################################################

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m',
       'BOLD' : '\033[1m',
       'ENDC' : '\033[0m'}


def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9

###############################################################################


def do_func1_tests(string_list1, string_list2, expected):
    res = program.func1(string_list1, string_list2)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista ritornata è sbagliata! / The returned list is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func1_1():
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','d']
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','d']
    expected = ['d', 'c', 'b']
    return do_func1_tests(string_list1, string_list2, expected)

def test_func1_2():
    '''
    string_list1 = ['coke', 'fanta', 'sprite', 'lambdala', 'lemonsoda', 'oransoda']
    string_list2 = ['coke', 'fanta', 'oransoda', 'pepsi']
    '''
    string_list1 = ['a','b','c']
    string_list2 = []
    expected = ['c', 'b', 'a']
    return do_func1_tests(string_list1, string_list2, expected)

def test_func1_3():
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','b','c']
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','b','c']
    expected = []
    return do_func1_tests(string_list1, string_list2, expected)

def test_func1_4():
    '''
    string_list1 = ['a','b','c']
    string_list2 = []
    '''
    string_list1 = ['a','b','c']
    string_list2 = []
    expected = ['c', 'b', 'a']
    return do_func1_tests(string_list1, string_list2, expected)

# %% ----------------------------------- FUNC2 ------------------------- #
def do_func2_tests(a_string, expected):
    res = program.func2(a_string)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La stringa restituita non è corretta / The returned string is incorrect\n[ERROR] expected={expected} returned={res}.\n {'*'*50}''')
        return 0
    return 0.5


def test_func2_1():
    '''
    a_string = 'welcome'
    '''
    a_string = 'welcome'
    expected = 'womlec'
    return do_func2_tests(a_string, expected)

def test_func2_2():
    '''
    a_string = 'abracadabra'
    '''
    a_string = 'abracadabra'
    expected = 'rdcba'
    return do_func2_tests(a_string, expected)

def test_func2_3():
    '''
    a_string = ''
    '''
    a_string = ''
    expected = ''
    return do_func2_tests(a_string, expected)

def test_func2_4():
    '''
    a_string = 'capslockunhinderedbacklistartsgamesparasolphiltershobbledehoysmdvpratedfutonselectrocutedprevaricatemistakeobjectivenessallegorizesdisgustingunorderedunreleasedsuperadded'
    '''
    a_string = 'capslockunhinderedbacklistartsgamesparasolphiltershobbledehoysmdvpratedfutonselectrocutedprevaricatemistakeobjectivenessallegorizesdisgustingunorderedunreleasedsuperadded'
    expected = 'zyvutsrponmlkjihgfedcba'
    return do_func2_tests(a_string, expected)

# %% ----------------------------------- FUNC3 ------------------------- #
def do_func3_tests(string_list1, string_list2, expected):
    res = program.func3(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 2/3


def test_func3_1():
    '''
    string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
    string_list2=['ce', 'cas', 'too', 'ceo', 'sia']
    expected = ['SIA', 'TOO', 'cAs', 'ceo', 'cE']
    '''
    string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
    string_list2=['ce', 'cas', 'too', 'ceo', 'sia']
    expected = ['SIA', 'TOO', 'cAs', 'ceo', 'cE']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_2():
    '''
    string_list1=['A']
    string_list2=['A']
    '''
    string_list1=['AAA', 'fkjskfjsdkABCHGHF', '']
    string_list2=['bbb', 'BBBBBBBBBBcmcmcmmc' '']
    expected = ['bbbbbbbbbbCMCMCMM', 'BBB']
    try:
	    return do_func3_tests(string_list1, string_list2, expected)
    except:
        string_list1=['AAA', 'fkjskfjsdkABCHGHF']
        string_list2=['bbb', 'BBBBBBBBBBcmcmcmmc']
        expected = ['bbbbbbbbbbCMCMCMM', 'BBB']
        return do_func3_tests(string_list1, string_list2, expected)


def test_func3_3():
    '''
    string_list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    string_list2=['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    '''
    string_list1=['a', 'b', 'c', 'd', 'e', 'F', 'G', 'H', 'I', 'J']
    string_list2=['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    expected =  ['A', 'B', 'C', 'D', 'E', 'f', 'g', 'h', 'i', 'j']
    return do_func3_tests(string_list1, string_list2, expected)

# ----------------------------------- FUNC 4  ----------------------------------- #

def do_func4_tests(ID, length, expected):
    input_filename  = f'func4/func4_test{ID}.txt'
    output_filename = f'func4/func4_out{ID}.txt'
    if os.path.exists(output_filename):
        os.remove(output_filename)
    expected_filename = f'func4/func4_exp{ID}.txt'
    res = program.func4(input_filename, output_filename, length)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di righe ritornato è sbagliato! / The number of written rows is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    try:
        testlib.check_text_file(output_filename, expected_filename)
        return 2
    except:
        return 4/3

def test_func4_1():
    '''
    input_filename = 'func4/func4_test1.txt'
    expected = 7
    '''
    ID = 1
    length = 3
    expected = 7
    return do_func4_tests(ID, length, expected)

def test_func4_2():
    '''
    input_filename = 'func4/func4_test2.txt'
    '''
    ID = 2
    length = 8
    expected = 5
    return do_func4_tests(ID, length, expected)


def test_func4_3():
    '''
    input_filename = 'func4/func4_test3.txt'
    '''

    ID = 3
    length = 7
    expected = 20
    return do_func4_tests(ID, length, expected)

# ----------------------------------- FUNC. 5 ----------------------------------- #


def do_test_func5(ID, W, H, expected):
    txt_in  = f'func5/in_{ID}.txt'
    img_out = f'func5/your_image_{ID}.png'
    img_exp = f'func5/expected_{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func5(txt_in, W, H, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di rettangoli e ellissi è sbagliato! / The number of rectangles and ellipses are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''
    txt_file = func5/in_1.txt
    output_imagefile = func5/your_image_1.png
    width = 50
    heigth = 100
    expected_imagefile = func5/expected_1.png
    expected = (2, 1)
    '''
    ID = 1
    width = 50
    heigth = 100
    expected = (2, 1)
    return do_test_func5(ID, width, heigth, expected)

def test_func5_2():
    '''
    txt_file = func5/in_2.txt
    output_imagefile = func5/your_image_2.png
    width = 200
    heigth = 200
    expected_imagefile = func5/expected_2.png
    expected = (4, 7)
    '''
    ID = 2
    width = 200
    heigth = 200
    expected = (4, 7)
    return do_test_func5(ID, width, heigth, expected)


def test_func5_3():
    '''
    txt_file = func5/in_3.txt
    output_imagefile = func5/your_image_3.png
    width = 300
    heigth = 400
    expected_imagefile = func5/expected_3.png
    expected = (8, 13)
    '''
    ID = 3
    width = 300
    heigth = 400
    expected = (8, 13)
    return do_test_func5(ID, width, heigth, expected)


def test_func5_4():
    '''
    txt_file = func5/in_4.txt
    output_imagefile = func5/your_image_4.png
    width = 500
    heigth = 200
    expected_imagefile = func5/expected_4.png
    expected = (32, 23)
    '''
    ID = 4
    width = 500
    heigth = 200
    expected = (32, 23)
    return do_test_func5(ID, width, heigth, expected)

# %% ----------------------------------- EX1 ------------------------- #
def do_test_ex1(a_set, n, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.ex1(a_set, n)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res == None:
                raise testlib.NotImplemented()
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(a_set, n)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] L'insieme ritornato non è corretto/ The set returned is not correct\n{'*'*50}
                 Expected: {expected}\n
                 Returned: {res}.''')
        return 0
    return 2

def test_ex1_1():
    '''
    a_set = {'a','b','c'}
    n = 2
    expected = {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
    '''
    a_set = {'a','b','c'}
    n = 2
    expected = {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
    return do_test_ex1(a_set, n, expected)


def test_ex1_2():
    '''
    a_set = {'a','b','c','d'}
    n = 3
    expected = {'cda', 'bad', 'dac', 'cab', 'bca', 'cdb', 'adc', 'bac', 'dba', 'dcb', 'adb', 'dbc', 'bda', 'abc', 'bcd', 'cba', 'cad', 'dab', 'dca', 'acd', 'acb', 'abd', 'cbd', 'bdc'}
    '''
    a_set = {'a','b','c','d'}
    n = 3
    expected = {'cda', 'bad', 'dac', 'cab', 'bca', 'cdb', 'adc', 'bac', 'dba', 'dcb', 'adb', 'dbc', 'bda', 'abc', 'bcd', 'cba', 'cad', 'dab', 'dca', 'acd', 'acb', 'abd', 'cbd', 'bdc'}
    return do_test_ex1(a_set, n, expected)


def test_ex1_3():
    '''
    a_set = {'a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'}
    n = 4
    '''
    a_set = {'a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'}
    n = 4
    expected = {'defbcklmnoa', 'pqrstuvwxyzdefbc', 'pqrstubcaghij', 'klmnoghijpqrstubc', 'klmnodefpqrstubc', 'klmnoavwxyzpqrstu', 'apqrstuklmnobc', 'avwxyzpqrstubc', 'bcdefpqrstuvwxyz', 'pqrstuklmnovwxyzghij', 'ghijaklmnopqrstu', 'klmnobcghija', 'apqrstudefbc', 'pqrstubcavwxyz', 'defabcklmno', 'bcpqrstughijvwxyz', 'pqrstughijklmnovwxyz', 'klmnopqrstughijdef', 'ghijvwxyzadef', 'bcaghijpqrstu', 'pqrstuklmnoghijbc', 'abcdefvwxyz', 'klmnobcvwxyza', 'vwxyzklmnoaghij', 'klmnovwxyzpqrstubc', 'aklmnovwxyzpqrstu', 'pqrstughijdefklmno', 'aghijbcpqrstu', 'pqrstuklmnodefghij', 'vwxyzpqrstughijklmno', 'klmnopqrstuaghij', 'avwxyzbcdef', 'pqrstudefghijklmno', 'vwxyzbcdefklmno', 'klmnovwxyzapqrstu', 'vwxyzklmnodefbc', 'ghijpqrstudefa', 'bcghijdefpqrstu', 'ghijpqrstudefklmno', 'bcklmnopqrstughij', 'klmnoghijbcpqrstu', 'klmnobcadef', 'avwxyzbcpqrstu', 'vwxyzklmnopqrstubc', 'bcghijvwxyzpqrstu', 'avwxyzghijdef', 'bcapqrstudef', 'defpqrstuklmnobc', 'vwxyzdefbcpqrstu', 'pqrstuaghijbc', 'vwxyzbcghijdef', 'bcdefghija', 'bcpqrstuklmnoa', 'bcdefklmnoa', 'vwxyzghijapqrstu', 'ghijklmnopqrstubc', 'bcvwxyzpqrstughij', 'klmnobcpqrstuvwxyz', 'vwxyzbcklmnodef', 'klmnopqrstudefghij', 'bcpqrstuadef', 'ghijbcklmnodef', 'aghijpqrstudef', 'defklmnoabc', 'defvwxyzklmnopqrstu', 'ghijpqrstubcdef', 'pqrstughijklmnodef', 'pqrstubcdefvwxyz', 'avwxyzpqrstudef', 'pqrstudefvwxyzbc', 'defghijpqrstuklmno', 'klmnoapqrstudef', 'klmnoapqrstubc', 'adefbcvwxyz', 'aghijdefbc', 'pqrstughijavwxyz', 'avwxyzdefbc', 'pqrstuvwxyzdefklmno', 'vwxyzklmnopqrstua', 'klmnopqrstuvwxyzbc', 'pqrstuvwxyzghijklmno', 'bcapqrstughij', 'vwxyzadefbc', 'vwxyzbcklmnoghij', 'klmnovwxyzadef', 'defapqrstughij', 'abcvwxyzklmno', 'klmnoabcvwxyz', 'ghijpqrstuklmnobc', 'bcvwxyzghijpqrstu', 'bcghijadef', 'ghijabcklmno', 'vwxyzpqrstudefghij', 'aklmnobcghij', 'bcvwxyzghijdef', 'ghijklmnovwxyza', 'bcaklmnoghij', 'pqrstughijklmnobc', 'defbcghijpqrstu', 'vwxyzghijbca', 'vwxyzdefbca', 'klmnodefvwxyzghij', 'pqrstubcvwxyzghij', 'pqrstughijdefvwxyz', 'klmnobcpqrstudef', 'pqrstubcklmnoghij', 'klmnoabcpqrstu', 'apqrstubcvwxyz', 'bcdefpqrstuklmno', 'klmnobcvwxyzghij', 'vwxyzghijdefa', 'pqrstuaklmnoghij', 'defapqrstubc', 'pqrstuabcghij', 'adefpqrstuvwxyz', 'vwxyzbcpqrstua', 'vwxyzpqrstuadef', 'ghijaklmnovwxyz', 'ghijvwxyzdefbc', 'defklmnobcvwxyz', 'klmnobcvwxyzdef', 'vwxyzabcklmno', 'defvwxyzghija', 'defghijklmnoa', 'bcdefklmnoghij', 'klmnoabcghij', 'abcpqrstuvwxyz', 'pqrstuklmnoaghij', 'defbcpqrstughij', 'klmnoaghijpqrstu', 'defghijbcpqrstu', 'ghijdefpqrstubc', 'klmnobcdefvwxyz', 'bcpqrstudefklmno', 'vwxyzbcapqrstu', 'abcklmnoghij', 'vwxyzdefghijklmno', 'pqrstughijbcvwxyz', 'pqrstuavwxyzghij', 'vwxyzklmnobcdef', 'ghijbcvwxyzklmno', 'ghijabcdef', 'klmnovwxyzghijpqrstu', 'defavwxyzbc', 'ghijbcavwxyz', 'bcghijvwxyzklmno', 'bcghijpqrstuklmno', 'klmnopqrstudefa', 'bcdefklmnovwxyz', 'vwxyzbcdefa', 'defbcvwxyzpqrstu', 'pqrstughijdefbc', 'ghijbcpqrstua', 'bcklmnodefa', 'defpqrstubcvwxyz', 'avwxyzdefghij', 'vwxyzbcadef', 'adefvwxyzghij', 'vwxyzdefklmnoa', 'ghijdefvwxyza', 'bcklmnoadef', 'abcvwxyzdef', 'vwxyzklmnoghijdef', 'vwxyzdefpqrstuklmno', 'ghijapqrstuklmno', 'defbcghijklmno', 'klmnoaghijvwxyz', 'pqrstuadefklmno', 'klmnovwxyzaghij', 'klmnoapqrstuvwxyz', 'aklmnodefbc', 'aklmnodefvwxyz', 'vwxyzghijklmnobc', 'ghijdefpqrstua', 'bcaklmnodef', 'avwxyzpqrstughij', 'bcdefghijklmno', 'bcdefvwxyza', 'defklmnoaghij', 'klmnovwxyzbcpqrstu', 'ghijvwxyzklmnobc', 'bcvwxyzpqrstudef', 'vwxyzaklmnopqrstu', 'defghijbcvwxyz', 'apqrstuklmnoghij', 'vwxyzbcklmnopqrstu', 'pqrstuavwxyzbc', 'vwxyzklmnobcpqrstu', 'ghijbcvwxyza', 'bcapqrstuvwxyz', 'pqrstuklmnodefa', 'ghijadefklmno', 'klmnoghijvwxyzbc', 'pqrstubcklmnovwxyz', 'vwxyzghijdefpqrstu', 'ghijpqrstuabc', 'defghijpqrstua', 'defghijklmnopqrstu', 'klmnodefbcghij', 'defabcvwxyz', 'klmnoadefpqrstu', 'ghijvwxyzbcpqrstu', 'pqrstuvwxyzbcghij', 'pqrstuaghijvwxyz', 'vwxyzapqrstuklmno', 'defbcvwxyza', 'bcpqrstudefghij', 'vwxyzghijaklmno', 'ghijpqrstubca', 'bcdefghijpqrstu', 'bcklmnopqrstudef', 'defpqrstuvwxyzbc', 'ghijvwxyzabc', 'pqrstudefbca', 'defbcvwxyzklmno', 'ghijdefbcvwxyz', 'vwxyzapqrstughij', 'ghijvwxyzklmnoa', 'vwxyzghijklmnodef', 'ghijklmnovwxyzdef', 'pqrstuklmnoabc', 'bcpqrstuklmnoghij', 'pqrstughijvwxyza', 'pqrstudefavwxyz', 'defklmnopqrstubc', 'bcavwxyzghij', 'defklmnovwxyzbc', 'aklmnopqrstudef', 'pqrstudefklmnobc', 'ghijpqrstubcklmno', 'klmnovwxyzdefpqrstu', 'ghijpqrstuvwxyzbc', 'defabcpqrstu', 'defpqrstuvwxyzghij', 'klmnobcpqrstua', 'ghijdefapqrstu', 'abcpqrstudef', 'ghijdefvwxyzklmno', 'klmnovwxyzpqrstua', 'klmnodefvwxyzpqrstu', 'klmnopqrstudefbc', 'bcdefpqrstua', 'ghijbcdefa', 'adefpqrstuklmno', 'pqrstuklmnoghijvwxyz', 'pqrstubcdefklmno', 'ghijbcpqrstudef', 'adefvwxyzbc', 'klmnoghijdefa', 'apqrstughijdef', 'ghijapqrstudef', 'klmnobcpqrstughij', 'adefpqrstughij', 'aghijvwxyzdef', 'pqrstughijklmnoa', 'pqrstudefklmnoghij', 'klmnoaghijbc', 'pqrstuaklmnodef', 'ghijdefaklmno', 'aklmnobcpqrstu', 'vwxyzpqrstudefbc', 'vwxyzpqrstughijbc', 'ghijdefbcpqrstu', 'bcklmnoghija', 'aklmnopqrstuvwxyz', 'pqrstuklmnovwxyza', 'ghijklmnodefvwxyz', 'bcpqrstuaghij', 'defbcpqrstuklmno', 'pqrstuaghijklmno', 'vwxyzdefghijbc', 'vwxyzbcaklmno', 'defbcpqrstuvwxyz', 'vwxyzdefpqrstubc', 'defklmnovwxyza', 'vwxyzpqrstughijdef', 'ghijklmnoapqrstu', 'klmnobcvwxyzpqrstu', 'abcghijklmno', 'bcklmnodefghij', 'defbcklmnovwxyz', 'aghijpqrstuvwxyz', 'defghijapqrstu', 'bcvwxyzpqrstua', 'aklmnobcvwxyz', 'defghijklmnovwxyz', 'ghijpqrstuaklmno', 'ghijavwxyzdef', 'pqrstuvwxyzklmnobc', 'klmnoapqrstughij', 'bcpqrstughija', 'defpqrstuvwxyza', 'klmnopqrstuabc', 'pqrstudefklmnovwxyz', 'bcpqrstuavwxyz', 'ghijpqrstuvwxyza', 'defvwxyzpqrstuklmno', 'defvwxyzklmnoghij', 'aklmnovwxyzghij', 'pqrstuvwxyzdefa', 'ghijbcpqrstuklmno', 'pqrstubcghija', 'vwxyzdefklmnoghij', 'defapqrstuklmno', 'vwxyzapqrstudef', 'bcavwxyzpqrstu', 'klmnopqrstubcdef', 'bcadefklmno', 'ghijavwxyzklmno', 'ghijbcapqrstu', 'bcghijpqrstuvwxyz', 'defklmnobca', 'ghijavwxyzpqrstu', 'defvwxyzaghij', 'vwxyzpqrstughija', 'defbcghija', 'abcghijvwxyz', 'pqrstughijbcklmno', 'adefbcklmno', 'klmnodefaghij', 'defvwxyzpqrstughij', 'vwxyzaklmnobc', 'bcaghijdef', 'defklmnovwxyzghij', 'klmnodefvwxyza', 'ghijvwxyzpqrstuklmno', 'ghijadefbc', 'defklmnobcghij', 'klmnoghijadef', 'vwxyzklmnopqrstughij', 'ghijbcvwxyzpqrstu', 'klmnopqrstubcvwxyz', 'avwxyzdefpqrstu', 'bcvwxyzadef', 'apqrstubcdef', 'vwxyzdefklmnopqrstu', 'vwxyzaghijdef', 'bcklmnovwxyzghij', 'klmnopqrstuvwxyzdef', 'bcpqrstughijdef', 'pqrstubcghijklmno', 'bcpqrstuvwxyzdef', 'vwxyzapqrstubc', 'defpqrstuvwxyzklmno', 'bcklmnodefpqrstu', 'klmnovwxyzdefa', 'klmnoghijvwxyzdef', 'klmnoghijpqrstua', 'adefghijpqrstu', 'pqrstubcghijdef', 'klmnoghijdefvwxyz', 'pqrstudefaklmno', 'vwxyzghijadef', 'avwxyzbcklmno', 'defghijavwxyz', 'defghijvwxyzpqrstu', 'pqrstudefabc', 'klmnobcavwxyz', 'defavwxyzklmno', 'pqrstughijadef', 'aghijklmnodef', 'bcghijklmnovwxyz', 'ghijaklmnodef', 'defbcghijvwxyz', 'ghijklmnopqrstudef', 'klmnovwxyzpqrstughij', 'vwxyzbcdefghij', 'pqrstughijbca', 'pqrstudefklmnoa', 'ghijklmnopqrstuvwxyz', 'avwxyzklmnodef', 'ghijbcpqrstuvwxyz', 'bcghijpqrstudef', 'defklmnoghijbc', 'vwxyzabcghij', 'klmnoavwxyzghij', 'vwxyzklmnodefa', 'ghijdefavwxyz', 'defghijvwxyza', 'apqrstubcklmno', 'bcghijdefa', 'aklmnoghijpqrstu', 'pqrstudefvwxyzklmno', 'vwxyzaghijbc', 'klmnoghijdefbc', 'ghijklmnobcvwxyz', 'bcvwxyzdefpqrstu', 'pqrstuklmnobcdef', 'ghijdefbca', 'klmnodefghijvwxyz', 'bcvwxyzklmnodef', 'defvwxyzbcpqrstu', 'aghijpqrstuklmno', 'adefvwxyzpqrstu', 'abcpqrstuklmno', 'klmnoadefbc', 'ghijvwxyzklmnodef', 'ghijvwxyzbcklmno', 'pqrstudefaghij', 'klmnodefghija', 'defvwxyzpqrstubc', 'apqrstuklmnovwxyz', 'pqrstuklmnovwxyzbc', 'bcadefpqrstu', 'pqrstuvwxyzaklmno', 'adefklmnobc', 'pqrstuklmnobcvwxyz', 'avwxyzbcghij', 'vwxyzghijklmnopqrstu', 'defklmnoghijpqrstu', 'aklmnoghijvwxyz', 'vwxyzdefapqrstu', 'vwxyzklmnobca', 'defpqrstubcghij', 'klmnodefpqrstua', 'klmnodefpqrstughij', 'defaklmnopqrstu', 'aklmnopqrstubc', 'bcklmnopqrstua', 'vwxyzklmnopqrstudef', 'klmnopqrstuavwxyz', 'ghijavwxyzbc', 'defpqrstuklmnovwxyz', 'abcdefpqrstu', 'ghijdefabc', 'adefklmnoghij', 'defklmnobcpqrstu', 'vwxyzadefghij', 'ghijvwxyzbca', 'pqrstubcdefa', 'ghijklmnovwxyzpqrstu', 'bcpqrstudefvwxyz', 'vwxyzdefklmnobc', 'pqrstuaklmnobc', 'ghijapqrstubc', 'bcdefghijvwxyz', 'vwxyzpqrstubcdef', 'klmnopqrstughija', 'pqrstuvwxyzghijdef', 'vwxyzklmnoapqrstu', 'defklmnoghijvwxyz', 'pqrstuabcklmno', 'defghijabc', 'vwxyzklmnoadef', 'ghijadefvwxyz', 'bcghijaklmno', 'avwxyzklmnopqrstu', 'aghijdefpqrstu', 'ghijdefklmnopqrstu', 'vwxyzpqrstuklmnoa', 'pqrstubcadef', 'klmnovwxyzbcdef', 'bcdefaklmno', 'ghijabcvwxyz', 'avwxyzghijbc', 'defvwxyzabc', 'apqrstughijklmno', 'defbcapqrstu', 'klmnodefapqrstu', 'bcpqrstughijklmno', 'avwxyzklmnobc', 'defpqrstuaklmno', 'vwxyzghijbcpqrstu', 'pqrstubcklmnoa', 'klmnopqrstubcghij', 'bcadefvwxyz', 'pqrstudefghijvwxyz', 'bcaghijvwxyz', 'ghijdefpqrstuvwxyz', 'vwxyzdefaghij', 'aklmnopqrstughij', 'ghijbcklmnopqrstu', 'abcvwxyzghij', 'defaghijklmno', 'defvwxyzklmnoa', 'vwxyzghijklmnoa', 'apqrstuvwxyzdef', 'ghijbcadef', 'bcvwxyzpqrstuklmno', 'defpqrstuavwxyz', 'ghijadefpqrstu', 'aklmnodefpqrstu', 'bcpqrstuklmnodef', 'bcvwxyzklmnoghij', 'abcklmnopqrstu', 'defavwxyzghij', 'defpqrstuklmnoa', 'aghijbcdef', 'defghijvwxyzklmno', 'vwxyzpqrstudefklmno', 'vwxyzdefbcklmno', 'apqrstuvwxyzbc', 'ghijbcklmnoa', 'ghijpqrstubcvwxyz', 'vwxyzaghijpqrstu', 'aklmnovwxyzbc', 'pqrstuvwxyzdefghij', 'vwxyzaklmnoghij', 'apqrstughijvwxyz', 'klmnodefavwxyz', 'adefbcpqrstu', 'abcklmnovwxyz', 'pqrstuadefghij', 'aghijvwxyzbc', 'defklmnovwxyzpqrstu', 'defghijaklmno', 'ghijklmnodefpqrstu', 'pqrstughijabc', 'adefklmnopqrstu', 'pqrstughijbcdef', 'ghijpqrstudefvwxyz', 'klmnovwxyzbca', 'defpqrstuabc', 'pqrstuabcdef', 'ghijvwxyzpqrstudef', 'ghijklmnobca', 'vwxyzbcklmnoa', 'bcdefavwxyz', 'bcapqrstuklmno', 'bcghijavwxyz', 'defpqrstuklmnoghij', 'klmnoghijbcvwxyz', 'apqrstuklmnodef', 'aklmnovwxyzdef', 'vwxyzghijdefklmno', 'defklmnopqrstughij', 'pqrstubcklmnodef', 'vwxyzpqrstubcklmno', 'vwxyzklmnoghijpqrstu', 'ghijklmnoabc', 'adefklmnovwxyz', 'ghijpqrstuvwxyzklmno', 'ghijbcdefpqrstu', 'avwxyzklmnoghij', 'vwxyzabcdef', 'klmnoghijapqrstu', 'pqrstughijdefa', 'defvwxyzapqrstu', 'adefpqrstubc', 'pqrstuklmnovwxyzdef', 'bcvwxyzghijklmno', 'aghijvwxyzklmno', 'bcpqrstuaklmno', 'vwxyzklmnodefghij', 'ghijvwxyzklmnopqrstu', 'klmnovwxyzbcghij', 'klmnobcghijvwxyz', 'bcklmnodefvwxyz', 'bcghijklmnoa', 'vwxyzghijbcdef', 'defpqrstughija', 'vwxyzbcpqrstudef', 'klmnovwxyzghija', 'pqrstuvwxyzklmnoa', 'vwxyzklmnoghija', 'defaghijpqrstu', 'defaklmnoghij', 'aghijvwxyzpqrstu', 'bcpqrstuvwxyza', 'bcdefapqrstu', 'defbcklmnopqrstu', 'defbcklmnoghij', 'pqrstudefbcvwxyz', 'vwxyzpqrstubcghij', 'vwxyzbcaghij', 'abcdefghij', 'defpqrstuaghij', 'bcklmnovwxyzdef', 'vwxyzghijdefbc', 'bcghijklmnodef', 'ghijpqrstudefbc', 'bcklmnopqrstuvwxyz', 'pqrstuklmnoavwxyz', 'pqrstuaklmnovwxyz', 'avwxyzghijpqrstu', 'vwxyzklmnodefpqrstu', 'vwxyzpqrstuaghij', 'bcklmnovwxyza', 'ghijvwxyzapqrstu', 'klmnovwxyzdefbc', 'aghijpqrstubc', 'ghijklmnodefbc', 'vwxyzghijpqrstubc', 'klmnobcaghij', 'vwxyzdefghijpqrstu', 'ghijdefpqrstuklmno', 'bcvwxyzaklmno', 'defaghijbc', 'pqrstudefvwxyzghij', 'pqrstuadefvwxyz', 'bcvwxyzklmnoa', 'defbcpqrstua', 'bcvwxyzdefghij', 'vwxyzdefpqrstua', 'bcvwxyzghija', 'klmnoghijabc', 'ghijklmnobcpqrstu', 'bcghijapqrstu', 'ghijapqrstuvwxyz', 'defghijklmnobc', 'adefbcghij', 'aklmnobcdef', 'defpqrstughijbc', 'ghijklmnopqrstua', 'ghijklmnovwxyzbc', 'vwxyzbcpqrstughij', 'klmnoabcdef', 'klmnoadefvwxyz', 'vwxyzghijpqrstudef', 'ghijvwxyzbcdef', 'apqrstughijbc', 'pqrstuvwxyzaghij', 'klmnodefvwxyzbc', 'defklmnoghija', 'defklmnopqrstua', 'bcklmnoghijvwxyz', 'vwxyzpqrstudefa', 'ghijpqrstuavwxyz', 'bcklmnoavwxyz', 'klmnopqrstuvwxyza', 'klmnobcdefghij', 'pqrstuvwxyzbcdef', 'defbcaghij', 'bcklmnovwxyzpqrstu', 'abcpqrstughij', 'pqrstuklmnoghija', 'pqrstughijvwxyzdef', 'defpqrstughijvwxyz', 'defvwxyzklmnobc', 'apqrstuvwxyzklmno', 'vwxyzbcghijklmno', 'vwxyzdefaklmno', 'bcvwxyzapqrstu', 'pqrstuavwxyzdef', 'klmnovwxyzdefghij', 'ghijvwxyzdefa', 'defvwxyzpqrstua', 'defbcavwxyz', 'defaklmnobc', 'ghijbcdefvwxyz', 'bcghijpqrstua', 'klmnoghijdefpqrstu', 'klmnodefbca', 'pqrstughijvwxyzklmno', 'pqrstuvwxyzklmnodef', 'ghijklmnoadef', 'apqrstuvwxyzghij', 'defvwxyzbcghij', 'klmnodefbcpqrstu', 'pqrstuaghijdef', 'vwxyzklmnoabc', 'vwxyzadefklmno', 'vwxyzaklmnodef', 'defaklmnovwxyz', 'abcklmnodef', 'pqrstuvwxyzghijbc', 'vwxyzbcghija', 'klmnopqrstudefvwxyz', 'defghijpqrstubc', 'vwxyzaghijklmno', 'ghijabcpqrstu', 'klmnobcapqrstu', 'vwxyzghijpqrstua', 'adefghijklmno', 'ghijklmnoavwxyz', 'aklmnodefghij', 'ghijvwxyzdefpqrstu', 'ghijpqrstuklmnovwxyz', 'bcdefaghij', 'adefghijbc', 'pqrstuavwxyzklmno', 'ghijvwxyzaklmno', 'avwxyzghijklmno', 'vwxyzghijpqrstuklmno', 'bcklmnoghijdef', 'vwxyzbcdefpqrstu', 'pqrstuvwxyzabc', 'bcdefvwxyzklmno', 'vwxyzdefghija', 'abcdefklmno', 'klmnovwxyzabc', 'defpqrstughijklmno', 'bcaklmnopqrstu', 'apqrstudefvwxyz', 'vwxyzpqrstuklmnoghij', 'pqrstudefghijbc', 'bcklmnoaghij', 'bcaklmnovwxyz', 'avwxyzdefklmno', 'pqrstudefghija', 'vwxyzpqrstuklmnobc', 'defvwxyzbca', 'defklmnoavwxyz', 'defklmnopqrstuvwxyz', 'defvwxyzghijklmno', 'bcpqrstudefa', 'ghijklmnobcdef', 'ghijbcaklmno', 'bcghijvwxyzdef', 'aghijdefklmno', 'adefghijvwxyz', 'pqrstubcvwxyza', 'defbcvwxyzghij', 'aghijbcklmno', 'bcklmnoghijpqrstu', 'apqrstudefklmno', 'pqrstubcghijvwxyz', 'bcklmnoapqrstu', 'vwxyzklmnobcghij', 'pqrstubcvwxyzklmno', 'bcdefklmnopqrstu', 'pqrstubcaklmno', 'ghijvwxyzdefklmno', 'bcghijvwxyza', 'defabcghij', 'defavwxyzpqrstu', 'vwxyzdefabc', 'klmnoaghijdef', 'bcadefghij', 'pqrstughijaklmno', 'ghijbcvwxyzdef', 'defghijbcklmno', 'ghijbcklmnovwxyz', 'klmnoadefghij', 'defghijvwxyzbc', 'klmnobcdefa', 'aklmnoghijdef', 'adefvwxyzklmno', 'pqrstuklmnoadef', 'ghijaklmnobc', 'pqrstuklmnobcghij', 'defbcaklmno', 'aghijbcvwxyz', 'aghijklmnovwxyz', 'bcpqrstuvwxyzghij', 'vwxyzpqrstuklmnodef', 'ghijvwxyzpqrstua', 'pqrstughijvwxyzbc', 'pqrstuvwxyzghija', 'ghijdefklmnobc', 'bcdefpqrstughij', 'ghijpqrstuklmnodef', 'klmnopqrstughijbc', 'vwxyzbcpqrstuklmno', 'ghijpqrstuklmnoa', 'ghijdefbcklmno', 'bcdefvwxyzghij', 'apqrstudefghij', 'ghijdefklmnoa', 'abcvwxyzpqrstu', 'bcvwxyzdefklmno', 'pqrstubcdefghij', 'defapqrstuvwxyz', 'aghijklmnopqrstu', 'bcdefvwxyzpqrstu', 'vwxyzpqrstubca', 'bcghijdefvwxyz', 'pqrstuadefbc', 'pqrstubcvwxyzdef', 'vwxyzpqrstuaklmno', 'pqrstuklmnoghijdef', 'defklmnoapqrstu', 'pqrstudefbcklmno', 'vwxyzghijbcklmno', 'ghijdefvwxyzbc', 'defpqrstubca', 'klmnobcghijpqrstu', 'defghijbca', 'pqrstuvwxyzadef', 'klmnodefpqrstuvwxyz', 'vwxyzklmnoghijbc', 'ghijklmnodefa', 'ghijvwxyzpqrstubc', 'defvwxyzbcklmno', 'defvwxyzaklmno', 'defvwxyzghijpqrstu', 'defaghijvwxyz', 'defvwxyzghijbc', 'klmnopqrstughijvwxyz', 'klmnoghijbcdef', 'ghijdefklmnovwxyz', 'defghijpqrstuvwxyz', 'klmnopqrstuvwxyzghij', 'pqrstuvwxyzbcklmno', 'aghijdefvwxyz', 'klmnoghijpqrstuvwxyz', 'klmnovwxyzghijdef', 'abcghijpqrstu', 'pqrstuklmnodefbc', 'vwxyzdefpqrstughij', 'klmnovwxyzghijbc', 'bcpqrstuvwxyzklmno', 'klmnodefabc', 'aklmnoghijbc', 'bcaghijklmno', 'vwxyzpqrstuabc', 'klmnoghijbca', 'pqrstuvwxyzbca', 'bcpqrstuklmnovwxyz', 'avwxyzpqrstuklmno', 'vwxyzbcghijpqrstu', 'vwxyzabcpqrstu', 'klmnoavwxyzdef', 'klmnodefbcvwxyz', 'klmnoghijvwxyzpqrstu', 'ghijdefvwxyzpqrstu', 'klmnobcghijdef', 'klmnopqrstuadef', 'abcghijdef', 'klmnobcdefpqrstu', 'ghijpqrstuadef', 'bcavwxyzdef', 'defpqrstubcklmno', 'ghijbcdefklmno', 'vwxyzdefbcghij', 'aghijklmnobc', 'pqrstudefvwxyza', 'bcghijklmnopqrstu', 'vwxyzghijabc', 'apqrstubcghij', 'bcavwxyzklmno', 'bcvwxyzdefa', 'klmnoavwxyzbc', 'bcvwxyzaghij', 'vwxyzadefpqrstu', 'pqrstudefbcghij', 'klmnoghijvwxyza', 'pqrstuklmnodefvwxyz', 'klmnoghijavwxyz', 'bcvwxyzklmnopqrstu', 'klmnoghijpqrstudef', 'bcghijdefklmno', 'klmnodefghijpqrstu', 'pqrstuklmnobca', 'klmnovwxyzpqrstudef', 'pqrstuabcvwxyz', 'pqrstuvwxyzklmnoghij', 'klmnopqrstubca', 'ghijpqrstuvwxyzdef', 'klmnodefghijbc'}
    return do_test_ex1(a_set, n, expected)

# ----------------------------------- EX.2 ----------------------------------- #
import tree

def do_test_ex2(itree, K, expected_depth, score=2):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(itree, K)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    out = program.ex2(itree, K)
    testlib.check(out, expected_depth, None, f"Wrong type of value: expecting int but received {type(out)}.")
    testlib.check(out, expected_depth, None, f"Wrong value: expecting {expected_depth} but received {out}.")
    return score


def test_ex2_1():
    ''' lowest multiple of 5 in example.txt -> depth 3 '''
    itree = tree.BinaryTree.fromList([1, [25, [3, [4, None, None], [55, None, None]], [65, None, None]], [7, None, None]])
    K              = 5
    expected_depth = 3
    return do_test_ex2(itree, K, expected_depth)

def test_ex2_2():
    ''' lowest multiple of 9 in tree-10-60.txt -> depth 6 '''
    itree = tree.BinaryTree.fromList([269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]])
    K              = 9
    expected_depth = 6
    return do_test_ex2(itree, K, expected_depth)

def test_ex2_3():
    ''' lowest multiple of 7 in tree-10-60.txt -> depth -1 (not found) '''
    itree = tree.BinaryTree.fromList([269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]])
    K             = 7
    expected_depth= -1
    return do_test_ex2(itree, K, expected_depth)


def test_ex2_4():
    ''' lowest multiple of 11 in tree-20-60.txt -> depth 14 '''
    tree_list = [783508, [-991165, None, [-403114, [694375, None, [-625776, [-984200, None, [-567675, None, None]], [-77560, None, None]]], [-124358, [-810037, None, [-429701, [317231, None, [919617, [-372775, [974707, [-428019, [634010, None, [631589, [245491, None, None], None]], None], [-860703, [-386442, None, None], [90256, [721441, None, None], [-956206, [236568, [340989, None, None], [-722839, [-541788, [-114194, [-285235, None, None], None], [-69670, None, [-658259, [565754, [-534894, None, None], [183819, None, None]], None]]], [-869311, [415418, None, None], None]]], None]]]], [-585669, [-859079, None, [-521882, None, [904930, [733448, [690672, [-351223, None, None], None], [581866, [693281, [-20457, None, None], None], [-389156, [-352329, None, [-413166, [209195, None, [19733, None, None]], None]], [434097, None, [-910322, [-388475, [285460, None, None], [335300, None, None]], [693920, [27441, None, None], [-790347, None, None]]]]]]], [338990, None, [-327537, None, [-574650, None, None]]]]]], None]], None]], None]], None]]], None]
    itree = tree.BinaryTree.fromList(tree_list)
    K             = 11
    expected_depth= 14
    return do_test_ex2(itree, K, expected_depth)

def test_ex2_5():
    ''' lowest multiple of 17 in tree-10-80.txt -> depth 8 '''
    expected_tree = [202842, [-645741, [-170691, None, [-165619, [222351, [100026, [-742935, [-350330, [346608, [924340, None, None], [-96809, None, None]], [470258, [-556482, None, None], [-377624, None, None]]], [403163, [264749, [-484352, None, None], [110219, None, None]], [-817934, [803773, None, None], [-169027, None, None]]]], [-337484, [360694, [916882, [-160455, None, None], [720819, None, None]], [797288, [-169054, None, None], [236718, None, None]]], [-6231, [436611, [985353, None, None], [881664, None, None]], [-913123, [-199797, None, None], [-783762, None, None]]]]], None], [-256813, [-702310, [677198, [721889, [32689, None, [452226, None, None]], [669594, None, [-628440, None, None]]], [-214851, [-62873, [-934471, None, None], None], [-711761, [-734368, None, None], [-556399, None, None]]]], [-265749, [327995, [-211601, [-271193, None, None], None], None], [71319, [-668323, [-362537, None, None], [-222064, None, None]], [-712034, [-393509, None, None], None]]]], [-312818, [46788, [-387131, [411132, [-471632, None, None], [-861109, None, None]], [858489, [606158, None, None], [352025, None, None]]], [-210168, [779036, [707104, None, None], [945391, None, None]], [776990, [913775, None, None], [-597112, None, None]]]], [682908, [-950136, [473635, [15850, None, None], [259694, None, None]], [708537, [4775, None, None], [-328988, None, None]]], [-808248, None, None]]]]]], None], None]
    itree = tree.BinaryTree.fromList(expected_tree)
    K              = 17
    expected_depth = 8
    return do_test_ex2(itree, K, expected_depth)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, 
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    grades = {}
    total  = 0
    with open('grade.csv') as F:
        for line in F:
            test, points = line.split(',')
            _, name, *_ = test.split('_')
            if name == 'personal': continue
            total += float(points)
            grades[name] = grades.get(name, 0) + float(points)
    #%% Constraint for the exam
    constraint1 = len([name for name,grade in grades.items() if grade>0 and name.startswith('func')]) >= 3
    constraint2 = len([name for name,grade in grades.items() if grade>0 and name.startswith('ex')]) >= 1
    constraint3 = total >= 18
    constraint4 = all((constraint1, constraint2, constraint3))
    if not constraint1:
        print(f'YOU HAVE NOT PASSED AT LEAST 3 FUNC EXERCISES: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint2:
        print(f'YOU HAVE NOT PASSED AT LEAST 1 RECURSIVE EXERCISE: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint3:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['BOLD']+COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
################################################################################
