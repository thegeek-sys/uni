package e13_06_23.ricorsione;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Ex3 {
    public static <T> List<T> filtraDoppioni(List<T> doppioni) {
        if (doppioni.size() == 1 || doppioni.isEmpty()) return doppioni;
        if (doppioni.getFirst().equals(doppioni.get(1)))
            doppioni.remove(doppioni.get(1));
        filtraDoppioni(doppioni.subList(1, doppioni.size()));
        return doppioni;
    }

    public static void main(String[] args) {
        ArrayList<String> d = new ArrayList<>();
        d.add("mario");
        d.add("luigi");
        d.add("luigi");
        d.add("peach");
        d.add("peach");
        System.out.println(d);
        System.out.println(filtraDoppioni(d));
    }
}
