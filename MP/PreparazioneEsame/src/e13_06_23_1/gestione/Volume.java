package e13_06_23_1.gestione;

import java.util.HashMap;
import java.util.Optional;

public class Volume {
    private String titolo;
    private int annoPubblicazione;
    private int mesePubblicazione;
    private int giornoPubblicazione;
    private int numeroSerie;
    private int numeroIncrementale;
    private static HashMap<Integer, Integer> id;

    public Volume(String titolo, int annoPubblicazione, int mesePubblicazione, int giornoPubblicazione, int numeroSerie) {
        if (id == null) id = new HashMap<>();
        id.put(numeroSerie, id.getOrDefault(numeroSerie, 0)+1);
        numeroIncrementale = id.get(numeroSerie);
        this.titolo = titolo;
        this.annoPubblicazione = annoPubblicazione;
        this.mesePubblicazione = mesePubblicazione;
        this.giornoPubblicazione = giornoPubblicazione;
        this.numeroSerie = numeroSerie;
    }

    public String getTitolo() {
        return titolo;
    }

    public int getAnnoPubblicazione() {
        return annoPubblicazione;
    }

    public int getMesePubblicazione() {
        return mesePubblicazione;
    }

    public int getGiornoPubblicazione() {
        return giornoPubblicazione;
    }

    public int getNumeroSerie() {
        return numeroSerie;
    }

    public int getNumeroIncrementale() {
        return numeroIncrementale;
    }

    public static HashMap<Integer, Integer> getId() {
        return id;
    }
}
