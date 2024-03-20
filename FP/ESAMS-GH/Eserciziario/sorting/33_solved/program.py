
def es33(fname1,fname2):
    ''' 
    Implementate la funzione es33(fname1,fname2) prende in input l'indirizzo di un  file di testo fname e
    costruisce un istogramma con le frequenze di alcuni dei caratteri presenti nel  file di testo. 
    Salva l'istogramma creato nel file di testo fname2 e restituisce il numero di linee di cui e' composto.
    L'istogramma contiene tante linee quanti sono i caratteri tra 'a' e 'z' presenti nel testo.
    Se un certo carattere x compare nel testo  y volte allora nell'istogramma ci sara' 
    una riga con una stringa composta dal carattere x ripetuto y volte. Le righe dell'istogramma 
    vanno ordinate per lunghezza decrescente dei caratteri che vi compaiono e 
    lessicograficamente a parita' di lunghezza.
    Ad esempio se il file fname1 contiene il testo 'Monti, Sterbini e Spognardi' allora
    il valore restituito dalla funzione sara' 11 e  l'istogramma sara'
    iiii
	nnn
	ee
	oo
	rr
	tt
	a
	b
	d
	g
	p
    '''
    
    words = {}
    with open(fname1, mode='rt') as fr:
        fr = ''.join([ x for x in fr.read() if x.isalpha() and x.islower() ])
        for x in fr:
            words[x] = words.get(x, 0) + 1
    
    words = sorted([ k*v for k,v in words.items() ], key=lambda x: (-len(x), x))
    with open(fname2, mode='wt') as fr:
        for word in words:
            fr.write(word+'\n')

    return len(words)

print(es33('ftesto3.txt', 'istogramma1.txt'))
    











 