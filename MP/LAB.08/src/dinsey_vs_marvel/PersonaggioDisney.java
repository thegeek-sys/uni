package dinsey_vs_marvel;

public abstract class PersonaggioDisney extends Personaggio {
    public PersonaggioDisney(String nome) {
        super(nome);
    }

    public abstract void saluta();
}
