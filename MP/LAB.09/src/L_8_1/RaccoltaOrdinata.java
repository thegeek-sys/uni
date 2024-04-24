package L_8_1;

import java.util.Comparator;
import java.util.TreeSet;

public class RaccoltaOrdinata {
    private TreeSet<Canzone> raccolta;

    public RaccoltaOrdinata(Canzone... canzoni) {
        for (Canzone canzone : canzoni) {
            raccolta.add(canzone);
        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        raccolta.forEach(x -> builder.append("\n").append(x.toString()));
        return builder.toString();
    }

}
