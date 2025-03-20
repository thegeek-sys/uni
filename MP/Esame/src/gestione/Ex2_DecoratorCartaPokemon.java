package gestione;

public abstract class Ex2_DecoratorCartaPokemon extends Ex2_AbstractCartaPokemon {
    protected Ex2_AbstractCartaPokemon carta;

    public Ex2_DecoratorCartaPokemon(Ex2_AbstractCartaPokemon carta) {
        this.carta = carta;
    }
}
