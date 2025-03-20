package e13_07_23.memoria;

public class Gatto extends Animale {
    private int numero;

    public Gatto(int numero) {
        super(numero);
        this.numero=++numero;
    }

    @Override
    public String toString() {
        return super.toString()+"_"+numero;
    }
}
