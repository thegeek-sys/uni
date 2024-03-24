package animali;

public class Passero extends Uccello {
    public final static String VERSO_PASSERO = "chip chip";
    public final static Taglia TAGLIA_PASSERO = Taglia.PICCOLA;

    public Passero() {
        super(VERSO_PASSERO, TAGLIA_PASSERO);
    }
}
