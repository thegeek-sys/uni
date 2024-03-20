.globl main

.data # parte statica della rappresentazione dei dati nella ram
	vector: .word 1, -2, 3, -4, 5, -6, 7, -8, 9, 10, 11, 12, 13 # scrivo ogni numero in una word della ram
	# vector: .byte 1, -2, 3, -4, 5, -6, 7, -8, 9, 10, 11, 12, 13 # scrivo ogni numero in un byte della ram
	n: .word 5

.text # parte della ram per il codice, senza .text non potrei scrivere il codice
main:
	la $s5, vector # mi prendo l'indirizzo di memoria del vettore
	la $s6, n # mi prendo l'indirizzo di memoria di n

	lw $t0,24($s5) # prendo il settimo elemento (6*4) del vettore memorizzato all'indirizzo di memoria contenuto in $s5
	lw $t1,($s6)
	add $t0,$t1,$t0
	sw $t0, 48($s5)
