package gestione;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Ex2_Main {
    public static void main(String[] args) {
        // Creazione di alcune carte Pokemon
        Ex2_CartaPokemon carta1 = new Ex2_CartaPokemon("Pikachu", Ex2_CartaPokemon.TipologiaPokemon.ELETTRO, Ex2_CartaPokemon.TipologiaCarta.V, 60);
        Ex2_CartaPokemon carta2 = new Ex2_CartaPokemon("Charizard", Ex2_CartaPokemon.TipologiaPokemon.FUOCO, Ex2_CartaPokemon.TipologiaCarta.V_MAX, 150);
        Ex2_CartaPokemon carta3 = new Ex2_CartaPokemon("Bulbasaur", Ex2_CartaPokemon.TipologiaPokemon.ERBA, Ex2_CartaPokemon.TipologiaCarta.NORMALE, 40);
        Ex2_CartaPokemon carta4 = new Ex2_CartaPokemon("Squirtle", Ex2_CartaPokemon.TipologiaPokemon.ACQUA, Ex2_CartaPokemon.TipologiaCarta.SHINING, 50);

        // Decorazione delle carte con il pattern Decorator
        Ex2_DecoratorCartaPokemonRara raraCarta1 = new Ex2_DecoratorCartaPokemonRara(carta1);
        Ex2_DecoratorCartaPokemonRara raraCarta2 = new Ex2_DecoratorCartaPokemonRara(carta2);

        // Creazione di alcune bustine di carte
        ArrayList<Ex2_AbstractCartaPokemon> carteBustina1 = new ArrayList<>();
        carteBustina1.add(carta1);
        carteBustina1.add(carta3);

        ArrayList<Ex2_AbstractCartaPokemon> carteBustina2 = new ArrayList<>();
        carteBustina2.add(carta2);
        carteBustina2.add(raraCarta1); // Pikachu raro

        ArrayList<Ex2_AbstractCartaPokemon> carteBustina3 = new ArrayList<>();
        carteBustina3.add(raraCarta2); // Charizard raro
        carteBustina3.add(carta4);

        Ex2_Bustina bustina1 = new Ex2_Bustina("Bustina 1", carteBustina1, 4.99, 2021);
        Ex2_Bustina bustina2 = new Ex2_Bustina("Bustina 2", carteBustina2, 5.99, 2021);
        Ex2_Bustina bustina3 = new Ex2_Bustina("Bustina 3", carteBustina3, 6.99, 2022);

        // Aggiunta delle bustine alla collezione
        Ex2_Buste collezioneBuste = Ex2_Buste.getInstance();
        collezioneBuste.addBustina(bustina1);
        collezioneBuste.addBustina(bustina2);
        collezioneBuste.addBustina(bustina3);

        // Test del metodo getMappaAnnoDiCommercializzazioneNomi
        Map<Integer, Set<String>> mappaAnnoNomi = collezioneBuste.getMappaAnnoDiCommercializzazioneNomi();
        System.out.println("Mappa Anno di Commercializzazione - Nomi:");
        for (Map.Entry<Integer, Set<String>> entry : mappaAnnoNomi.entrySet()) {
            System.out.println("Anno: " + entry.getKey() + " - Nomi: " + entry.getValue());
        }

        // Test del metodo getHashMappaNomePokemonRare
        HashMap<String, List<Ex2_DecoratorCartaPokemonRara>> mappaNomeRare = collezioneBuste.getHashMappaNomePokemonRare();
        System.out.println("\nMappa Nome Pokemon - Carte Rare:");
        for (Map.Entry<String, List<Ex2_DecoratorCartaPokemonRara>> entry : mappaNomeRare.entrySet()) {
            System.out.println("Nome: " + entry.getKey() + " - Carte Rare:");
            for (Ex2_DecoratorCartaPokemonRara rara : entry.getValue()) {
                rara.stampa();
            }
        }
    }
}
