package Persona;

public class Persona {
    private final String nome, cognome;

    public Persona(String nome, String cognome) {
        this.nome = nome;
        this.cognome = cognome;
    }

    public void stampa() {
        System.out.println("Nome: "+nome+" Cognome: "+cognome);
    }

    public static void main(String[] args) {
        Persona p = new Persona("Flavio", "Sperandeo");
        p.stampa();

        // creo un'istanza di persona ma non ci posso più accedere
        new Persona("Uladislau", "Rybin").stampa();
    }
}
