package e25_01_24.gestione;

public class Publisher {
    private String nome;
    private int anno;
    private String indirizzo;

    public Publisher(String nome, int anno, String indirizzo) {
        this.nome = nome;
        this.anno = anno;
        this.indirizzo = indirizzo;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Publisher p = (Publisher)o;
        return nome.equals(p.nome) && anno == p.anno && indirizzo.equals(p.indirizzo);
    }
}
