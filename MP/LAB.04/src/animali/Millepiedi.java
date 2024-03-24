package animali;

public class Millepiedi extends Animale {
    public final static String VERSO_MILLEPIEDI = null;
    public final static int NUM_ZAMPE = 1000;
    public final static Taglia TAGLIA_MILLEPIEDI = Taglia.PICCOLA;

    public Millepiedi() {
        super(NUM_ZAMPE, VERSO_MILLEPIEDI, TAGLIA_MILLEPIEDI);
    }
}
