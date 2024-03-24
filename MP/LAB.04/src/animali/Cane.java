package animali;

public class Cane extends Mammifero {
    public final static int NUM_ZAMPE = 4;
    public final static String VERSO_CANE = "bau bau";

    public Cane(Taglia taglia) {
        super(NUM_ZAMPE, VERSO_CANE, taglia);
    }

    public void puccioso() {

    }

}
