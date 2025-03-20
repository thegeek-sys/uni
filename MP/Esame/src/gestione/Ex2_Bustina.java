package gestione;

import java.util.ArrayList;

public class Ex2_Bustina {
    private final String nome;
    private final ArrayList<Ex2_AbstractCartaPokemon> carte;
    private double prezzo;
    private final int anno;

    public Ex2_Bustina(String nome, ArrayList<Ex2_AbstractCartaPokemon> carte, double prezzo, int anno) {
        this.nome = nome;
        this.carte = carte;
        this.prezzo = prezzo;
        this.anno = anno;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public int getAnno() {
        return anno;
    }

    public String getNome() {
        return nome;
    }

    public ArrayList<Ex2_AbstractCartaPokemon> getCarte() {
        return carte;
    }
}
