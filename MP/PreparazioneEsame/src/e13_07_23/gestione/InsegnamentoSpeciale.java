package e13_07_23.gestione;

public class InsegnamentoSpeciale extends Insegnamento {
    private String attivita;
    private String descrizione;

    public InsegnamentoSpeciale(String nomeDocente, String cognomeDocente, int annoCorso, int semestre, String attivita, String descrizione) {
        super(nomeDocente, cognomeDocente, annoCorso, semestre);
        this.attivita = attivita;
        this.descrizione = descrizione;
    }
}
