package e25_01_24_1.gestione;

public class Publisher {
    private String nome;
    private int annoInizio;
    private String indirizzo;

    public String getNome() {
        return nome;
    }

    public int getAnnoInizio() {
        return annoInizio;
    }

    public String getIndirizzo() {
        return indirizzo;
    }

    public Publisher(String nome, int annoInizio, String indirizzo) {
        this.nome = nome;
        this.annoInizio = annoInizio;
        this.indirizzo = indirizzo;
    }
}
