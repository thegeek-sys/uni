package e19_06_24.gestione;

import java.util.ArrayList;

public class Ricetta {
    private String nome;
    private Difficolta difficolta;
    private Tipologia tipologia;
    private String descrizione;

    public ArrayList<Ingrediente> getIngredienti() {
        return ingredienti;
    }

    private ArrayList<Ingrediente> ingredienti;

    public enum Difficolta {
        FACILE, MEDIO, DIFFICILE;
    }

    public enum Tipologia {
        VEGNANA, NON_VEGANA;
    }

    public void addIngrediente(Ingrediente ingrediente) {
        ingredienti.add(ingrediente);
    }

    public void removeIngrediente(Ingrediente ingrediente) {
        ingredienti.remove(ingrediente);
    }

    public Tipologia getTipologia() {
        return tipologia;
    }

    private Ricetta(String nome, Difficolta difficolta, Tipologia tipologia, String descrizione, ArrayList<Ingrediente> ingredienti) {
        this.nome = nome;
        this.difficolta = difficolta;
        this.tipologia = tipologia;
        this.descrizione = descrizione;
        this.ingredienti = ingredienti;
    }

    public static class Builder {
        private String nome;
        private Difficolta difficolta;
        private Tipologia tipologia;
        private String descrizione;
        private ArrayList<Ingrediente> ingredienti;

        public Ricetta build() {
            return new Ricetta(nome, difficolta, tipologia, descrizione, ingredienti);
        }

        public Builder setNome(String nome) {
            this.nome = nome;
            return this;
        }

        public Builder setDifficolta(Difficolta difficolta) {
            this.difficolta = difficolta;
            return this;
        }

        public Builder setTipologia(Tipologia tipologia) {
            this.tipologia = tipologia;
            return this;
        }

        public Builder setDescrizione(String descrizione) {
            this.descrizione = descrizione;
            return this;
        }

        public Builder setIngredienti(ArrayList<Ingrediente> ingredienti) {
            this.ingredienti = ingredienti;
            return this;
        }
    }
}


