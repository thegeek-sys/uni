package e25_01_24.memoria;


public class Persona extends EssereVivente {
    private int numero;

    public Persona(int numero) {
        super(numero);
        this.numero = ++numero;
    }

    public String toString() {
        return super.toString()+"_"+numero;
    }
}
