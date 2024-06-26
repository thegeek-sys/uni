
import immagini as images

def es42(fImageIn, fcolori, fImageOut):
    '''
    Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
    modifica il colore di alcuni pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
    modificata  in un nuovo file PNG FImageOut.
    La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
    I colori da modificare sono specificati dal file di testo fcolori.
    Il file fcolori ha tante righe quanti sono i colori da modificare.
    Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
    I primi tre indicano il colore da modificare
    e i secondi tre il nuovo colore
    Ad esempio la presenza eventuale della riga
    0 0 0  255 255 255
    indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
    assumere colore bianco (i.e. devono assumere colore (255,255,255)).

    NOTA: i colori devono essere sostituiti contemporaneamente
    (e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

    :param fImageIn: nome del file PNG contenente l'immagine da modificare
    :param fcolori: nome del file di testo in cui trovare i colori da modificare
    :param fImageOut: nome del file PNG in cui salvare l'immagine modificata
    :return: numero di pixel modificati
    '''
    
    img = images.load(fImageIn)
    with open(fcolori, mode='rt') as fr:
        colors = {}
        for line in fr:
            colors[tuple(int(x) for x in line.split()[0:3])] = tuple(int(x) for x in line.split()[3:])
    
    i = 0
    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] in colors:
                img[row][col] = colors[img[row][col]]
                i+=1
                
    images.save(img, fImageOut)
    return i
