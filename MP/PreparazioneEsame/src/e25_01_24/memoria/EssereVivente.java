package e25_01_24.memoria;

public class EssereVivente {
    public static int numeroEsseriViventi=10;
    private int numero;

    public EssereVivente(int numero) {
        numeroEsseriViventi=numero;
        numeroEsseriViventi++;
        this.numero = numero;
    }

    public String toString() {
        return numeroEsseriViventi+"_"+numero;
    }
}
