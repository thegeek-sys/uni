package e13_07_23.gestione;

import java.util.HashMap;

public class Studente {
    private int matricola;
    private String nome;
    private String cognome;
    private String corsoDiStudi;
    private HashMap<Insegnamento, Integer> voti;

    public Studente(int matricola, String nome, String cognome, String corsoDiStudi) {
        this.matricola = matricola;
        this.nome = nome;
        this.corsoDiStudi = corsoDiStudi;
        voti = new HashMap<>();
    }

    public void addVoto(Insegnamento insegnamento, Integer voto) {
        voti.put(insegnamento, voto);
    }

    public HashMap<Insegnamento, Integer> getVoti() { return voti; }

    public int getMediaVoti() {
        int media = 0;
        for (Integer voto : voti.values()) {
            media+=voto;
        }
        media /= voti.size();
        return media;
    }
}
