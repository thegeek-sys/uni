##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26
    #buffer: .asciiz "101101111\n"
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

li $t7,0
li $t1,0

for:
	li $v0,0	# multiplo di tre
	lb $t0,($a0)
	beq $t0,'\n',endFor
	sub $t0,$t0,0x30
	sll $t0,$t0,2
	add $t7,$t7,$t0
	addi $a0,$a0,1
	addi $v1,$v1,1
	
	li $v0,1
	lb $t0,($a0)
	beq $t0,'\n',skip
	sub $t0,$t0,0x30
	sll $t0,$t0,1
	add $t7,$t7,$t0
	addi $a0,$a0,1
	
	lb $t0,($a0)
	beq $t0,'\n',skip
	sub $t0,$t0,0x30
	add $t7,$t7,$t0
	addi $a0,$a0,1
	
	add $t7,$t7,0x30	# trasformo in ASCII
	sb $t7,output($t1)
	addi $t1,$t1,1
	move $t7,$zero
	
	j for

skip:
	add $t7,$t7,0x30	# trasformo in ASCII
	sb $t7,output($t1)

endFor:
	add  $t0,$0,$v0
	
	li $v0,4
	move $a0,$a2
	syscall
	
	li $v0,11
	li $a0,'\n'
	syscall
	
	
	li $v0,1
	move $a0,$t0
	syscall
	
	
	li $v0,11
	li $a0,'\n'
	syscall
	
	li $v0,1
	move $a0,$v1
	syscall
	
	#move $v0,$t0
	
	li $v0,10
	syscall
	
	
	
	