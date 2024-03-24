.data
	matrice2D: .word 0:400	# matrice quadrata 20x20 word
	DIM: .word 20		# lato della matrice
	Sum: .word 0
	
.text
main:	li $t0,0	# x
	li $t1,0	# y
	lw $s0,DIM	# max i
	li $s1,0	# sum
	
for:	bge $t0,$s0,endFor	# while x<20
	bge $t1,$s0,endFor	# while y<20
	
	mul $t3,$t1,$s0		# t3=2*y
	add $t3,$t3,$t0		# t3+x
	sll $t3,$t3,2		# t3*4
	lw $t4,matrice2D($t3)	# t4=matrice2D[t3]
	add $s1,$s1,$t4		# sum+=t4
	addi $t0,$t0,1		# x++
	addi $t1,$t1,1		# y++
	j for
	
endFor:
	sw $s1,Sum
