package carta;

public enum Valori {
    UNO(1), DUE(2), TRE(3), QUATTRO(4), CINQUE(5),
    SEI(6), SETTE(7), OTTO(8), NOVE(9), DIECI(10), JACK(11), DONNA(12), RE(13);
    private final int valore;

    Valori(int valore) {
        this.valore = valore;
    }

    public int getValore() { return valore; }
}
