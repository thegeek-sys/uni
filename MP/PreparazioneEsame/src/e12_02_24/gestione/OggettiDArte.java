package e12_02_24.gestione;

import e19_06_24.gestione.Ingrediente;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class OggettiDArte {
    private static OggettiDArte instance;
    private ArrayList<OggettoDArte> opere;

    private OggettiDArte() {
        opere = new ArrayList<>();
    }

    public static OggettiDArte getInstance() {
        if (instance == null) instance = new OggettiDArte();
        return instance;
    }

    public Map<OggettoDArte.Genere, Set<OggettoDArte>> getMappaGenereOggettiDiArte() {
        return opere.stream()
                .collect(Collectors.groupingBy(
                r -> r.getGenere().getFirst(),
                Collectors.toSet()
        ));
    }

    public Map<Artista, List<OggettoDArte>> getMappaArtistaOggettiDiArteNelPeriodo(int annoInizio, int annoFine) {
        return opere.stream()
                .filter(x -> x.getAnno() <= annoFine && x.getAnno() >= annoInizio)
                .collect(Collectors.groupingBy(
                        OggettoDArte::getArtista,
                        Collectors.toList()
                ));
    }
}
