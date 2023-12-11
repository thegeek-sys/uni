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

#@profile
def trans_recurs(encrypted_list, k, v, j, q=0):
    while q < len(k):
        l_key = len(k[q])+1
        translated = list(encrypted_list[j])
        l_translated = len(translated)-l_key
        l_translated = (l_translated if l_translated >= 0 else 0)
        i = 0
        while i <= l_translated:
            #w = ''.join(translated[i:i+l_key])
            #y = k[q]
            #z = encrypted_list[j]
            #print()

            if all(translated[i:i+l_key].count(x) >= k[q].count(x) for x in k[q]):
                new = translated[:]
                new[i:i+l_key] = v[q]
                new = ''.join(new)
                if new not in encrypted_list:
                    return trans_recurs(encrypted_list+[new], k, v, j, q)
                
            if (q == k_list) and (i == l_translated) and (j+1 != len(encrypted_list)):
                return trans_recurs(encrypted_list, k, v, j+1)
            i += 1
        q += 1
    return encrypted_list
    

    

def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    global k_list
    k = list(pharaohs_cypher.keys())
    v = list(pharaohs_cypher.values())
    k_list = len(k)-1
    decrytted_list = trans_recurs([encrypted_text], k, v, 0)
    min_len = min(len(el) for el in decrytted_list)
    return {shortest for shortest in decrytted_list if len(shortest) == min_len}




if __name__ == '__main__':
    file = 'tests/normal/test__4_3.json'
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        encrypted_text  = data['encrypted_text']
        pharaohs_cypher = data['pharaohs_cypher']
        expected        = set(data['expected'])
    res = pharaohs_revenge(encrypted_text, pharaohs_cypher)
    assert res == expected
    #encrypted_text=  "aaabaaac"
    #pharaohs_cypher= {"aa":"bc","bb":"c","cc":"d"}
    #expected=        { "d" }
    #res = pharaohs_revenge(encrypted_text, pharaohs_cypher)
    #print(res)

        
        