package e13_06_23.gestione;

public class Allegato extends Volume {
    private String descrizione;
    private TipoAllegato tipoAllegato;

    public Allegato(String titolo, int annoPubblicazione, int mesePubblicazione, int giornoPubblicazione, long numeroSerie, String descrizione, TipoAllegato tipoAllegato) {
        super(titolo, annoPubblicazione, mesePubblicazione, giornoPubblicazione, numeroSerie);
        this.descrizione = descrizione;
        this.tipoAllegato = tipoAllegato;
    }
}
