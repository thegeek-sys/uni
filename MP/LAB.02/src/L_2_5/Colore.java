package L_2_5;

public class Colore {
    public final static String NERO = "0-0-0";
    public final static String BIANCO = "255-255-255";
    private String c;

    public Colore() {
        c = NERO;
    }

    public Colore(int r, int g, int b) {
        c = r+"-"+g+"-"+b;
    }

    public String display() {
        return c;
    }


}
