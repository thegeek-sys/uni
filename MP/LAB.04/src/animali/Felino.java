package animali;

public abstract class Felino extends Mammifero{
    public final static int NUM_ZAMPE = 4;

    public Felino(String verso, Taglia taglia) {
        super(NUM_ZAMPE, verso, taglia);
    }

    public void graffia() {

    }
}
