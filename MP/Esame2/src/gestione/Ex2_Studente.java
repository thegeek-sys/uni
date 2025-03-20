package gestione;

import java.util.HashMap;
import java.util.Objects;

public class Ex2_Studente {
    private String nome;
    private String cognome;
    private int matricola;
    private int annoImmatricolazione;
    private String nomeCorso;
    private HashMap<Ex2_Insegnamento, Integer> mappaInsegnamentoVoti;

    public Ex2_Studente(String nome, String cognome, int matricola, int annoImmatricolazione, String nomeCorso) {
        this.nome = nome;
        this.cognome = cognome;
        this.matricola = matricola;
        this.annoImmatricolazione = annoImmatricolazione;
        this.nomeCorso = nomeCorso;
    }

    public void addVoto(Ex2_Insegnamento insegnamento, int voto) {
        mappaInsegnamentoVoti.put(insegnamento, voto);
    }

    public String getNome() {
        return nome;
    }

    public String getCognome() {
        return cognome;
    }

    public int getMatricola() {
        return matricola;
    }

    public int getAnnoImmatricolazione() {
        return annoImmatricolazione;
    }

    public String getNomeCorso() {
        return nomeCorso;
    }

    public HashMap<Ex2_Insegnamento, Integer> getMappaInsegnamentoVoti() {
        return mappaInsegnamentoVoti;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || this.getClass() != o.getClass()) return false;
        Ex2_Studente s = (Ex2_Studente) o;
        return matricola == s.matricola && annoImmatricolazione == s.annoImmatricolazione && nome.equals(s.nome) && cognome.equals(s.cognome) && nomeCorso.equals(s.nomeCorso) && mappaInsegnamentoVoti.equals(s.mappaInsegnamentoVoti);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nome, cognome, matricola, annoImmatricolazione, nomeCorso, mappaInsegnamentoVoti);
    }
}
