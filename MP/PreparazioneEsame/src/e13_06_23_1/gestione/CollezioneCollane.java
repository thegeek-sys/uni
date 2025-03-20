package e13_06_23_1.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class CollezioneCollane implements Iterable<CollanaFumetti> {
    private static CollezioneCollane instance;
    private ArrayList<CollanaFumetti> collaneFumetti;

    private CollezioneCollane() {
        collaneFumetti = new ArrayList<>();
    }

    public static CollezioneCollane getInstance() {
        if (instance == null) instance = new CollezioneCollane();
        return instance;
    }

    public void addCollanaFumetti(CollanaFumetti collanaFumetti) {
        collaneFumetti.add(collanaFumetti);
    }

    @Override
    public Iterator<CollanaFumetti> iterator() {
        return collaneFumetti.iterator();
    }

    public Map<Volume, Allegato> getMappaVolumiAllegati() {
        return collaneFumetti.stream()
                .map(CollanaFumetti::getVolumi)
                .flatMap(ArrayList::stream)
                .filter(x -> x.getClass() == VolumeSpeciale.class)
                .collect(Collectors.toMap(
                        (x -> x),
                        (x -> ((VolumeSpeciale)x).getAllegato())
                ));
    }

    public Map<Integer, Set<Volume>> getMappaAnniVolumi() {
        return collaneFumetti.stream()
                .map(CollanaFumetti::getVolumi)
                .flatMap(ArrayList::stream)
                .collect(Collectors.toMap(
                        (Volume::getAnnoPubblicazione),
                        (x -> {
                            HashSet<Volume> v = new HashSet<>();
                            v.add(x);
                            return v;
                        }),
                        ((set1, set2) -> {
                            set1.addAll(set2);
                            return set1;
                        })
                ));
    }

}
