

import immagini as images
def es15(fimm1,fimm2,fimm3):
    '''    
    Es 3: 6 punti
    Si definisca la  funzione es3(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
      La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
      Per quanto riguarda i colori dei pixel della nuova immagine:
      il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
      le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore 
      del pixel dell'unica immagine originaria in cui e' presente.
      (guardate le immagini di test per chiarimenti)
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    im1, im2 = images.load(fimm1), images.load(fimm2)
    
    img = [ [ (0,)*3 ]*max(len(im1[0]), len(im2[0])) for _ in range(max(len(im1), len(im2))) ]
    
    x1, x2, y1, y2 = len(im1[0]), len(im2[0]), len(im1), len(im2)
    
    i = 0
    for row in range(len(img)):
        for col in range(len(img[0])):
            if (row < y1 and row < y2 and col < x1 and col < x2) or (row > y1 and row > y2 and col > x1 and col > x2):
                img[row][col] = (0,0,0)
            elif row < y1 and col < x1:
                img[row][col] = im1[row][col]
            elif row < y2 and col < x2:
                img[row][col] = im2[row][col]
            if img[row][col] == (0,0,0):
                i+=1
    images.save(img, fimm3)
    
    return i

print(es15('foto1.png','foto2.png','pippo.png'))



