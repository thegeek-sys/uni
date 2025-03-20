package e13_06_23.gestione;

public class Volume {
    private String titolo;
    private int annoPubblicazione;
    private int mesePubblicazione;
    private int giornoPubblicazione;
    private long numeroSerie;
    private static long id = 0;

    public Volume(String titolo, int annoPubblicazione, int mesePubblicazione, int giornoPubblicazione, long numeroSerie) {
        this.titolo = titolo;
        this.annoPubblicazione = annoPubblicazione;
        this.mesePubblicazione = mesePubblicazione;
        this.giornoPubblicazione = giornoPubblicazione;
        numeroSerie = id++;
    }

    public int getAnnoPubblicazione() {
        return annoPubblicazione;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || this.getClass() != o.getClass()) return false;
        Volume v = (Volume)o;
        return this.titolo.equals(v.titolo) && this.annoPubblicazione == v.annoPubblicazione && this.giornoPubblicazione == v.giornoPubblicazione && this.numeroSerie == v.numeroSerie;
    }

    @Override
    public int hashCode() {
        int result = titolo.hashCode();
        return 31 * result;
    }
}
