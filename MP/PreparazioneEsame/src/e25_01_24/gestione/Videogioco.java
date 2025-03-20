package e25_01_24.gestione;

import java.util.ArrayList;

public class Videogioco {
    private String titolo;
    private Publisher publisher;
    private int anno;
    private ArrayList<Generi> genere;
    private int giocatori;
    private Piattaforma piattaforma;

    public Videogioco(String titolo, Publisher publisher, int anno, ArrayList<Generi> genere, int giocatori, Piattaforma piattaforma) {
        this.titolo = titolo;
        this.publisher = publisher;
        this.anno = anno;
        this.genere = genere;
        this.giocatori = giocatori;
        this.piattaforma = piattaforma;
    }

    public String getTitolo() {
        return titolo;
    }

    public void setTitolo(String titolo) {
        this.titolo = titolo;
    }

    public Publisher getPublisher() {
        return publisher;
    }

    public void setPublisher(Publisher publisher) {
        this.publisher = publisher;
    }

    public int getAnno() {
        return anno;
    }

    public void setAnno(int anno) {
        this.anno = anno;
    }

    public ArrayList<Generi> getGenere() {
        return genere;
    }

    public void setGenere(ArrayList<Generi> genere) {
        this.genere = genere;
    }

    public int getGiocatori() {
        return giocatori;
    }

    public void setGiocatori(int giocatori) {
        this.giocatori = giocatori;
    }

    public Piattaforma getPiattaforma() {
        return piattaforma;
    }

    public void setPiattaforma(Piattaforma piattaforma) {
        this.piattaforma = piattaforma;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Videogioco v = (Videogioco)o;
        return titolo.equals(v.titolo) && anno == v.anno && publisher.equals(v.publisher) && genere.equals(v.genere) && giocatori == v.giocatori && piattaforma.equals(v.piattaforma);
    }
}
