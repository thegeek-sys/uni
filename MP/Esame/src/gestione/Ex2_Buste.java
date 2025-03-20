package gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ex2_Buste {
    private static Ex2_Buste instance;
    private ArrayList<Ex2_Bustina> buste;

    private Ex2_Buste() {
        buste = new ArrayList<>();
    }

    public static Ex2_Buste getInstance() {
        if (instance == null) instance = new Ex2_Buste();
        return instance;
    }

    public void addBustina(Ex2_Bustina bustina) {
        buste.add(bustina);
    }

    public void removeBustina(Ex2_Bustina bustina) {
        buste.remove(bustina);
    }

    public Iterator<Ex2_Bustina> ex2BustinaIterator() {
        return buste.iterator();
    }

    public Map<Integer, Set<String>> getMappaAnnoDiCommercializzazioneNomi() {
        return buste.stream().collect(Collectors.toMap(
                Ex2_Bustina::getAnno,
                r -> {
                    HashSet<String> a = new HashSet<>();
                    a.add(r.getNome());
                    return a;
                },
                (a,b) -> {
                    a.addAll(b);
                    return a;
                }
        ));
    }

    public HashMap<String, List<Ex2_DecoratorCartaPokemonRara>> getHashMappaNomePokemonRare() {
        return (HashMap<String, List<Ex2_DecoratorCartaPokemonRara>>) buste.stream()
                .map(Ex2_Bustina::getCarte)
                .flatMap(ArrayList::stream)
                .filter(r -> r instanceof Ex2_DecoratorCartaPokemonRara)
                .map(r -> (Ex2_DecoratorCartaPokemonRara)r)
                .filter(r -> r.carta instanceof Ex2_CartaPokemon)
                .collect(Collectors.groupingBy(
                        r -> ((Ex2_CartaPokemon)r.carta).getNome(),
                        Collectors.toList()
                ));
    }


}
