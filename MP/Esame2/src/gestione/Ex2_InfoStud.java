package gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ex2_InfoStud implements Iterable<Ex2_Studente> {
    private static Ex2_InfoStud instance;
    private ArrayList<Ex2_Studente> studenti;
    private ArrayList<Ex2_CorsoDegliStudi> corsiDegliStudi;

    private Ex2_InfoStud() {
        studenti = new ArrayList<>();
        corsiDegliStudi = new ArrayList<>();
    }

    public static Ex2_InfoStud getInstance() {
        if (instance == null) instance = new Ex2_InfoStud();
        return instance;
    }

    public void addStudente(Ex2_Studente studente) {
        studenti.add(studente);
    }

    public void removeStudente(Ex2_Studente studente) {
        studenti.remove(studente);
    }

    public void addCorso(Ex2_CorsoDegliStudi corso) {
        corsiDegliStudi.add(corso);
    }

    public void removeCorso(Ex2_CorsoDegliStudi corso) {
        corsiDegliStudi.remove(corso);
    }

    @Override
    public Iterator<Ex2_Studente> iterator() {
        return studenti.iterator();
    }

    public Iterator<Ex2_CorsoDegliStudi> iteratorCorsoDegliStudi() {
        return corsiDegliStudi.iterator();
    }

    public Map<Integer, Set<Ex2_Studente>> getMappaVotiStudenti(Ex2_Insegnamento insegnamento) {
        return studenti.stream()
                .filter(x -> x.getMappaInsegnamentoVoti().containsKey(insegnamento))
                .collect(Collectors.toMap(
                        (x -> x.getMappaInsegnamentoVoti().get(insegnamento)),
                        (Set::of),
                        ((set1, set2) -> {
                            set1.addAll(set2);
                            return set1;
                        })
                ));
    }

    public Map<Ex2_Studente, Double> getMediaVoti() {
        return studenti.stream()
                .collect(Collectors.toMap(
                        (x -> x),
                        (x -> x.getMappaInsegnamentoVoti().values().stream().mapToDouble(v -> v).average().orElse(0))
                ));
    }
}
