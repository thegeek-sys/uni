#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal tu 18

The final score is the sum of the solved problems.
"""
name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

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

# %%  ---- FUNC1 ----
''' func1: 2 points
Define a function func1(string_list) that takes as input a list of strings an
returns another list with only the strings that start with a capital letter.
The returned list has to be ordered by the number of letters in
increasing order.
'''
def func1(string_list):
    a = [x for x in string_list if x[0].isupper()]
    a.sort(key=len)
    return a

# %%  ---- FUNC2 ----
''' func2: 2 points
Define a function func2(pathname) that takes as input a string representing
the path of a text file. The file has only rows with two words separated by
whitespace. The function must return a dictionary where the keys are the first
elements of a row and the values are sets with the second elements of a row.
Every second element of a row appears in the set corresponding to the key
of the first element of the same row.

Example:
Content of animals.txt:
    cat     meaow
    dog     woof
    cat     purr
The call func2('animals.txt') returns {'cat':{'meaow', 'purr'}, 'dog':{'woof'}
'''
def func2(pathname):
    with open(pathname, mode='r') as fr:
        corr = dict()
        for line in fr:
            words = line.split()
            corr[words[0]] = corr.get(words[0], set())|{words[1]}
        return corr

# %%  ---- FUNC3 ----
'''  func3: 2 points
Define a function func3(listA, listB, listC, pathname) that takes three lists
of numbers (integers or floats) and returns a new list where each element is
obtained considering the sum between the corresponding elements of the lists
listA and listB, sum multiplied for the corresponding element of listC.
The list built as above has to be written, one value for each row, in a text
file, with name pathname,
The function has to return the maximum value of the built list.
'''
def func3(listA, listB, listC, pathname):
    lis = []
    for i in range(len(listA)):
        el = (listA[i]+listB[i])*listC[i]
        lis.append(el)
    
    with open(pathname, mode='wt') as fw:
        for x in lis:
            fw.write(str(x)+'\n')
    
    return max(lis)
    
        

    
# %%  ---- FUNC4 ----
""" func4: 6 points

Define the function func4(triangles) that takes as input a list of
triples of positive numbers and eliminates from the list all triples
that cannot be the sides of a right triangle. Each number in the
triple can be either cathetus or hypotenuse, and there is no
predetermined order.  The function must return the number of triples
deleted from the triangles list. The triangles list must be modified
in-place.  To evaluate whether a triangle is right-angled one can use
the Pythagorean theorem: the sum of the squares constructed on the
catheti must equal the square constructed on the hypotenuse.  For
comparisons, use the round(x,3) rounding function.

Example: if triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         the function func4(triangles) return the value 3 and modifies the list
         so that
         triangles = [(3, 4, 5), (12, 36.05551, 34)].

In fact, considering the expected result triangles = [(3, 4, 5), (12, 36.05551, 34)]
it holds the following:

| triplet            | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTE: Break down the problem in small sub problems. Write small functions
for each sub problem. Compose everything together.

"""


def func4(triangles):
    i = 0
    for tri in triangles[::-1]:
        rev = sorted(tri)
        if round(rev[0]**2+rev[1]**2, 3)!=round(rev[2]**2, 3):
            i += 1
            triangles.remove(tri)
    return i
        



# %%  ---- FUNC5 ----
""" func5: 6 points
Define a function func5(img, filename) that returns a copy of the image img
flipped with respect to the vertical axis and saves the image in the file
with path as the filename string taken in input. The function returns the
color of the pixel in position (0,0) of the new image.
"""
import images
def func5(img, filename):
    new_im = []
    for row in img:
        new_im.append(row[::-1])
    images.save(new_im, filename)
    return new_im[0][0]



# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 points

Define the recursive function ex1 that takes as input a string
'directory' and a string 'namefile'. The function must search recursively
within the directory given by directory and in all subdirectories for
all files with name equal to namefile.  Such files are to be
interpreted as text files. Each text file contains only positive
numeric strings. Files with the same namefile always have the same
number of numeric strings.  The function must return a list of
integers obtained by summing the numeric strings of the files found,
position by position.

Example: if two files with the SAME namefile are found and those
files contain the sequences "11 23 90" and "11 77 0," the function ex3
returns the list [22, 100, 90].

We suggest using the functions os.listdir, os.path.isfile and
os.path.isdir and NOT to use the os.join function in Windows (use
concatenation between strings with the '/' character).

It is forbidden to use the os.walk function.

NOTE: Break down the problem in small sub problems. Write small
functions for each sub problem. Compose everything together.
"""

