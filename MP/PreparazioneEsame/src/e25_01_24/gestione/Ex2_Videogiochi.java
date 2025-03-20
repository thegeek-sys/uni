package e25_01_24.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ex2_Videogiochi implements Iterable<Videogioco> {
    private Ex2_Videogiochi instance;
    private ArrayList<Videogioco> videogiochi;

    private Ex2_Videogiochi() {
        videogiochi = new ArrayList<>();
    }

    public Ex2_Videogiochi getInstance() {
        if (instance == null) instance = new Ex2_Videogiochi();
        return instance;
    }

    @Override
    public Iterator<Videogioco> iterator() {
        return videogiochi.iterator();
    }

    public void addVideogioco(Videogioco videogioco) {
        videogiochi.add(videogioco);
    }

    public void removeVideogioco(Videogioco videogioco) {
        videogiochi.remove(videogioco);
    }

    public Map<Piattaforma, Set<Videogioco>> getMappaPiattaformaVideogiochi() {
        return videogiochi.stream().collect(Collectors.groupingBy(Videogioco::getPiattaforma, Collectors.toSet()));
    }

    public Map<Integer, List<Videogioco>> getAnnoVideogiochiDiUnaPiattaforma(Piattaforma piattaforma) {
        return videogiochi.stream()
                .filter(s -> s.getPiattaforma().equals(piattaforma))
                .collect(Collectors.groupingBy(Videogioco::getAnno));
    }

    public Set<Integer> getConversioniEPortings(String videogioco) {
        return videogiochi.stream()
                .filter(v -> v.getTitolo().equals(videogioco))
                .map(Videogioco::getPiattaforma)
                .map(Piattaforma::getArchitettura)
                .collect(Collectors.toSet());
    }

}
