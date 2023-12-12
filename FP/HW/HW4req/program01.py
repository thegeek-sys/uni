#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ajeje la bibliotecaria ha recentemente trovato una stanza nascosta
nella biblioteca di Keras (un posto fantastico situato in
Umkansa, il villaggio più grande delle Montagne Bianche).
Lì ha scoperto diversi libri contenenti
spartiti musicali di antiche canzoni Tarahumara e ha,
quindi, invitato un amico musicista a dare un'occhiata.
Il musicista le ha detto che è una scoperta sensazionale,
dato che gli spartiti sono scritti in notazione Tarahumara,
una popolazione ormai estinta, ma molto famosa per 
aver influenzato i musicisti della Sierra Nevada. Per poter
riprodurre i brani le suggerisce di farli tradurre in una
notazione familiare ai musicisti Umkansaniani, ultimi
discendenti dei Tarahumara, in modo che possano riprodurli.

I Tarahumara scrivevano le note usando numeri invece di lettere:
0 al posto di A, 1 al posto di B e così via, fino a 7 al posto di G. 
Le note bemolle (b) e diesis (#)
(vedi la nota 3 sotto, se non sai cosa sono bemolle e diesis)
erano seguite rispettivamente da un - e da un + 
(ad esempio, 0- significa A bemolle). 
Inoltre, ripetevano semplicemente lo stesso numero più volte 
per rappresentare la durata della nota. 
Ad esempio, 0000 significa che la nota A ha una lunghezza di 4, 
mentre 0-0-0-0- significa che la nota A bemolle ha una lunghezza di 4.

Le pause venivano scritte come spazi:
ad esempio, dodici spazi rappresentano una pausa lunga 12. 
Sia le note che le pause potevano estendersi su
diverse linee della partitura (ad esempio, iniziando dalla linea
x e continuando sulla riga x+1, x+2 e così via).
Infine, gli spartiti musicali erano scritti da destra
a sinistra e dall'alto verso il basso, mentre andare accapo 
non significava nulla in termini di partitura musicale.

Gli Umkansaniani, invece, sono soliti scrivere le note utilizzando lettere,
e ogni nota è seguita dalla sua durata (quindi, l'esempio
sopra verrebbe scritto come A4). 
Le note bemolle e diesis sono seguite rispettivamente 
da una 'b' o da una '#' (ad esempio, A bemolle è scritto Ab, 
quindi l'esempio sopra verrebbe scritto ad Ab4). 
Le pause vengono scritte utilizzando la lettera P, seguita dalla 
loro durata e non viene utilizzato alcuno spazio.
Infine, gli Umkansaniani sono abituati a leggere la musica da
sinistra a destra, scritta su una singola riga.

Poiché Ajeje sa che sei un abile programmatore, 
ti fornisce una cartella contenente la trascrizione
di tutte le canzoni di Tarahumara che ha trovato, 
organizzate in più sottocartelle e file (un brano per file).
Inoltre, ha preparato un file indice in cui ogni riga
contiene il titolo di una canzone Tarahumara (tra virgolette),
seguito da uno spazio e dal percorso del file contenente
quella canzone (tra virgolette, relativa alla cartella principale).
Vorrebbe tradurre tutte le canzoni elencate nell'indice e 
salvarle in nuovi file, ciascuno denominato con il titolo 
della canzone che contiene (con estensione .txt),
in una struttura di cartelle corrispondente a quella originale.
Inoltre, vorrebbe archiviare nella cartella principale della
struttura creata un file indice contenente su ogni riga
il titolo di una canzone (tra virgolette) e la corrispondente
lunghezza del brano, separati da uno spazio. 
Le canzoni nell'indice devono essere ordinate per lunghezza decrescente e, 
se la durata di alcuni brani è la stessa, in ordine alfabetico ascendente. 
La durata di una canzone è la somma delle durate
di tutte le note e delle pause di cui è composta.

Sarai capace di aiutare Ajeje nel tradurre le canzoni
Tarahumara in canzoni Umkansaniane?

Nota 0: di seguito viene fornita una funzione per
Umkansanizzare le canzoni di Tarahumara; 
dopo essere stata eseguita, deve restituire un dizionario 
in cui ogni chiave è il titolo di una canzone
ed il valore associato è la durata del brano.

Nota 1: l'indice delle canzoni da tradurre è il file 'index.txt'
che si trova nella directory passata nell'argomento source_root

Nota 2: l'indice delle canzoni tradotte è il file 'index.txt'
che deve essere creato nella directory passata nell'argomento target_root

Nota 3: le note bemolle e diesis sono solo versioni "alterate".
di note regolari; per esempio un A# ("A diesis") è la
versione alterata di un A, cioè una nota A che è un
mezzo tono più alto del A regolare; lo stesso vale per
note bemolle, che sono mezzo tono più basse delle note normali;
dal punto di vista dei compiti, note bemolle e diesis
devono essere trattate allo stesso modo delle note regolari 
(ad eccezione della loro notazione).

Nota 4: Usiamo la notazione inglese delle note A B C D E F G.

Nota 5: potete usare le funzioni della libreria 'os' per creare le directory necessarie
(ad esempio os.makedirs)
'''


import builtins
if 'profile' not in dir(builtins):
    def profile(X) : return X

import os

#@profile
def count_segno(i, nota, no_duration, durata):
    while no_duration[i:i+2] == nota:
        durata += 1
        i+=2
    return durata, True, nota, i

#@profile
<<<<<<< HEAD
def count_same(i, no_duration, nota):
    same = True
    j = 1
    while j+1 <= len(no_duration)-1 and no_duration[j] == nota and no_duration[j+1] not in '#b':
        j += 1
    return j, same, j+i, nota
    

#@profile
def translate_files(pretty_files: dict, translation_table) -> dict[str:str]:
    
=======
def count_same(i, no_duration, nota, l):
    j = i
    while i<l and no_duration[i+1] not in '#b' and no_duration[i] == nota:
        i += 1
    return i-j, True, i, nota
    

#@profile
def translate_files(pretty_files: dict, translation_table: str) -> dict[str:str]:
>>>>>>> 4a6cb4c023f1bdee192205cdb0b4a8b1695a758e
    duration = {}
    for file, song in pretty_files.items():
<<<<<<< HEAD
        print(file)
        out = nota = ''
        no_duration = str(song.translate(translation_table))
        no_duration += '\n\n'
        i= durata = 0
        segno=same=False
        total = 0
        while i < len(no_duration)-1:
            if no_duration[i] == no_duration[i+1] and not segno and not same:
                durata, same, i, nota = count_same(i, no_duration[i:], no_duration[i])
            elif no_duration[i+1] in '#b' and not same and not segno:
                durata, segno, nota, i = count_segno(i, no_duration[i]+no_duration[i+1], no_duration, durata)
=======
        out = ''
        no_duration = str(song.translate(translation_table))+'\n\n'
        i = durata = total = 0
        segno = same = False
        l = len(no_duration)-1
        while i < l:
            if no_duration[i] == no_duration[i+1] and segno==same==False:
                durata, same, i, nota = count_same(i, no_duration, no_duration[i], l)                
            elif no_duration[i+1] in '#b' and segno==same==False:
                durata, segno, nota, i = count_segno(i, no_duration[i:i+2], no_duration, durata)
>>>>>>> 4a6cb4c023f1bdee192205cdb0b4a8b1695a758e
            else:
                if segno or same:
                    out += nota+str(durata)
                    total += durata
                    durata = 0
                    segno=same=False
                else:
                    out += no_duration[i]+'1'
                    total += 1
                    i+=1
        with open(file, mode='wt', encoding='utf-8') as fw:
            fw.write(out.rstrip())

<<<<<<< HEAD
        duration[file.split('/')[-1].replace('.txt','')] = total
        #print(os.path.basename(file))
        #duration[os.path.basename(file).replace('.txt','')] = total
    #return out, total
=======
        duration[os.path.basename(file)[:-4]] = total
>>>>>>> 4a6cb4c023f1bdee192205cdb0b4a8b1695a758e
    return duration


#@profile
def sanitize_txt(source: str, titles: dict, dest: str) -> list:
    pretty_files = {}
    for title, path_rel in titles.items():
        dir_name = os.path.dirname(path_rel)
        file_name = os.path.basename(path_rel)
        path = f'{dest}/{dir_name}'
        
        os.makedirs(path, exist_ok=True)
<<<<<<< HEAD
        #path += '/'+title+'.txt'
        
        with open(f'{source}/{dir_name}/{file_name}', mode='rt', encoding='utf-8') as song:
            sanitized = ''.join(line[::-1].replace('\n', '') for line in song)
        
        #pretty_files[os.path.join(path, f'{title}.txt')] = sanitized
=======
        
        with open(f'{source}/{dir_name}/{file_name}', mode='rt', encoding='utf-8') as song:
            sanitized = ''.join(line[::-1].strip('\n') for line in song)
    
>>>>>>> 4a6cb4c023f1bdee192205cdb0b4a8b1695a758e
        pretty_files[f'{path}/{title}.txt'] = sanitized

    return pretty_files

#@profile
def get_titles_files(directory: str) -> dict:
    titles = {}

    with open(f'{directory}/index.txt', mode='rt', encoding='utf-8') as file_titles:
        for line in file_titles:
            title, path_rel = map(lambda x: x.strip('"'), line.strip().split('" "'))
            titles[title] = path_rel

    return titles

#@profile    
def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    notes = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '-': 'b', '+': '#', ' ': 'P'}
    translation_table = str.maketrans(notes)
    
    titles = get_titles_files(source_root)
    pretty_files = sanitize_txt(source_root, titles, target_root)
    duration = translate_files(pretty_files, translation_table)

    with open(f'{target_root}/index.txt', 'wt', encoding='utf-8') as index:
        duration = dict(sorted(duration.items(), key=lambda item: (-item[1], item[0])))
        for name, lenght in duration.items():
            print(f'"{name}" {lenght}', file=index)
    return duration

if __name__ == "__main__":
    #with open('test02/0.txt', mode='rt', encoding='utf-8') as song:
    #    sanitized = ''.join(line[::-1].strip('\n') for line in song)
    #print(sanitized)
    Umkansanize('test10', 'translated10')
    #print(translate_files({'':'1 4- 52-2 4+  111  5552-2-2-6 1-1-3-3-11   4-4-66   6+4-4-55500 6  2-1-1-1-6   333  333  4-4-4-2-   6+6+666 0+0+   555 2225- 3+3+6666'}))
    #pass