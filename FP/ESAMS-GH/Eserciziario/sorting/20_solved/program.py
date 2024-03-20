def es20(stringa1):
    '''
    Es 3: 4 punti
    Si consideri l'ordine alfabetico delle 21 lettere dell'alfabeto italiano:
    A – B – C – D – E – F – G – H – I – L – M – N – O – P – Q – R – S – T – U – V – Z
    definiamo valore di una lettera la posizione che occupa in quest'ordine a partire da 1
    (ad esempio il valore di A e' 1 mentre il valore di Z e' 21). 
    La funzione  es3(stringa1) presa la stringa stringa1 
    contenente parole sull'alfabeto italiano separate da uno spazio, restituisce la stringa 
    che si ottine sostituendo a ciasuna parola presente in  stringa1 
    la stringa numerica che si ottiene sommando  il valore delle lettere che compongono la parola.
    Non si distingue tra lettere maiuscole e minuscole).
    Ad esempio con stringa1='Angelo Monti Andrea Sterbini e Angelo Spognardi' la funzione restituira' 
    la stringa '48 63 39 88 5 48 93'
    '''
    alf = 'abcdefghilmnopqrstuvz'
    stringa1 = stringa1.split()
    s = []
    for i in range(len(stringa1)):
        for j in range(len(stringa1[i])):
            if len(s) == i+1:
                s[i] += alf.index(stringa1[i][j].lower())+1
            else:
                s.append(alf.index(stringa1[i][j].lower())+1)
    return ' '.join([str(x) for x in s])
    
    
# print(es20('Angelo Monti Andrea Sterbini e Angelo Spognardi'))