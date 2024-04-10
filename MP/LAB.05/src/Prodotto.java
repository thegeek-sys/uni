public abstract class Prodotto {
    protected double prezzo;
    protected int id;

    public Prodotto(double prezzo, int id) {
        this.prezzo = prezzo;
        this.id = id;
    }

    public double getPrezzo() { return prezzo; }
    public int getID() { return id; }

    @Override
    public String toString() {
        return this.getClass().getSimpleName()+id;
    }
}
