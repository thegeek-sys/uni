.data
vector:	.word 4, -1, 5, 500, 0, 10000, -256
N: 	.word 5
Somme: 	.word 0, 0

.text
	la $a1, Somme
	li $t0,0		# i = 0
	ori $t1,$zero,1		# j = 1
	lw $t2,N		# N -> $t2
	xor $s0,$s0,$s0		# even
	xor $s1,$s1,$s1		# odd

for0: bge $t0,$t2,for1
	sll $t4,$t0,2		# i*4
	lw $t5,vector($t4)	# vector[i]
	add $s0,$s0,$t5		# even*=vector[i]
	addi $t0,$t0,2		# i+=2
	j for0

for1: bge $t1,$t2,endFor
	sll $t4,$t1,2		# j*4
	lw $t5,vector($t4)	# vector[j]
	add $s1,$s1,$t5		# odd*=vector[j]
	addi $t1,$t1,2		# j+=2
	j for1
endFor:

# sw $s0,Somme + 0
# sw $s1,Somme + 4
sw $s0,0($a1)
sw $s1,4($a1)

