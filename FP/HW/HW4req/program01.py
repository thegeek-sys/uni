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

def translate_files(pretty_files: list, target_root: str) -> dict[str:str]:
    notes = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '-': 'b', '+': '#', ' ': 'P'}
    duration = {}
    for file, song in pretty_files.items():
        out = ''
        #with open(song, mode='rt', encoding='utf-8') as fr:
        #fr = fr.read()
        no_duration = [notes[x] for x in song if x in notes]
        no_duration.append('\n')
        srt = 0
        test = no_duration[0:2]
        i = 1
        while i <= len(no_duration)-1:
            a = no_duration[srt:i]
            if a != no_duration[srt:i+1] and (('#' not in test) and ('b' not in test)):
                dur=0
                base = ''.join(a)
                pattern = base
                while pattern in ''.join(no_duration[srt:i+dur*len(a)+1]):
                    dur += 1
                    pattern += base
                indices = [i for i in range(srt,i+dur*len(a)-int(2 if len(base) == 2 else 1))]
                if (no_duration[indices[-1]+1] == '#' and '#' not in base) or (no_duration[indices[-1]+1] == 'b' and 'b' not in base):
                    dur -= 1
                    indices.pop()
                if dur > 1:
                    rem = []
                    for x in sorted(indices, reverse=True):
                        rem.append(no_duration.pop(x))
                    dur = rem.count(str(rem[-1]))
                    i-=int(2 if len(base)==2 else 1)

                out += base+' '+str(dur)+' '
                srt = i
                test = no_duration[srt:i+2]
            else:
                test.clear()
            i+=1
        with open(file, mode='wt', encoding='utf-8') as fw:
            fw.write(out.replace(' ',''))

        duration[os.path.splitext(os.path.basename(file))[0]] = sum([int(s) for s in out.split() if s.isdigit()])

    return duration


def sanitize_txt(titles: dict, dest: str) -> list:
    #pretty_files = []
    pretty_files = {}
    for title, path_rel in titles.items():
        path = dest + '/' + os.path.dirname(path_rel[path_rel.index('/')+1:])
        sanitized = []
        with open(path_rel, mode='rt', encoding='utf-8') as song:
            song=song.readlines()
            for i in range(len(song)):
                sanitized.append(song[i][::-1])
            sanitized = ''.join([x.replace('\n','') for x in sanitized])
        
        os.makedirs(path, exist_ok=True)
        
        with open(f'{path}/{title}.txt', mode='wt', encoding='utf-8') as song:
        #with open(os.path.join(path, title+'.txt'), mode='wt', encoding='utf-8') as song:
            song.write(sanitized)
        #pretty_files.append(f'{path}/{title}.txt')
        pretty_files[f'{path}/{title}.txt'] = sanitized
    return pretty_files
        
def get_titles_files(directory: str) -> dict:
    titles = {}

    with open(f'{directory}/index.txt', mode='rt', encoding='utf-8') as file_titles:
        for line in file_titles:
            title, path_rel = map(lambda x: x.strip('"'), line.strip().split('" "'))
            titles[title] = f'{directory}/{path_rel}'

    return titles
        

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    titles = get_titles_files(source_root)
    pretty_files = sanitize_txt(titles, target_root)
    duration = translate_files(pretty_files, target_root)

    with open(f'{target_root}/index.txt', 'wt', encoding='utf-8') as index:
        duration = dict(sorted(duration.items(), key=lambda item: (-item[1], item[0])))
        for name, lenght in duration.items():
            print(f'"{name}" {lenght}', file=index)
    return duration

if __name__ == "__main__":
    Umkansanize('test03', 'translated03')
    ##print(translate_files(['translated10\\The friendly erection distributes programming..txt']))