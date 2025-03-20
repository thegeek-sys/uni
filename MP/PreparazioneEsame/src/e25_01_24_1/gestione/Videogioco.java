package e25_01_24_1.gestione;

import java.util.ArrayList;
import java.util.Objects;

public class Videogioco {
    private String titolo;
    private Publisher publisher;
    private int anno;
    private ArrayList<Genere> generi;
    private int numeroGiocatori;
    private Piattaforma piattaforma;

    public Videogioco(String titolo, Publisher publisher, int anno, ArrayList<Genere> generi, int numeroGiocatori, Piattaforma piattaforma) {
        this.titolo = titolo;
        this.publisher = publisher;
        this.anno = anno;
        this.generi = generi;
        this.numeroGiocatori = numeroGiocatori;
        this.piattaforma = piattaforma;
    }

    public Publisher getPublisher() {
        return publisher;
    }

    public int getAnno() {
        return anno;
    }

    public ArrayList<Genere> getGeneri() {
        return generi;
    }

    public int getNumeroGiocatori() {
        return numeroGiocatori;
    }

    public Piattaforma getPiattaforma() {
        return piattaforma;
    }

    public String getTitolo() {
        return titolo;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Videogioco that)) return false;
        return anno == that.anno && numeroGiocatori == that.numeroGiocatori && Objects.equals(titolo, that.titolo) && Objects.equals(publisher, that.publisher) && Objects.equals(generi, that.generi) && Objects.equals(piattaforma, that.piattaforma);
    }

    @Override
    public int hashCode() {
        return Objects.hash(titolo, publisher, anno, generi, numeroGiocatori, piattaforma);
    }
}
