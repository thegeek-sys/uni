import immagini as images
import json


def es23(fileJson, filePng):
    '''
    Abbiamo un file di tipo json contenente una matrice (lista di liste) M i cui elementi 
    sono stringhe. La matrice e' il risultato della codifica di un'immagine.
    L'immagine ha ampiezza w e altezza h dove w e' il numero di colonne della matrice M e h 
    il numero di righe. Il colore (r,g,b) del  pixel di coordinate x,y e' codificato con 
    la stringa presente in M[y][x], piu' precisamente la stringa e' composta da 9 cifre. 
    Le tre piu' significative sono la codifica di r, le tre centrali sono la codica di g e le tre 
    meno significative la codifica di b.  

    Scrivete la funzione es7(fileJson, filePng) che riceve come argomenti:
        :param fileJson: il path del file json dove si trova la matrice dell'immagine codificata
        :param filePng:  il path del file PNG dove salvare l'immagine decodificata.
        :return: il colore che appare piu' spesso tra quelli dei pixel dell'immagine (a parita'
        viene selezionato il colore che precede nell'ordinamento crescente 
        rispetto alla prima, alla seconda e poi alla terza coordinata).
    '''
    with open(fileJson, mode='rt') as fr:
        M = json.load(fr)
    
    colors = {}
    for row in range(len(M)):
        for col in range(len(M[0])):
            color = (int(M[row][col][0:3]), int(M[row][col][3:6]), int(M[row][col][6:]))
            colors[color] = colors.get(color, 0) + 1
            M[row][col] = color
    
    images.save(M, filePng)


    # return sorted(M, key=lambda x: (-M.count(x), x[0], x[1], x[2]))[0]
    if list(colors.values()).count(max(list(colors.values()))) > 1:
        c = []
        for k, v in colors.items():
            if v == max(list(colors.values())):
                c.append(k)
        return sorted(c, key=lambda x: (x[0], x[1], x[2]))[0]

    return list(colors.keys())[list(colors.values()).index(max(list(colors.values())))]
    
    
# print(es23('italia.json', 'pippo.png'))