import immagini as images


def draw(n_im, color, x, y, w, h):
    for row in range(y,y+h):
        for col in range(x,x+w):
            n_im[row][col] = color
    return n_im
    

def es4(fimm, fimm1, h1, w1):
    '''    
    Si definisca la  funzione es4(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
    - legge l'immagine da fimm e crea una seconda  immagine. L'immagine da creare 
      ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
      sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h e ampiezza w aventi 
      tutti il colore del pixel originario.
    - salva l'immagine creata all'indirizzo fimm.
    - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
    caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    
    img = images.load(fimm)
    n_im = [ [(0,)*3] * len(img[0])*w1 for _ in range(len(img)*h1) ]
    
    colors = {}
    for row in range(len(img)):
        for col in range(len(img[0])):
            colors[img[row][col]] = colors.get(img[row][col], [])+[(row,col)]
            n_im = draw(n_im, img[row][col], col*w1, row*h1, w1, h1)
    
    images.save(n_im, fimm1)
    M = max(list(colors.values()), key=len)
    c = tuple(k for k in list(colors.keys()) if colors[k] == M)[0]
    mul = {}
    mul[c] = M
    for k, v in colors.items():
        if len(v) == len(M) and v != M:
            mul[k] = v
    

    l = sorted(list(mul.values()))[0][0]
    return [k for k, v in mul.items() if l in v][0]
            
        
    # print(color)
    
    
print(es4('cubo.png','test8_1.png',1,3))



