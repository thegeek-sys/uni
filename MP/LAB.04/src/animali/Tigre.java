package animali;

public class Tigre extends Felino {
    public final static String VERSO_TIGRE = "roar";
    public final static Taglia TAGLIA_TIGRE = Taglia.GRANDE;

    public Tigre() {
        super(VERSO_TIGRE, TAGLIA_TIGRE);
    }
}
