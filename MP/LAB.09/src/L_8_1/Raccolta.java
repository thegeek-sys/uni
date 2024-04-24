package L_8_1;

import java.util.HashSet;

public class Raccolta {
    private HashSet<Canzone> raccolta;

    public Raccolta(Canzone... canzoni) {
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
