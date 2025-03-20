package gestione;

public class Ex2_DecoratorCartaPokemonRara extends Ex2_DecoratorCartaPokemon {

    public Ex2_DecoratorCartaPokemonRara(Ex2_AbstractCartaPokemon carta) {
        super(carta);
    }

    @Override
    public void stampa() {
        carta.stampa();
        System.out.println("**** RARA ****");
    }


}
