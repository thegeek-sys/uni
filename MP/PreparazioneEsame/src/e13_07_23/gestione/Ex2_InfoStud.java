package e13_07_23.gestione;

import java.util.*;
import java.util.stream.Collectors;

public class Ex2_InfoStud {
    private Ex2_InfoStud instance;
    private ArrayList<Studente> studenti;
    private ArrayList<CorsoDegliStudi> corsiDegliStudi;

    private Ex2_InfoStud() {
        studenti = new ArrayList<>();
        corsiDegliStudi = new ArrayList<>();
    }

    public Ex2_InfoStud getInstance() {
        if (instance == null) instance = new Ex2_InfoStud();
        return instance;
    }

    public void addStudente(Studente studente) { studenti.add(studente); }
    public void removeStudente(Studente studente) { studenti.remove(studente); }
    public ArrayList<Studente> getStudenti() { return studenti; }
    //public void addCorsoDegliStudi(CorsoDegliStudi corsoDegliStudi) { corsiDegliStudi.add(corsoDegliStudi); }

    public Iterator<Studente> studenteIterator() { return studenti.iterator(); }
    public Iterator<CorsoDegliStudi> corsoDegliStudiIterator() { return corsiDegliStudi.iterator(); }

    public Map<Integer, Set<Studente>> getMappaVotiStudenti(Insegnamento insegnamento) {
        return studenti.stream()
                .filter(s -> s.getVoti().containsKey(insegnamento))
                .collect(Collectors.groupingBy(
                        s -> s.getVoti().get(insegnamento),
                        Collectors.toSet()
                ));
    }

    public Map<Studente, Double> getMediaVoti() {
        return studenti.stream()
                .collect(Collectors.toMap(
                        s -> s,
                        s -> s.getVoti().values().stream().mapToInt(v -> v).average().orElse(0.0)
                ));
    }
}
