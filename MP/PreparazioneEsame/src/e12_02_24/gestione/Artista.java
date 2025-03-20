package e12_02_24.gestione;

public class Artista {
    private final String nome;
    private final int annoInizioCarriera;
    private final int annoFineCarriera;

    public int getAnnoFineCarriera() {
        return annoFineCarriera;
    }

    public int getAnnoInizioCarriera() {
        return annoInizioCarriera;
    }

    public Artista(String nome, int annoInizioCarriera, int annoFineCarriera) {
        this.nome = nome;
        this.annoInizioCarriera = annoInizioCarriera;
        this.annoFineCarriera = annoFineCarriera;
    }
}
