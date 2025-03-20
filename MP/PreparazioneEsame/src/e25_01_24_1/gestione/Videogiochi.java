package e25_01_24_1.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Videogiochi implements Iterable<Videogioco> {
    private static Videogiochi instance;
    private ArrayList<Videogioco> collezioneVideogiochi;

    private Videogiochi() {
        collezioneVideogiochi = new ArrayList<>();
    }

    public static Videogiochi getInstance() {
        if (instance == null) instance = new Videogiochi();
        return instance;
    }

    @Override
    public Iterator<Videogioco> iterator() {
        return collezioneVideogiochi.iterator();
    }

    public void addVideogioco(Videogioco videogioco) {
        collezioneVideogiochi.add(videogioco);
    }

    public Videogioco removeVideogioco(int index) {
        return collezioneVideogiochi.remove(index);
    }

    public Map<Piattaforma, Set<Videogioco>> getMappaPiattaformaVideogiochi() {
        return collezioneVideogiochi.stream()
                .collect(Collectors.groupingBy(
                        Videogioco::getPiattaforma,
                        Collectors.toSet()
                ));
    }

    public Map<Integer, List<Videogioco>> getAnnoVideogiochiDiUnaPiattaforma(Piattaforma piattaforma) {
        return collezioneVideogiochi.stream()
                .filter(x -> piattaforma.equals(x.getPiattaforma()))
                .collect(Collectors.groupingBy(Videogioco::getAnno));
    }

    public Set<Integer> getConversioniEPortings(String titolo) {
        return collezioneVideogiochi.stream()
                .filter(x -> x.getTitolo().equals(titolo))
                .map(x -> x.getPiattaforma().getBit())
                .collect(Collectors.toSet());
    }
}
