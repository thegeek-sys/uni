import albero


def es48(tree):
    '''
    Si definisca la funzione es48(tree) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
    - riceve come argomento 'tree' un  albero  formato da nodi di tipo
      AlberoBinario definito nella libreria albero.py allegata
    - calcola il numero di nodi che nell'albero hanno ESATTAMENTE due figli
    - torna come risultato il numero calcolato
    Esempio: se l'albero e':

             7
            /\
           1  3
          / \
        4    6
       /    /
      5    2
     /     \
    9       8

    Nell'albero ci sono solo due nodi con esattamente due figli (il nodo con valore 7 ed il nodo
    con valore 1) cosi'  la funzione tornera' il valore 2.
    '''

    n = 0
    if tree.sx and tree.dx:
        n += 1
    
    n+= es48(tree.sx) if tree.sx else 0
    n+= es48(tree.dx) if tree.dx else 0
    
    return n
        
     
