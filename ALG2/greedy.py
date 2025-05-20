'''
Sia G = (V, E) un qualsiasi grafo orientato con pesi sugli archi, pesi che possono
essere anche negativi ma in cui non sono presenti cicli di peso negativo.
• Dimostrare che l’algoritmo di Dijkstra su grafi di questo tipo non calcola
necessariamente i cammini di costo minimo tra la sorgente e gli altri nodi
del grafo.
• Per il calcolo dei cammini di costo minimo in G si suggerisce il seguente
algoritmo:
Sia M il costo minimo tra i costi degli archi di G. Modifichiamo i pesi
degli archi di G sommando a ciascuno di questi l’intero |M | abbastanza
grande da renderli tutti positivi. Al grafo che si ottiene G0 (che ha pesi
positivi) applichiamo l’algoritmo di Dijkstra.
I cammini minimi che vengono cos`ı calcolati sono anche cammini minimi
per il grafo originale G? Motivare la risposta.
'''
