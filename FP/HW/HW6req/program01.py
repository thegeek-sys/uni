#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
È una tranquilla serata di dicembre e mentre fuori piove a dirotto
ricevi una chiamata dalla tuo amico Bart, poco esperto di computer.
Dopo averlo calmato, ti racconta di essersi messo al
pc per cercare un regalo perfetto sull'onda del successo dei siti di
e-commerce alternativi, facendo ricerche sui siti più disparati
utilizzando un traduttore automatico. Ti racconta di essere finito
su un sito con il dominio .atp, pensando che avesse a che fare
con il tennis, sua grande passione. Dopo aver
seguito un paio di prodotti sullo strano sito, si è accorto che
il suo browser rispondeva più lentamente e il puntatore del mouse
cominciava ad andare a scatti. Dopo pochi secondi, gli è apparso un
messaggio di avvertimento che lo informava di essere stato
infettato da un ransomware di ultima generazione, che prende
di mira i file del pc. Colto dal panico, si è ricordato della
tua impresa con gli spartiti dei Tarahumara e ti ha chiamato
affinché lo aiuti a recuperare i suoi file. Il giorno dopo,
ti rechi a casa di Bart e analizzi la situazione: come pensavi,
il ransomware è il famigerato Burl1(ONE), che cifra i file del pc
memorizzando la chiave di cifratura all'interno delle immagini
con estensione .png, trasformandole in puzzle complicatissimi.
Poiché Bart memorizza le sue immagini su un servizio on cloud,
riesci a recuperare le immagini originali in modo da poter
risalire alla chiave di cifratura del ransomware. Riuscirai
a trovare tutte le chiavi? Bart conta su di te!

