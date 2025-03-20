package e08_09_23.memoria;

public abstract class Animale {
    public static int esseri_viventi;
    protected int z;
    private String s;
    public Animale(int k) {
        z=(esseri_viventi++)+k;
    }
    @Override
    public String toString() {
        return "Animale:"+z;
    }
}
