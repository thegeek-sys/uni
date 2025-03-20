package gestione;

public class Ex2_InsegnamentoSpeciale extends Ex2_Insegnamento {
    private String descrizioneAttivita;

    public Ex2_InsegnamentoSpeciale(String nomeDocente, String cognomeDocente, int annoCorso, int semestreCorso, String descrizioneAttivita) {
        super(nomeDocente, cognomeDocente, annoCorso, semestreCorso);
        this.descrizioneAttivita = descrizioneAttivita;
    }

    public String getDescrizioneAttivita() {
        return descrizioneAttivita;
    }
}
