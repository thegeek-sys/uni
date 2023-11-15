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

import os

def translate_files(pretty_files: list):
#def translate_files(path: str):
    '''notes = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '-': 'b', '+': '#', ' ': 'P'}
    for file in pretty_files:
        with open(file, mode='rt') as file:
            pass

        with open(file, mode='wt') as file:
            pass'''
    notes = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '-': 'b', '+': '#', ' ': 'P'}
    out = ''
    for pretty_file in pretty_files:
        with open(pretty_file, mode='rt') as fr:
            fr = fr.read()
            no_duration = [notes[x] for x in fr if x in notes]
            no_duration.append('\n')
            srt = 0
            test = no_duration[0:2]
            i = 1
            while i < len(no_duration)-1:
                a,b = no_duration[srt:i],no_duration[srt:i+1]
                if no_duration[srt:i] != no_duration[srt:i+1] and (('#' not in test) and ('b' not in test)):
                    #dur = sum(c.isupper() for c in no_duration[srt:i])
                    dur=0
                    base = ''.join(no_duration[srt:i])
                    pattern = base
                    #print(pattern)
                    #print(no_duration[srt:i+dur*len(no_duration[srt:i])+1])
                    while pattern in ''.join(no_duration[srt:i+dur*len(no_duration[srt:i])+1]):
                        #print(no_duration[srt:i+dur*len(no_duration[srt:i])])
                        dur += 1
                        #print(pattern, ''.join(no_duration[srt:i+dur*len(no_duration[srt:i])+1]))
                        pattern += base
                        #print(dur*len(no_duration[srt:i]), pattern)
                    '''if dur > 1 and len(base) == 2 and no_duration[srt:i+dur*len(no_duration[srt:i])][-1] == base[0] and no_duration[srt:i+dur*len(no_duration[srt:i])][-2] == base[0]:
                        print('base == 2')
                        print(''.join(no_duration[srt:i+dur*len(no_duration[srt:i])]))
                        #del no_duration[i:i+len(pattern)-3]
                        del no_duration[i:i+dur*len(no_duration[srt:i])-2]
                    elif dur > 1 and len(base) == 1 and no_duration[srt:i+dur*len(no_duration[srt:i])][-1] == ('#' or 'b'):
                        print('base == 1')
                        print(''.join(no_duration[srt:i+dur*len(no_duration[srt:i])]))
                        del no_duration[i:i+len(pattern)-3]'''
                    l = no_duration[0:i+dur*len(no_duration[srt:i])-int(2 if len(base) == 2 else 1)]
                    #if dur > 1 and no_duration[i+dur*len(no_duration[srt:i])-int(2 if len(base) == 2 else 1)+1] == ('#' or 'b'):
                    #    dur = l.count(str(l[0]))-1
                    #    del no_duration[:i+dur*len(no_duration[srt:i])-int(2 if len(base) == 2 else 1)]
                    if dur > 1:
                        #l = no_duration[:i+dur*len(no_duration[srt:i])-int(2 if len(base) == 2 else 1)]
                        #print(base, no_duration[srt:i+dur*len(no_duration[srt:i])][-1], no_duration[srt:i+dur*len(no_duration[srt:i])][-2])
                        
                        #del no_duration[i:i+len(pattern)-int(2 if len(base)==1 else 4)]
                        del no_duration[0:i+dur*len(no_duration[srt:i])-int(2 if len(base) == 2 else 1)]
                        dur = l.count(str(l[0]))
                        print(dur)
                        print(''.join(l))
                        
                        
                        
                    #print(no_duration)
                    out += base
                    out += str(dur)
                    srt = i
                    test = no_duration[srt:i+2]
                else:
                    test = no_duration[srt:i-1]
                i+=1
    #print(''.join(no_duration))
    print()
    print(out)
    




def sanitize_txt(titles: dict, dest: str) -> list:
    pretty_files = []
    for title, path_rel in titles.items():
        #a = path_rel.index('/')
        path = dest + '/' + os.path.dirname(path_rel[path_rel.index('/')+1:])
        sanitized = []
        print('\n\n\n\n\n')
        with open(path_rel, mode='rt') as song:
            print(path_rel)
            song=song.readlines()
            for i in range(len(song)):
                sanitized.append(song[i][::-1])
            sanitized = ''.join([x.replace('\n','') for x in sanitized])
        
        #parent = f'{dest}/{path}'
        print(path, os.path.exists(path))
        os.makedirs(path, exist_ok=True)
        with open(f'{path}/{title}.txt', mode='wt') as song:
            song.write(sanitized)
        pretty_files.append(f'{path}/{title}.txt')
    return pretty_files
        
        

def get_titles_files(dir) -> dict[str,str]:
    titles = {}
    rel_path = f'{dir}/index.txt'
    with open(rel_path, mode='rt') as file_titles:
        file_titles = file_titles.read().split('\n')
        for tit_file in file_titles[:-1]:
            single = tit_file.split('" "')
            single[0], single[1] = single[0].replace('"', ''), single[1].replace('"', '')
            titles[single[0]] = f'{dir}/{single[1]}'
    return titles
        

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    titles = get_titles_files(source_root)
    pretty_files = sanitize_txt(titles, target_root)
    #final = translate_files(pretty_files)
    #print(final)

if __name__ == "__main__":
    #Umkansanize('test10', 'translated10')
    print(translate_files(['translated10\\The friendly erection distributes programming..txt']))
    '''
    res = ''
    for i in range(len(fr)-1):
        print((fr[i] == fr[i+1]), ((fr[i+1] == '-') and ('+' not in res)), ((fr[i+1] == '+') and ('-' not in res)), (fr[i+1] in res))
        print(fr[i], fr[i+1])
        if (fr[i] == fr[i+1]) or ((fr[i+1] == '-') and ('+' not in res)) or ((fr[i+1] == '+') and ('-' not in res)) or (fr[i+1] in res):
            res+=fr[i]
            #print(res)
        else:
            counter = sum(c.isdigit() or c.isspace() for c in to_replace)
            to_replace = set(x for x in res)
            #print(to_replace)
            to_replace = [notes[c] for c in to_replace]
            to_replace = sorted(to_replace, key=lambda elem:(not elem.isupper(), elem.islower(), elem))
            #print(to_replace)
            out += ''.join(to_replace)+str(counter)
            res = ''
    print(out)'''