Il ransomware Burl1 memorizza la chiave di cifratura dividendo
in tasselli quadrati le immagini con estensione .png ed eseguendo
o meno delle rotazioni dei singoli tasselli di 90, 180 oppure 270°, 
ovvero eseguendo una, due o tre rotazioni a destra. La chiave avrà
rispettivamente una 'R' (right) una 'F' (flip) o una 'L' (left) a
seconda della rotazione fatta. L'assenza di rotazione indica il
carattere 'N'. Per ogni immagine è necessario ricostruire la chiave
di cifratura sotto forma di una lista di stringhe: ogni stringa
corrisponde alla sequenza di rotazioni di ogni tassello di una
riga. Per cui un'immagine 100x60 in cui i tasselli hanno dimensione
20 nasconderà una chiave di cifratura di 15 caratteri, organizzati
in tre stringhe da cinque caratteri ognuna. Infatti, ci saranno
5 tasselli per riga (100//20 = 5) e 3 righe (60//20 = 3).
Per scoprire le rotazioni eseguite devi utilizzare l'immagine
che hai recuperato dal cloud per eseguire il confronto con
l'immagine cifrata.

Devi scrivere la funzione
jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
che prende in ingresso 
- il nome del file contenente l'immagine con i tasselli ruotati, 
- il nome del file contenente l'immagine con i tasselli non ruotati, 
- un intero che indica la dimensione del lato dei tasselli quadrati, 
- il nome di un file di testo da decifrare con la chiave di cifratura 
- e il nome in cui salvare il file decifrato.

La funzione deve restituire la chiave di cifratura nascosta
nell'immagine in puzzle_image, ovvero la sequenza di
rotazioni da fare per ricostruire l'immagine iniziale e decifrare
il file in input.

Ad esempio, confrontando l'immagine in test01_in.png con test01_exp.png
e considerando i tasselli quadrati da 20 pixel, è possibile
stabilire che le rotazioni applicate sono state
            - 'LFR' per i tasselli della prima riga
            - 'NFF' per i tasselli della seconda riga e
            - 'FNR' per i tasselli della terza riga
            Per cui la chiave da ritornare sarà: ['LFR', 'NFF', 'FNR'].
            
La decifratura del file si ottiene attuando una trasformazione del
cattere in posizione i mediante il carattere della chiave in posizione
i modulo la lunghezza della chiave.

Ad esempio, se la chiave è ['LFR', 'NFF', 'FNR'], la chiave è lunga 9 
e bisogna decifrare il carattere in posizione 14 del file in input,
bisogna considerare il carattere in posizione 14%9 = 5 della chiave,
ovvero 'F'.
Le trasformazioni per la decifratura sono le seguenti:
    - R = text[i] sostituito dal carattere con ord seguente
    - L = text[i] sostituito dal carattere con ord precedente
    - N = resta invariato
    - F = swap text[i] con text[i+1]. Se i+1 non esiste, si considera 
          il carattere text[0].

Ad esempio, se la chiave di cifratura è LFR e il testo cifrato è BNVDCAP,
il testo in chiaro sarà AVOCADO, in quanto la decifratura è la seguente:

step     key      deciphering-buffer
1        LFR      BNVDCAP -> ANVDCAP
         ^        ^
2        LFR      ANVDCAP -> AVNDCAP
          ^        ^
3        LFR      AVNDCAP -> AVODCAP
           ^        ^
4        LFR      AVODCAP -> AVOCCAP
         ^           ^
5        LFR      AVOCCAP -> AVOCACP
          ^           ^
6        LFR      AVOCACP -> AVOCADP
           ^           ^
7        LFR      AVOCADP -> AVOCADO
         ^              ^

'''

# %%
import images

def get_tiles(im_or: list[list[tuple]], im_cryt: list[list[tuple]], n_r: int, n_c: int, tile_size: int) -> list[list[tuple]]:
    tile_or = []
    tile_cryt = []
    for r in range(n_r*tile_size,(n_r+1)*tile_size):
        row_or = im_or[r][n_c*tile_size:(n_c+1)*tile_size]
        tile_or.append(row_or)
        
        row_cryt = im_cryt[r][n_c*tile_size:(n_c+1)*tile_size]
        tile_cryt.append(row_cryt)
    return tile_or, tile_cryt

            
def check_rotation(tile_or: list[list[tuple]], tile_cryt: list[list[tuple]]) -> str:
    i = 0
    decod = ['N', 'R', 'F', 'L']
    while tile_cryt != tile_or:
        tile_cryt = [list(r) for r in zip(*tile_cryt[::-1])]
        #images.visd(tile_cryt)
        i += 1
    return decod[i]
        
def decryt(encrypted_file: str, decode_pattern: list[str], key_len: int) -> str:
    decode_raw = ''.join(decode_pattern)
    
    with open(encrypted_file, mode='rt', encoding='utf-8') as fr:
        fr = list(fr.read())
        l = len(fr)-1
        
        for i in range(len(fr)):
            key = decode_raw[i%key_len]
            if key == 'R':
                fr[i] = chr(ord(fr[i])+1)
            elif key == 'L':
                fr[i] = chr(ord(fr[i])-1)
            elif key == 'F' and i != l:
                s = fr[i]
                n = fr[i+1]
                fr[i] = n
                fr[i+1] = s
            elif key == 'F' and i == l:
                s = fr[i]
                n = fr[0]
                fr[i] = n
                fr[0] = s
    return ''.join(fr)
                
    

def jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
    im_or = images.load(plain_image)
    im_cryt = images.load(puzzle_image)
    
    tiles_rows = len(im_or)//tile_size
    tiles_cols = len(im_or[0])//tile_size
    key_len = tiles_rows*tiles_cols
    #print(key_len)
    
    #images.visd(im_or)
    #images.visd(im_cryt)
    
    decode_pattern = []
    for n_r in range(tiles_rows):
        decode_rows = ''
        for n_c in range(tiles_cols):
            tile_or, tile_cryt = get_tiles(im_or, im_cryt, n_r, n_c, tile_size)
            #images.visd(tile_or)
            #images.visd(tile_cryt)
            decode_rows += check_rotation(tile_or, tile_cryt)
        decode_pattern.append(decode_rows)
    #print(decode_pattern)
    decrytted = decryt(encrypted_file, decode_pattern, key_len)
    with open(plain_file, mode='wt', encoding='utf-8') as fw:
        fw.write(decrytted)
    
    return decode_pattern
    
    
    
            
if __name__ == '__main__':
    print(jigsaw('tests/test02_in.png', 'tests/test02_exp.png', 4,
                 'tests/test02_enc.txt', 'output/test02_out.txt'))

