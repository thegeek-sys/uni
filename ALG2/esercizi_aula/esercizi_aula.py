'''
Progettare un algoritmo che, dato un DAG pesato G rappresentato mediante
liste di adiacenza ed un suo vertice sorgente s, restituisca il vettore delle distanze
dei nodi da s
'''
def BFSdistanze(x, G):
	D = [float('inf')]*len(G)
	D[x] = 0
	coda = [x]
	i = 0
	while  len(coda) > i:
		u = coda[i]
		i += 1
		for y in G[u]:
			if D[y[0]] == -1:
				D[y[0]] = D[u]+1
				coda.append(y[0])
	return D

def es1(G, s):
    

