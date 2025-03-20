package e13_06_23.gestione;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Map;
import java.util.stream.Collectors;

public class CollezioneCollane {
    private static CollezioneCollane instance;
    private ArrayList<CollanaFumetti> collaneFumetti;

    private CollezioneCollane() {
        collaneFumetti = new ArrayList<>();
    }

    public static CollezioneCollane getInstance() {
        if (instance == null) instance = new CollezioneCollane();
        return instance;
    }

    public Map<Volume, Allegato> getMappaVolumiAllegati() {
        return collaneFumetti.stream()
                .map(CollanaFumetti::getVolumi)
                .flatMap(ArrayList::stream)
                .filter(v -> v instanceof VolumeSpeciale)
                .collect(Collectors.toMap(
                        v -> v,
                        v -> ((VolumeSpeciale)v).getAllegato()
                ));
    }

    public Map<Integer, HashSet<Volume>> getMappaAnniVolumi() {
        return collaneFumetti.stream()
                .map(CollanaFumetti::getVolumi)
                .flatMap(ArrayList::stream)
                .collect(Collectors.toMap(
                        Volume::getAnnoPubblicazione,
                        v -> {
                            HashSet<Volume> volumi = new HashSet<>();
                            volumi.add(v);
                            return volumi;
                        },
                        (set1, set2) -> {
                            set1.addAll(set2);
                            return set1;
                        }

                ));
    }
}
