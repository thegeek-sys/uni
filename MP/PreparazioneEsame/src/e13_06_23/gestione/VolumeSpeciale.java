package e13_06_23.gestione;

public class VolumeSpeciale extends Volume {
    private Allegato allegato;

    public VolumeSpeciale(String titolo, int annoPubblicazione, int mesePubblicazione, int giornoPubblicazione, long numeroSerie, Allegato allegato) {
        super(titolo, annoPubblicazione, mesePubblicazione, giornoPubblicazione, numeroSerie);
        this.allegato = allegato;
    }

    public Allegato getAllegato() {
        return allegato;
    }
}
