package e13_06_23_1.gestione;

import java.util.HashMap;

public class Allegato {
    private String titolo;
    private String descrizioneTestuale;
    private TipoAllegato descrittore;
    private int annoPubblicazione;
    private int mesePubblicazione;
    private int giornoPubblicazione;
    private int numeroSerie;
    private int numeroIncrementale;
    private static HashMap<Integer, Integer> id;

    public Allegato(String titolo, int annoPubblicazione, int mesePubblicazione, int giornoPubblicazione, int numeroSerie, String descrizioneTestuale, TipoAllegato descrittore) {
        if (id == null) id = new HashMap<>();
        id.put(numeroSerie, id.getOrDefault(numeroSerie, 0)+1);
        numeroIncrementale = id.get(numeroSerie);
        this.titolo = titolo;
        this.annoPubblicazione = annoPubblicazione;
        this.mesePubblicazione = mesePubblicazione;
        this.giornoPubblicazione = giornoPubblicazione;
        this.numeroSerie = numeroSerie;
        this.descrizioneTestuale = descrizioneTestuale;
        this.descrittore = descrittore;
    }
}
