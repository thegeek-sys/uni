
################################################################################
# Calcoli
################################################################################

import math

# Scrivete una espressione che calcoli il numero di secondi che ci sono in
# 42 minuti e 42 secondi.
print("42:42 in sec:",42*60+42,"sec")

# Scrivete una espressione che calcoli il numero di miglia che ci sono in
# 10 chilometri. (1 miglio=1.61 km).
print("10 km in miglia:",format(10/1.61, '.2f'),"miglia")

# Scrivete una espressione che calcoli la velocità media e la cadenza media
# (tempo per miglio, in minuti e secondi) di un corridore che corre una gara
# di 10 chilometri in 42 minuti e 42 secondi.
print("Velocità media:",format(10/(42/60+42/60/60), '.2f'),"km/h")
print("Cadenza media:",format(10/1.61/(42+42/60), '.2f'),"mi/m")
print("Cadenza media:",format(10/1.61/(42*60+42), '.5f'),"mi/s")

# Il volume di una sfera di raggio `r` è `4/3 * PI * r ^ 3`.
# Scrivere una espressione che calcoli il volume di una sfera di raggio 5.
print("Volume sfera r=5:",format(4/3*math.pi*5**3, '.2f'))

# Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40%
# di sconto. I costi di spedizione sono 3 euro per la prima copia, e 75
# centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?
print("Costo totale:",format(0.75*59+3+((24.95-(40/100*24.95))*60), '.2f'),'€')

# Se uscite di casa alle 6: 52 di mattina e correte un miglio a ritmo blando
# (8 minuti e 15 secondi al miglio), e poi 3 miglia a ritmo moderato
# (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando
# (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?
min = 6*60+52 + 8+15/60 + 3*(7+12/60) + 9+45/60
fin_h = min//60
fin_m = (min/60-fin_h)*60
print('Arrivo alle ore '+str(int(fin_h))+':'+str(int(fin_m)))