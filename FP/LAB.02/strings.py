################################################################################
# Stringhe
################################################################################

# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale.
# Ad esempio, `s = "85721"`. Stampate la somma delle cifre contenute nella stringa.
def dec_str_to_dec(s):
    #s = int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4])
    f = 0
    for x in s:
        f += int(x)
    print(f, end='\n')

print("Result of dec_str_to_dec: ", end="")
dec_str_to_dec("85721")

# Scrivete una espressione che a partire da una stringa di 5 caratteri,
# rappresentante un numero binario, stampi la sua rappresentazione decimale.
# Ad esempio, `s = "00101" -> 5`.
def bin_str_to_dec(s):
    s = int(s[-1])*2**0+int(s[-2])*2**1+int(s[-3])*2**2+int(s[-4])*2**3+int(s[0])*2**4
    print(s, end='\n')

print("Result of bin_str_to_dec: ", end="")
bin_str_to_dec("00101")

# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale
# ('.'). Ad esempio, s = "52.29". Stampare il numero decimale rappresentato
# dalla stringa(stamparlo come numero, non come stringa).
def dec_frac_str_to_dec(s):
    s = int(s[0:s.index('.')])+int(s[s.index('.')+1:5])*10**-2
    print(s)

print("Result of dec_frac_str_to_dec: ", end="")
dec_frac_str_to_dec("52.29")