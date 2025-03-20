##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    	buffer: .space 20
    	#buffer: .asciiz "10145\n"

.text

main:
    	li $v0, 8       # Codice per input stringa
    	la $a0, buffer  # Carica indirizzo base in $a0
    	li $a1, 20      # Alloca al massimo 20 caratteri
    	syscall         # $a0 contiene l'indirizzo base della stringa


	li $s0,0	# valore cifre prese 2 a 2
	li $s1,0	# num caratteri

	add $t0,$t0,$a0
contaChar: 
	lb $t1,($t0)
	beq $t1,0xA,contaOccorrenze
	addi $s1,$s1,1
	addi $t0,$t0,1
	j contaChar



contaOccorrenze:
	lb $t1,($a0)
	beq $t1,0xA,esci
	subi $t1,$t1,0x30
	move $t9,$a0
	addi $t9,$t9,1
	lb $t9,($t9)
	if: beq $t9,0xA,else
		mul $t1,$t1,10
		addi $a0,$a0,1
		lb $t0,($a0)
		subi $t0,$t0,0x30
		add $s0,$s0,$t1
		add $s0,$s0,$t0
		addi $a0,$a0,1
		j contaOccorrenze
	else:
		add $s0,$s0,$t1
		addi $a0,$a0,1
		j contaOccorrenze
	

esci:
	li $v0,1
	move $a0,$s0
	syscall
	
	li $v0,11
	li $a0,0xA
	syscall
	
	li $v0,1
	move $a0,$s1
	syscall
	
	move $v0,$s0
	move $v1,$s1
	