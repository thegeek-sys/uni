.data
	vettore: .word 1,2,3,4,5,6,7,8,9
	N: .word 9
	Somma: .word 0
.text
  main:	la	$t0,vettore		# indirizzo vettore
  	lw	$t1,N 			# len(vettore)
  	sll	$t1,$t1,2		# offset fine
  	add 	$t1,$t1,$t0		# indirizzo fine
  	li	$s0,0
  loop:	bge 	$t0,$t1,endLoop
  	lw 	$t2,($t0)		# vettore[i]
  	add 	$s0,$s0,$t2		# somma+=vettore[i]
  	addi 	$t0,$t0,12		# i+=3*4
  	j loop
  endLoop:
  	sw 	$s0,Somma