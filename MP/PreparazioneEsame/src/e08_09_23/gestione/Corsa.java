package e08_09_23.gestione;

import java.util.Comparator;
import java.util.HashMap;
import java.util.TreeSet;

public class Corsa {
    private static int id;
    private Treno treno;
    private TreeSet<Stazione> stazioni;
    private HashMap<Stazione,Long> orari;

    public Corsa(Treno treno) {
        this.treno = treno;
        orari = new HashMap<>();
        stazioni = new TreeSet<>(Comparator.comparingLong(orari::get));
        id++;
    }

    public void addOrario(Stazione stazione, long orario) {
        orari.put(stazione, orario);
        stazioni.add(stazione);
    }

    public TreeSet<Stazione> getStazioni() { return stazioni; }
    public HashMap<Stazione,Long> getOrari() { return orari; }

}
