##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    #buffer: .asciiz "06845\n"
    buffer: .space 26
    output: .byte  0,0,0,0,0,0,0,0,0  # Un carattere extra per la fine della stringa

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    syscall         # $a0 contiene l'indirizzo base della stringa
    la $a2, output
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

li $v0,0 # multipli di 2
li $v1,0 # multipli di 4

lb $t0,($a0)
for: beq $t0,'\n',exit
	subi $t0,$t0,0x30
	beqz $t0,ugualeZero
	andi $t1,$t0,1
	
	bnez $t1,ugualeZero
	addi $v0,$v0,1

	srl $t0,$t0,1
	andi $t1,$t0,1
	bnez $t1,fin
	addi $v1,$v1,1
	
	fin:
	addi $a0,$a0,1
	lb $t0,($a0)
	j for
	
	
ugualeZero:
	addi $a0,$a0,1
	lb $t0,($a0)
	j for

exit:
	move $t0,$v0
	li $v0,1
	move $a0,$t0
	syscall
	
	li $v0,11
	li $a0,'\n'
	syscall
	
	li $v0,1
	move $a0,$v1
	syscall
	
	li $v0,10
	syscall
