package e13_06_23_1.gestione;

public class VolumeSpeciale extends Volume {
    private Allegato allegato;

    public Allegato getAllegato() {
        return allegato;
    }

    public VolumeSpeciale(String titolo, int annoPubblicazione, int mesePubblicazione, int giornoPubblicazione, int numeroSerie) {
        super(titolo, annoPubblicazione, mesePubblicazione, giornoPubblicazione, numeroSerie);
    }
}
