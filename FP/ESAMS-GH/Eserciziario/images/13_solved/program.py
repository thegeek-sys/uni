import immagini as images

'''    
    Es 12: 4 punti
    Progettare la  funzione es13(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e  fimm1 di due file .PNG. 
    - legge l'immagine da fimm ne modifica i colori dei pixel e  la salva poi 
      all'indirizzo fimm1.
    - restituisce infine il numero di colori DIFFERENTI presenti nell'immagine modificata.
      I colori dei pixel dalla nuova immagine si ottengono a partire da quelli 
      dell'immagine originaria con la seguente  procedura:.
      le tuple dei DIFFERENTI colori presenti nella prima immagine vengono ordinate in 
      ordine crescente.
      La sequenza ordinata di tuple  che si ottiene viene suddivisa a gruppi di 50 (se il 
      numero totale di tuple non e' un multiplo di 50 allora l'ultimo gruppo avra' 
      meno di 50 elementi). 
      I colori corrispondenti alle tuple che compaiono come  primo elemento di 
      ciascun gruppo saranno i colori assegnati ai pixel dell'immagine.
      tutti i pixel che avevano colori corrispondenti a tuple finite in uno stesso 
      gruppo avranno come colore quello corrispondente alla prima tupla del gruppo.
      Ad esempio i pixel che avevano colori corrispondenti alle tuple finite nelle prime 50 posizioni 
      della sequenza ordinata  avranno ora tutti lo stesso colore (dato dal colore corrispondente 
      alla tupla che occupa la prima posizione  della sequenza), i pixel 
      che avevano colori le cui tuple  nella sequenza occupano le posizioni 
      da 50 a 99 avranno tutti lo stesso  colore (corrispondente alla tupla in posizione  
      50) ecc. ecc. 
      Sull'immagine Fig1.png la funzione deve produrre il file RisFig1.png e restituire il numero ?
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
def es13(fimm,fimm1):
    img = images.load(fimm)
    colors = sorted(set(img[row][col] for row in range(len(img)) for col in range(len(img[0]))))
    
    lcolors, p = [], []
    for x in colors:
        p.append(x)
        if len(p)%50 == 0:
            lcolors.append(p)
            p = []
    if p != []:
        lcolors.append(p)
    
    for row in range(len(img)):
        for col in range(len(img[0])):
            ori = img[row][col]
            color = [ x[0] for x in lcolors if ori in x ]
            img[row][col] = color[0]
    images.save(img, fimm1)
    
    return len(lcolors)
                
    
# print(es13('Foto3.png', 'pippo.png'))