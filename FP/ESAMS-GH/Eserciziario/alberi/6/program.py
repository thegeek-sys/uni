'''
Si definisca la funzione es6(testo) ricorsiva (o che fa uso di funzioni o 
metodi ricorsive/i) che:
- riceve come argomento:
   - un insieme di stringhe che hanno la proprietà che ciascuna è stata 
   ottenuta a partire dallo stesso albero binario
      (in cui ciascun nodo contiene un solo carattere), risalendo da ciascuna 
      foglia fino alla radice e concatenando
      i valori dei nodi
      NOTA l'albero è localmente ordinato da sinistra a destra, ovvero:
      - ciascun figlio sinistro contiene un carattere minore di quello del padre
      - ciascun figlio destro contiene un carattere maggiore di quello del padre
- ricostruisce l'albero originale e lo torna come risultato

Esempio: se l'albero da ricostruire è
                  i     
                  |
          |-----------------|               
          h                 m 
          |                 |   
      |--------|        |------|   
      c        j        k      p
      |        |               |
   |-----|  |-----|         |-----|
   a     f  g     k         m     q    

L'insieme di stringhe è
   { 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }

ATTENZIONE: è VIETATO usare i metodi della classe AlberoBinario

'''

import albero

def aux(percorsi, tree, j=0, i=0):
    while j < len(percorsi)-1:
        while i < len(percorsi[j])-1:

            
            tree.sx = albero.AlberoBinario(aux(percorsi, tree, j, i+1))
            # tree.dx = albero.AlberoBinario(aux(percorsi, tree, j, i+1))
        return percorsi[j][i]
        j+=1
    
    
        
    

    

def es6(percorsi):
   # percorsi = [x[::-1] for x in percorsi]
   percorsi = sorted(percorsi)
   print(percorsi)
   tree = albero.AlberoBinario(percorsi[0][-1])
   a = aux(percorsi, tree)
   return tree


print(es6({ 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }))
