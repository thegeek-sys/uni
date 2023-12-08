#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Il tuo caro amico Pico de Paperis ti ha mandato un messaggio molto strano scarabocchiato su una cartolina.
Ê da tanto che non lo vedi e da sempre vi divertite a scrivervi in codice.
Per decodificare il suo messaggio vai a cercare nella tua biblioteca un libro un po' particolare,
il cifrario di Archimede Pitagorico. Il cifrario da applicare è la famosa "Cifra del Faraone".
La decifrazione col metodo del Faraone si basa su delle regole di sostituzione di sequenze di simboli nel testo.
Il motivo per cui si chiama "cifra del Faraone" è che in antico Egizio le sequenze formate da più geroglifici
potevano essere scritte in qualsiasi ordine, quindi ogni anagramma delle sequenze era valido.
Per rendere la cosa più strana, Pico de Paperis ha deciso di usare un cifrario che non è esattamente quello del
Faraone, ma una sua variante. Invece di usare gli anagrammi usa dei "quasi anagrammi", cioè anagrammi che nel testo
originale hanno un carattere spurio in più rispetto alla sequenza cercata.
Nel cifrario sono contenute coppie di sequenze che indicano come trasformare il testo.
Ad esempio la coppia 'shampoo' -> 'soap' corrisponde a cercare un punto del messaggio in cui appare la sequenza 'shampoo'
(o un suo anagramma) ma con un carattere in più (ad esempio 'pmQohaso') e sostituirla con la sequenza 'soap'.

La decodifica del messaggio può portare a più possibili messaggi finali, perchè possono esserci più sequenze nel testo
che possono essere trasformate in ogni momento e l'ordine delle trasformazioni influenza le trasformazioni successive.
Ad un certo punto succederà che nessun "quasi-anagramma" delle sequenze del cifrario è presente in nessun punto
della sequenza di simboli per cui non è più possibile fare trasformazioni.
Queste sequenze le chiamiamo sequenze finali.
Di tutte le possibili sequenze finali,ci interessa l'insieme delle più corte.

Per decodificare il messaggio di Pico de Paperis devi implementare la funzione
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
che riceve come argomenti:
- il testo che ti ha mandato Pico de Paperis, come stringa di simboli (caratteri)
- il cifrario da applicare, un dizionario che ha come chiavi le sequenze di cui cercare nel testo un quasi-anagramma
   e come valore associato la stringa da sostituire al quasi-anagramma trovato.
la funzione deve tornare l'insieme dei più brevi testi ottenibili applicando ripetutamente
le trasformazioni fin quando non è più possibile applicarne nessuna.

Esempio:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Risultato: {'tmeopcus', 'metopcus', 'ameopcus', 'atmepcus'}
e tutte le trasformazioni applicate sono quelle contenute nel file example.txt
(in ordine alfabetico e senza ripetizioni)

NOTA: almeno una delle funzioni o metodi che realizzate deve essere ricorsiva
NOTA: la funzione/metodo ricorsivo/o deve essere definita a livello più esterno
      altrimenti fallirete il test di ricorsione.
'''
#import json

'''def translate(encrypted, original, new):
    l = len(original)+1
    #original = list(original)
    translated = list(encrypted)
    print(original)
    i = 0
    while i < len(translated):
        #print(''.join(translated[i:i+l]))
        if all(x in list(translated[i:i+l]) for x in original):
            translated[i:i+l] = new
        i += 1
    return ''.join(translated)

def recurs(encrypted_list, pharaohs_cypher):
    for encrypted in encrypted_list:
        for k, v in pharaohs_cypher.items():
            l = len(k)+1
            translated = list(encrypted)
            #print(k)
            i = 0
            while i < len(translated):
                #print(''.join(translated[i:i+l]))
                if all(x in list(translated[i:i+l]) for x in k):
                    translated[i:i+l] = v
                    print(encrypted_list)
                    return recurs([''.join(translated)]+encrypted_list, pharaohs_cypher)
                elif (list(pharaohs_cypher.keys())[-1] == k) and (i == len(translated)-1):
                    return encrypted_list
                i += 1
                '''

def recurs1(encrypted_list, k, v, j, q):
    while q < len(k):
        l = len(k[q])+1
        translated = list(encrypted_list[j])
        #print(k)
        i = 0
        while i < len(translated):
            #w = ''.join(translated[i:i+l])
            #y = k[q]
            #z = encrypted_list[j]
            print()
            #print(''.join(translated[i:i+l]))
            if all(x in list(translated[i:i+l]) for x in k[q]):
                new = translated[:]
                new[i:i+l] = v[q]
                if ''.join(new) not in encrypted_list:
                    #print(encrypted_list)
                    return recurs1(encrypted_list+[''.join(new)], k, v, j, q)
            elif (q == len(k)-1) and (i == len(translated)-1):
                if j+1 != len(encrypted_list):
                    return recurs1(encrypted_list, k, v, j+1, 0)
            i += 1
        q += 1
    #print(encrypted_list)
    return encrypted_list
    


#def recurs():
    

def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    '''i = 0
    while i < 3:
        for k, v in pharaohs_cypher.items():
            k = list(k)
            encrypted_text = translate(encrypted_text, k, v)
            print(encrypted_text)
        i += 1'''
    k = list(pharaohs_cypher.keys())
    v = list(pharaohs_cypher.values())
    a = recurs1([encrypted_text], k, v, 0, 0)
    res = min(len(ele) for ele in a)
    short_name = [name for name in a if len(name) == res]
    print(short_name)
    return set(short_name)
    
    #a = recurs([encrypted_text], pharaohs_cypher)
    #print(a)




if __name__ == '__main__':
    file = 'tests/normal/example.json'
    with open(file) as json_file:
        data = json.load(json_file)
        encrypted_text  = data['encrypted_text']
        pharaohs_cypher = data['pharaohs_cypher']
        expected        = set(data['expected'])
    pharaohs_revenge(encrypted_text, pharaohs_cypher)
    #translate(encrypted_text, 'sorta', 'tur')
    #print(encrypted_text, pharaohs_cypher)
    #for k, v in pharaohs_cypher.items():
    #    print(k, v)
        
        