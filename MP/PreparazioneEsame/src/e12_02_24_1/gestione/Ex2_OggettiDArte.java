package e12_02_24_1.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ex2_OggettiDArte implements Iterable<OggettoDArte> {
    private Ex2_OggettiDArte instance;
    private ArrayList<OggettoDArte> oggettiDArte;

    private Ex2_OggettiDArte() {
        oggettiDArte = new ArrayList<>();
    }

    public Ex2_OggettiDArte getInstance() {
        if (instance == null) instance = new Ex2_OggettiDArte();
        return instance;
    }

    @Override
    public Iterator<OggettoDArte> iterator() {
        return oggettiDArte.iterator();
    }

    public void addOggettoDArte(OggettoDArte oggettoDArte) {
        oggettiDArte.add(oggettoDArte);
    }

    public void removeOggettoDArte(OggettoDArte oggettoDArte) {
        oggettiDArte.remove(oggettoDArte);
    }

    public Map<Genere, Set<OggettoDArte>> getMappaGeneriOggettiDiArte() {
        return oggettiDArte.stream()
                .flatMap(oggetto -> oggetto.getGeneri().stream()
                        .map(genere -> new AbstractMap.SimpleEntry<>(genere, oggetto)))
                .collect(Collectors.groupingBy(
                        Map.Entry::getKey,
                        Collectors.mapping(Map.Entry::getValue, Collectors.toSet())
                ));
    }

    public Map<Artista, List<OggettoDArte>> getMappaArtistaOggettiDiArteNelPeriodo(int inizio, int fine) {
        return oggettiDArte.stream()
                .filter(s -> inizio <= s.getAnno() && s.getAnno() <= fine)
                .collect(Collectors.groupingBy(
                        OggettoDArte::getArtista
                ));
    }


}
