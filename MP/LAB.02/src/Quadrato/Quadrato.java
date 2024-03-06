package Quadrato;

public class Quadrato {
    private final double lato;

    public Quadrato(double lato) {
        this.lato = lato;
    }
    public double getPerimetro() { return lato*4; }

    public static void main(String[] args) {
        Quadrato q = new Quadrato(4);
        System.out.println("Perimetro: "+q.getPerimetro());
    }
}
