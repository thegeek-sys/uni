package e19_06_24.gestione;

public class Ingrediente {
    private IngredienteType nome;
    private double grammi;

    public Ingrediente(IngredienteType nome, double grammi) {
        this.nome = nome;
        this.grammi = grammi;
    }

    public void setGrammi(double grammi) {
        this.grammi = grammi;
    }

    public double getGrammi() {
        return grammi;
    }

    public enum IngredienteType {
        SALE, PEPE, FARINA, UOVA, POMODORO;
    }
}
