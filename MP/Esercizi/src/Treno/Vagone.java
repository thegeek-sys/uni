package Treno;

public abstract class Vagone {
    private String destinazione;
    protected int postiDisponibili;

    public Vagone(String destinazione, int postiDisponibili) {
        this.destinazione = destinazione;
        this.postiDisponibili = postiDisponibili;
    }

    public abstract void occupa(Passeggero passeggero) throws PostiNonDisponibiliException, PasseggeroNonAmmessoException;

    public int getNumeroPostiLiberi() { return postiDisponibili; }
    public String getDestinazione() { return destinazione; }
}
