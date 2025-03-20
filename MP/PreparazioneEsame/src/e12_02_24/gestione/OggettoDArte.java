package e12_02_24.gestione;

import java.util.ArrayList;

public class OggettoDArte {
    private String nome;
    private Artista artista;
    private int anno;
    private ArrayList<Genere> genere;
    private String luogo;
    private Tipologia tipologia;
    private boolean inRestauro;

    public ArrayList<Genere> getGenere() {
        return genere;
    }

    public int getAnno() {
        return anno;
    }

    public Artista getArtista() {
        return artista;
    }

    private OggettoDArte(String nome, Artista artista, int anno, ArrayList<Genere> genere, String luogo, Tipologia tipologia, boolean inRestauro) {
        this.nome = nome;
        this.artista = artista;
        this.anno = anno;
        this.genere = genere;
        this.luogo = luogo;
        this.tipologia = tipologia;
        this.inRestauro = inRestauro;
    }

    public enum Genere {
        SCULTURA, PITTURA, AUDIO, TESTO, FOTOGRAFIA, SPARTITO;
    }

    public static class Builder {
        private String nome;
        private Artista artista;
        private int anno;
        private ArrayList<Genere> genere;
        private String luogo;
        private Tipologia tipologia;
        private boolean inRestauro;

        public Builder(String nome, Artista artista, int anno, ArrayList<Genere> genere, String luogo, Tipologia tipologia) {
            this.nome = nome;
            this.artista = artista;
            this.anno = anno;
            this.genere = genere;
            this.luogo = luogo;
            this.tipologia = tipologia;
        }

        public OggettoDArte build() {
            return new OggettoDArte(nome, artista, anno, genere, luogo, tipologia, inRestauro);
        }

        public Builder setInRestauro(boolean inRestauro) {
            this.inRestauro = inRestauro;
            return this;
        }
    }
}
