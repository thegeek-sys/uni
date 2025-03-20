.data
	N: .word 0:400	# matrice 7x7
	DIM: .word 20	# dimesione matrice

.text
main:
	li $t0,0	# x = 0
	li $t1,6	# x = 6
	li $t4,0	# y = 0
	lw $t2,DIM	# max i = 7
	li $s0,0	# sum diagonal
	
while1:
	bge $t0,$t2,while2
	mul $t3,$t0,$t2
	add $t3,$t3,$t0
	sll $t3,$t3,2
	lw $t3,N($t3)
	add $s0,$s0,$t3
	addi $t0,$t0,1
	j while1
	
while2:
	bge $t1,$t2,endWhile
	bge $t4,$t2,endWhile
	mul $t3,$t4,$t2
	add $t3,$t3,$t1
	sll $t3,$t3,2
	lw $t3,N($t3)
	add $s0,$s0,$t3
	subi $t1,$t1,1
	addi $t4,$t4,1
	j while2

endWhile:
	li $v0,1
	or $a0,$a0,$s0
	syscall
	li $v0,10
	syscall
	