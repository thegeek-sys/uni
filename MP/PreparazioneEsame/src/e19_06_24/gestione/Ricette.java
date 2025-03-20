package e19_06_24.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ricette {
    private static Ricette instance;
    private ArrayList<Ricetta> ricette;

    private Ricette() {
        ricette = new ArrayList<>();
    }

    public static Ricette getInstance() {
        if (instance == null) instance = new Ricette();
        return instance;
    }

    public Iterator<Ricetta> ricettaIterator() {
        return ricette.iterator();
    }

    public HashMap<Ricetta.Tipologia, Set<Ricetta>> getMappaTipologiaRicette() {
        return (HashMap<Ricetta.Tipologia, Set<Ricetta>>) ricette.stream().collect(Collectors.groupingBy(
                Ricetta::getTipologia,
                Collectors.toSet()
        ));
    }

    public Map<Ingrediente, ArrayList<Double>> getHashMappaIngredientiQuantitaPerTipologiaRicette(Ricetta.Tipologia tipologia) {
        return ricette.stream()
                .filter(r -> r.getTipologia() == tipologia)
                .map(Ricetta::getIngredienti)
                .flatMap(ArrayList::stream)
                .collect(Collectors.toMap(
                        s -> s,
                        r -> {
                            ArrayList<Double> a = new ArrayList<>();
                            a.add(r.getGrammi());
                            return a;
                        },
                        (a,b) -> {
                            a.addAll(b);
                            return a;
                        }
                ));
    }
}
