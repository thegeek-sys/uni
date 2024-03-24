package animali;

public abstract class Animale {
    protected String verso;
    protected int numZampe;
    protected Taglia taglia;

    public Animale(int numZampe, String verso, Taglia taglia) {
        //super(); // chiama implicitamente il supercostruttore Object
        this.verso = verso;
        this.numZampe = numZampe;
        this.taglia = taglia;
    }

    public String emettiVerso() { return verso; }
    public int getNumeroDiZampe() { return numZampe; }
    public Taglia getTaglia() { return taglia; }

}
