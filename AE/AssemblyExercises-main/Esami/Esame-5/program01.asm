##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20
    #buffer: .asciiz "1123455\n"

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 20      # Alloca al massimo 20 caratteri
    syscall         # $a0 contiene l'indirizzo base della stringa


##########################################
## INSERIRE IL CODICE QUI
   
li $v0,0 # identico
li $v1,0 # somma

lb $s0,($a0)
addi $a0,$a0,1
lb $t0,($a0)

add $v1,$v1,$s0
sub $v1,$v1,0x30

for: beq $t0,'\n',exit
	bne $t0,$s0,skip
	addi $v0,$v0,1
	skip:
	add $v1,$v1,$t0
	sub $v1,$v1,0x30
	
	move $s0,$t0
	addi $a0,$a0,1
	lb $t0,($a0)
	j for

exit:
	move $a0,$v0
	li $v0,1
	syscall
	
	li $a0,'\n'
	li $v0,11
	syscall
	
	move $a0,$v1
	li $v0,1
	syscall

	li $v0,10
	syscall





