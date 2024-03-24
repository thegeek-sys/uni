package animali;

public class Corvo extends Uccello {
    public final static String VERSO_CORVO = "cra cra";
    public final static Taglia TAGLIA_CORVO = Taglia.MEDIA;

    public Corvo() {
        super(VERSO_CORVO, TAGLIA_CORVO);
    }
}
