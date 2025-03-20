package e13_07_23.gestione;

public class Insegnamento {
    private String nomeDocente;
    private String cognomeDocente;
    private int annoCorso;
    private int semestre;

    public Insegnamento(String nomeDocente, String cognomeDocente, int annoCorso, int semestre) {
        this.nomeDocente = nomeDocente;
        this.cognomeDocente = cognomeDocente;
        this.annoCorso = annoCorso;
        this.semestre = semestre;
    }
}
