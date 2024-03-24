package animali;

public abstract class Uccello extends Animale {
    public final static int NUM_ZAMPE = 2;

    public Uccello(String verso, Taglia taglia) {
        super(NUM_ZAMPE, verso, taglia);
    }

    public void becca() {

    }
}