import os


def recur(base, f):
    ls = os.listdir(base)
    rez = []
    for el in ls:
        path = f'{base}/{el}'
        if os.path.basename(path) == f:
            rez.append(path)
        
        if os.path.isdir(path):
            part = recur(path, f)
            rez = rez+part
    return rez

def ex1(directory, namefile):
    sums = []
    files = recur(directory, namefile)
    for file in files:
        with open(file, mode='rt') as fr:
            fr = fr.read().split()
            fr = [int(x) for x in fr]
            if len(sums) == 0:
                sums = fr[:]
            else:
                for i in range(len(fr)):
                    sums[i] = sums[i] + fr[i]
    return sums
                    
    

# %% Ex2
"""
Ex2: 3+3 points
Define a recursive function (or one that uses recursive functions)
ex2(strings, n) that takes a set 'strings' and an integer 'n' and
recursively generates all possible strings that can be constructed by
concatenating n strings of the set strings. The function must return
all strings constructed. The function can return either a set with all
strings constructed (3 points), or a sorted list (6 points).  The list
is ordered considering the descending order of the length of the
strings and, in case of parity, considering the alphabetical order.

Example: if strings={'a','b','c','de'}, the function ex2(strings, 2)
returns the set {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 points)
or the list ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 points)
"""

def recu1(strings, let, n, num=1):
    rez = set()
    
    # caso base
    if num == n:
        return let
    
    else:
        
        for i in let:
            for j in strings:
                if not j in i:
                    rez.add(i+j)
        rez = recu1(strings, rez, n, num+1)
        # rez = rez | part
    return rez
    

def ex2(strings, n):
    a = set()
    for let in strings:
        rez = recu1(strings-{let}, set(let), n)
        a = a|rez
    a = sorted(a, key=lambda x: (-len(x), x))
    return a
        

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    '''print(func3([4, 1, 3, 5, 2], [5, 1, 1, 2, 3], [10, 5, 9, 9, 6], 'pippo.txt'))
    a = []
    with open('func3_1_exp.txt', mode='rt') as fr:
        for l in fr:
            a.append(l)
    
    b = []
    with open('pippo.txt', mode='rt') as fr:
        for l in fr:
            b.append(l)
       
    print(a)
    print(b)
    print(a==b) '''
    # print(func4([(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]))
    # print(func5('func5/image01.png', 'pipp.png'))
    # print(ex1('ex3/A',  'a.txt'))
    exp = {'roPythonmmin', 'Pythonpmmin', 'Pythongrammin', 'proPython', 'prommin', 'ropgra', 'grapro', 'graPythonmmin', 'Pythonrommin', 'rograPython', 'mmingraPython', 'Pythonpgra', 'pgraPython', 'graPythonp', 'progra', 'Pythonmminp', 'Pythonrop', 'gramminPython', 'pPythonro', 'grapmmin', 'mminroPython', 'mminpgra', 'mminPythonro', 'mminPythonp', 'grapPython', 'pgrammin', 'pmmingra', 'romminp', 'rommingra', 'pPythonmmin', 'Pythonmminro', 'Pythonrogra', 'pPythongra', 'romminPython', 'mmingraro', 'ropPython', 'mmingrap', 'mminrop', 'gramminp', 'mminrogra', 'Pythongrap', 'graPythonro', 'roPythonp', 'rograp', 'ropmmin', 'mminPythongra', 'Pythongraro', 'grarommin', 'rogrammin', 'Pythonpro', 'graroPython', 'roPythongra', 'pmminro', 'pmminPython', 'mminpro', 'mminpPython', 'pgraro', 'Pythonmmingra', 'gramminro', 'grarop'}
    print(ex2({'p', 'ro', 'gra', 'mmin', 'Python'}, 3))
    
    
    
