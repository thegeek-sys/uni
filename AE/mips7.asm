.globl main

.data
string: .asciiz "Hello world!"

.text
main:
	li $v0,4	# print_string
	la $a0,string	# load address della stringa
	syscall
