package e08_09_23.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ferrovie {
    private Ferrovie instance;
    private ArrayList<Corsa> corseTreni;

    private Ferrovie() {
        corseTreni = new ArrayList<>();
    }

    public Ferrovie getInstance() {
        if (instance == null) instance = new Ferrovie();
        return instance;
    }

    public Iterator<Corsa> corsaIterator() {
        return corseTreni.iterator();
    }

    public void addCorsa(Corsa corsa) { corseTreni.add(corsa); }
    public void removeCorsa(Corsa corsa) { corseTreni.remove(corsa); }
    public ArrayList<Corsa> getCorseTreni() { return corseTreni; }

    public Map<Stazione, Set<Corsa>> getMappaStazioniCorse() {
        return corseTreni.stream()
                .collect(Collectors.groupingBy(
                        s -> s.getStazioni().getFirst(),
                        Collectors.toSet()
                ));
    }

    public long getMediaTempoDiPercorrenza(Stazione stazione1, Stazione stazione2) {
        return (long) corseTreni.stream()
                .filter(s -> s.getStazioni().getFirst().equals(stazione1) && s.getStazioni().getLast().equals(stazione2))
                .mapToLong(s -> s.getOrari().get(stazione2)-s.getOrari().get(stazione1))
                .average().orElse(0);
    }
}
