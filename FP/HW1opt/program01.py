# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

'''
def ex1(int_seq, subtotal):
    i, int_seq_list = 0, int_seq.split(',')
    int_seq_list = [int(elem) for elem in int_seq_list]

    for start in range(len(int_seq_list)):
        somma = 0
        for end in range(len(int_seq_list)):
            for x in int_seq_list[start:end]:
                somma += x
            #somma = sum(int_seq_list[start:end])
            if somma == subtotal:
                i += 1
            elif somma > subtotal:
                break
            somma = 0
    


    
    for start in range(len(int_seq_list)):
        end = 0
        somma = 0
        while end < len(int_seq_list) and somma <= subtotal:
            somma = 0
            for x in int_seq_list[start:end]:
                somma += x
            if somma == subtotal:
                i += 1
            end += 1
    
    return i
'''

def ex1(int_seq, subtotal):
    int_seq_list = [int(elem) for elem in int_seq.split(',')]
    n = len(int_seq_list)
    prefix_sum = [0] * (n + 1)
    count = 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + int_seq_list[i] # somma cumulativa

    for start in range(n):
        for end in range(start + 1, n + 1):
            current_sum = prefix_sum[end] - prefix_sum[start] # differenza della somma cumulativa tra end e start
            if current_sum == subtotal:
                count += 1
            elif current_sum > subtotal:
                break

    return count


if __name__ == '__main__':
    int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
    subtotal=9
    #int_seq_list = [int(x) for x in int_seq_list]
    #print(int_seq_list)
    #for start in range(len(int_seq_list)):
    '''
        end = 0
        somma = 0
        while end < len(int_seq_list) and somma <= subtotal:
            somma = 0
            lista = int_seq_list[start:end]
            for x in lista:
                somma += int(x)
            
            if somma == subtotal:
                i += 1
                print(i,')',",".join(int_seq_list[start:end]))
                print(somma)
            end += 1
            
        #print('azzero la somma')
        
            #print(somma, int_seq_list[start:end])
        '''

    '''
        for end in range(len(int_seq_list)):
            for x in int_seq_list[start:end]:
                somma += int(x)
            #print(somma, int_seq_list[start:end])
            if somma == subtotal:
                i += 1
                print(i,')',",".join(int_seq_list[start:end]))
            elif somma > subtotal:
                somma = 0
                #print('azzero la somma')
                break
            somma = 0
        
    '''

    int_seq_list = [int(elem) for elem in int_seq.split(',')]
    n = len(int_seq_list)
    prefix_sum = [0] * (n + 1)
    count = 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + int_seq_list[i]

    for start in range(n):
        for end in range(start + 1, n + 1):
            current_sum = prefix_sum[end] - prefix_sum[start]
            if current_sum == subtotal:
                count += 1
            elif current_sum > subtotal:
                break

    print(count)