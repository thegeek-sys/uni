#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER

To pass the exam you must:
    - solve at least 3 exercises of type func AND;
    - solve at least 1 exercise of type ex (recursive problem) AND;
    - obtain a score greater than or equal to 18

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "NAME"
surname = "SURNAME"
student_id = "MATRICULATION NUMBER"


#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# To run only some of the tests, you can comment out the entries
# corresponding to the tests you do not want to run within the list.
# `test` at the END of `grade.py`.
#
# To debug recursive functions you can disable the test of
# recursion by assigning `DEBUG=True` inside `grade.py` file.
#
# Setting DEBUG=True also enables the terminal printing of the STACK
# TRACE of errors, which lets you know the line number of the
# program.py that generated an error.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 points
Define the function func1(string_list1, string_list2) that receives as
input two lists of strings and returns a new list of strings
containing the strings present in only one of the two input lists
(i.e., that do not appear in both lists). The output list
must be sorted in reverse alphabetical order.
'''
def func1(string_list1, string_list2):
    # Write here your code
    pass


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points

Define a function func2(a_string) that takes as input a
string 'a_string' and returns another string. The new string has
all the letters of the input string repeated once and in
reverse alphabetical order.

Example: if a_string='welcome' the function func2(a_string) should
return 'womlec'
'''

def func2(a_string):
    # Write here your code
    pass

# print(func2('welcome'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points

Define a function func3(string_list1, string_list2) that takes
as input two lists of strings with the same number of strings.
Two strings taken in pairs from string_list1 and string_list2 always have
the same length.

Example: if string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
             string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

'sIN' has the same length as 'cas', 'VUL' has the same length as 'sia'.

Return a new list with the same elements of string_list2, modified with the
following rules:
 - the case of the characters of a string in string_list1 serves
   as a guide to set the case of the characters of the corresponding string
   in string_list2
- in particular if a character of the string of string_list1
  is lowercase, then the new character to be created must be taken from the
  corresponding character of the string in string_list2 but made lowercase.
- Conversely, if a character of the string of string_list1
  is UPPERCASE, then the new character to be created must to be taken from the
  corresponding character of the string in string_list2 but made UPPERCASE.
- In case a character is neither lowercase nor UPPERCASE it is left unchanged
- Lists may contain empty strings.

The final list should be sorted in descending order according to the length
of the strings, in case of equality, in alphabetical order.

Example: Given the input from before, the invocation of func3(string_list1, string_list2)
         should return the list ['cE', 'SIA', 'TOO', 'cAs', 'ceo']

For example, 'ce' --> 'cE' because 'sO' has a lowercase 's' and uppercase 'O'.

NOTE: use the string functions isupper(), lower() etc.     
'''


def func3(string_list1, string_list2):
    # Write here your code
    pass

# string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
# string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

# print(func3(string_list1, string_list2))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4+2 points
4 points:
Define a function func4(input_filename, output_filename, length)
that takes two strings representing two filenames and an integer
as input.
The file named input_filename contains strings separated by spaces,
tabs, or carriage returns.

The function must return the number of strings of the requested length
found in the input file.

+2 points:
The function must create a new text file named output_filename
containing all the strings of length 'length' present in the file
input_filename organized by rows.
The rows are in alphabetical order.
The words in each row:
    - have the same initial letter, with no distinction between
      uppercase and lowercase;
    - are separated by a space;
    - are sorted in alphabetical order, with no distinction between
      uppercase and lowercase. In the case of equal words, they are
      in lexicographical order (UPPERCASE before lowercase).


Example
If the following three lines are present in the file 'func4_test1.txt'
cat bat rat
Condor baT
cat cAr CAR

the function func4('func4_test1.txt', 'func4_out1.txt', 3) must write
in the file 'func4_out1.txt' the following 3 lines:
baT bat
CAR cAr cat
rat

and return the value 7.

"""


def func4(input_filename, output_filename, length):
    ## Write your code here
    pass

# print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 3))

#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 8 points
Define the function func5(txt_input, width, height, png_output) that
receives as arguments:
- txt_input: the path to a file containing a list of figures to be drawn
- width: width in pixels of the image to be created
- height: height in pixels of the image to be created
- png_output: the path to a PNG image you need to create, containing the figures

The function should create a black background image and draw all the figures
indicated in the 'txt_input' file, in the order they appear in the file.

The txt_file contains, one per line, separated by spaces:
- a word indicating the type of figure to be drawn
- the three R G B components of the color to be used
- the coordinates and other parameters needed to define the figure.
There can be 2 types of figure:
- descending diagonal of a square (-45° direction):
    diagonalDOWN R G B x y L
    The diagonal begins at the point (x,y), heads LOW-right, and is L pixels long
- ascending diagonal of a square (+45° direction):
    diagonalUP R G B x y L
    The diagonal starts at the point (x,y), heads UP-right, and is L pixels long

Then it must save the obtained image in the file 'png_output' using the
images.save function.
It must also return the number of diagonals drawn of the two types
as a tuple of the two values (DIAGUP, DIAGDOWN).

NOTE: the points of the figures outside the image must be handled correctly,
in fact, negative coordinates are also allowed,
and dimensions or parameter L such that parts of the figure are outside the image.

Example: if the file func5/in_1.txt contains the 3 figures:
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

running the function func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
will produce the figure in the file 'func5/expected_1.png'
and will return the pair (2, 1)
'''


import images

def func5(txt_input, width, height, png_output):
    # Write here your code
    pass

#print(func5('func5/in_1.txt', 50, 100, 'func5/out_1.png'))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Define a recursive function ex1(a_set, n), or that within it
uses a recursive function, which takes as input a set of strings
'a_set' and an integer n and returns a new set.
The output set must contain all possible strings obtained
with the concatenation of n elements belonging to a_set, without
repetition.  If n is greater than the number of elements in
a_set, the function returns an empty set.

Esempio:
    the function  ex1({'a','b','c'}, 2) returns
    {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
"""

def ex1(a_set, n):
    # INSERT HERE YOUR CODE
    pass
# print(ex1({'a','b','c'}, 2))

# ----------------------------------- EX.2 ----------------------------------- #


"""
Es 2: 6 punti

Design the function ex2(node, k), recursive or making use of
recursive functions or methods, which receives as arguments a binary 
tree and finds the node with a value multiple of k that is at the maximum
depth, starting from root=0. The function returns the depth
of the identified node. If no node has a value multiple of k, then the function
returns the value -1.

Each node is an object of the class tree.BinaryTree

Example: if k=5 and the tree is as follows.
                    1                           # depth 0
                /       \                       #
            25           7  ------------------- # 1
        /      \                                #
       3        65 ---------------------------- # 2
     /   \                                      #
    4     55  --------------------------------- # 3

the function ex2 must return 3, because 55 is the node with value
multiple of 5 that is at maximum depth, which is 3. The
other potential nodes are 25 and 65, but they are at a depth
lower (1 and 2, respectively).
"""

import tree

def ex2(node, k):
    # Write here your code
    pass

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
