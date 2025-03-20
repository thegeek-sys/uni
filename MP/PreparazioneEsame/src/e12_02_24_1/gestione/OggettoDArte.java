package e12_02_24_1.gestione;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class OggettoDArte {
    private String nome;
    private Artista artista;
    private int anno;
    private ArrayList<Genere> generi;
    private String luogo;
    private Tipologia tipologia;
    private boolean inRestauro;

    private OggettoDArte(OggettoDArteBuilder builder) {
        builder.nome = nome;
        builder.artista = artista;
        builder.anno = anno;
        builder.generi = generi;
        builder.luogo = luogo;
        builder.tipologia = tipologia;
        builder.inRestauro = inRestauro;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Artista getArtista() {
        return artista;
    }

    public void setArtista(Artista artista) {
        this.artista = artista;
    }

    public int getAnno() {
        return anno;
    }

    public void setAnno(int anno) {
        this.anno = anno;
    }

    public ArrayList<Genere> getGeneri() {
        return generi;
    }

    public void setGeneri(ArrayList<Genere> generi) {
        this.generi = generi;
    }

    public String getLuogo() {
        return luogo;
    }

    public void setLuogo(String luogo) {
        this.luogo = luogo;
    }

    public Tipologia getTipologia() {
        return tipologia;
    }

    public void setTipologia(Tipologia tipologia) {
        this.tipologia = tipologia;
    }

    public boolean isInRestauro() {
        return inRestauro;
    }

    public void setInRestauro(boolean inRestauro) {
        this.inRestauro = inRestauro;
    }

    public static class OggettoDArteBuilder {
        private String nome;
        private Artista artista;
        private int anno;
        private ArrayList<Genere> generi;
        private String luogo;
        private Tipologia tipologia;
        private boolean inRestauro;

        public OggettoDArteBuilder(String nome, Artista artista, int anno, ArrayList<Genere> generi, String luogo, Tipologia tipologia) {
            this.nome = nome;
            this.artista = artista;
            this.anno = anno;
            this.generi = generi;
            this.luogo = luogo;
            this.tipologia = tipologia;
        }

        public OggettoDArteBuilder setInRestauro(boolean inRestauro) {
            this.inRestauro = inRestauro;
            return this;
        }

        public OggettoDArte build() {
            return new OggettoDArte(this);
        }
    }
}
