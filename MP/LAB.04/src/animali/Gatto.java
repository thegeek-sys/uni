package animali;

public class Gatto extends Felino{
    public static final String VERSO_GATTO = "miao miao";
    public static final Taglia TAGLIA_GATTO = Taglia.PICCOLA;
    public Gatto() {
        super(VERSO_GATTO, TAGLIA_GATTO);
    }
}
