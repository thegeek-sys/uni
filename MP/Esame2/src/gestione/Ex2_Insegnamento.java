package gestione;

import java.util.Objects;

public class Ex2_Insegnamento {
    private String nomeDocente;
    private String cognomeDocente;
    private int annoCorso;
    private int semestreCorso;

    public Ex2_Insegnamento(String nomeDocente, String cognomeDocente, int annoCorso, int semestreCorso) {
        this.nomeDocente = nomeDocente;
        this.cognomeDocente = cognomeDocente;
        this.annoCorso = annoCorso;
        this.semestreCorso = semestreCorso;
    }

    public String getNomeDocente() {
        return nomeDocente;
    }

    public String getCognomeDocente() {
        return cognomeDocente;
    }

    public int getAnnoCorso() {
        return annoCorso;
    }

    public int getSemestreCorso() {
        return semestreCorso;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || this.getClass() != o.getClass()) return false;
        Ex2_Insegnamento s = (Ex2_Insegnamento) o;
        return nomeDocente.equals(s.nomeDocente) && cognomeDocente.equals(s.cognomeDocente) && annoCorso == s.annoCorso && semestreCorso == s.semestreCorso;
    }

    @Override
    public int hashCode() {
        return Objects.hash(nomeDocente, cognomeDocente, annoCorso, semestreCorso);
    }
}
